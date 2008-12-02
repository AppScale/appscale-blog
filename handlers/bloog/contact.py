# The MIT License
# 
# Copyright (c) 2008 William T. Katz
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to 
# deal in the Software without restriction, including without limitation 
# the rights to use, copy, modify, merge, publish, distribute, sublicense, 
# and/or sell copies of the Software, and to permit persons to whom the 
# Software is furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER 
# DEALINGS IN THE SOFTWARE.

"""
contact.py
This module provides a simple form for entering a message and the
handlers for receiving the message through a HTTP POST.
"""
__author__ = 'William T. Katz'

import hmac
import logging
import string
import time

from google.appengine.api import users

from handlers import restful
import view
import config

class ContactHandler(restful.Controller):
    def get(self):
        # Generate a token from the current time and its hmac, using the email
        # address as key. This ensures that we will only accept submissions
        # within a limited window, and that nobody can forge the token without
        # knowing the destination email address anyway.
        now = long(time.time())
        hm = hmac.new(config.BLOG['email'], str(now)).hexdigest()
        token = "%d:%s" % (now, hm)
        
        user = users.get_current_user()
        # Don't use cache since we want to get current time for each post.
        view.ViewPage(cache_time=0). \
             render(self, {'email': user.email() if user else 'Required',
                           'nickname': user.nickname() if user else '',
                           'token': token})

    def post(self):
        from google.appengine.api import mail

        token = self.request.get('token', None)
        validated = False
        if ':' in token:
            issued, hm = token.split(':')
            age = time.time() - long(issued)
            if hmac.new(config.BLOG['email'], str(issued)).hexdigest() == hm:
                logging.info("Valid token found with age %d.", age)
                if age >= 5 and age <= 3600:
                    validated = True
        if not validated:
            logging.info("Aborted contact mailing because token was invalid or "
                         "expired.")
            self.error(403)
            return

        user = users.get_current_user()
        sender = user.email() if user else config.BLOG['email']
        reply_to = self.request.get('email') or \
                   (user_email() if user else 'unknown@foo.com')
        mail.send_mail(
            sender = sender,
            reply_to = self.request.get('author') + '<' + reply_to + '>',
            to = config.BLOG['email'],
            subject = self.request.get('subject') or 'No Subject Given',
            body = self.request.get('message') or 'No Message Given'
        )

        view.ViewPage(cache_time=36000).render(self)