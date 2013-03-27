import os
import logging

APP_ROOT_DIR = os.path.abspath(os.path.dirname(__file__))

# If we're debugging, turn the cache off, etc.
# Set to true if we want to have our webapp print stack traces, etc
DEBUG = os.environ['SERVER_SOFTWARE'].startswith('Dev')
logging.info("Starting application in DEBUG mode: %s", DEBUG)

# Don't change default_blog or default_page to prevent conflicts when merging #  Bloog source code updates.
# Do change blog or page dictionaries at the bottom of this config module.

BLOG = {
    "bloog_version": "0.8",
    "html_type": "text/html",
    "charset": "utf-8",
    "title": "The AppScale Blog",
    "author": "AppScale Systems, Inc.",
    # This must be the email address of a registered administrator for the 
    # application due to mail api restrictions.
    "email": "chris@appscale.com",
    "description": "Making Cloud Software Easy to Use",
    "root_url": "http://blog.appscale.com",
    "master_atom_url": "/feeds/atom.xml",
    # By default, visitors can comment on article for this many days.
    # This can be overridden by setting article.allow_comments
    "days_can_comment": 60,
    # You can override this default for each page through a handler's call to 
    #  view.ViewPage(cache_time=...)
    "cache_time": 0, #if DEBUG else 3600,

    # Use the default YUI-based theme.
    # If another string is used besides 'default', calls to static files and
    #  use of template files in /views will go to directory by that name.
    "theme": ["default"],
    
    # Display gravatars alongside user comments?
    "use_gravatars": True,
    
    # Do you want to be emailed when new comments are posted?
    "send_comment_notification": True,

    # If you want to use legacy ID mapping for your former blog platform,
    # define it here and insert the necessary mapping code in the
    # legacy_id_mapping() function in ArticleHandler (blog.py).
    # Currently only "Drupal" is supported.
    "legacy_blog_software": None,
    #"legacy_blog_software": "Drupal",
    #"legacy_blog_software": "Serendipity",
    
    # If you want imported legacy entries _not_ mapped in the file above to
    # redirect to their new permanent URL rather than responding on their
    # old URL, set this flag to True.
    "legacy_entry_redirect": False,
}

PAGE = {
    "title": BLOG["title"],
    "articles_per_page": 20,
    "navlinks": [
        { "title": "Documentation",
	  "description": "Documentation", 
          "url": "/articles"} ,
        #{ "title": "Contact", "description": "Send me a note", 
          #"url": "/contact"},
    ],
    "featuredMyPages": {
        "title": "Community",
        "description": "Learn about AppScale",
        "entries": [
            { "title": "Our Web Site", 
              "url": "http://www.appscale.com", 
              "description": "What AppScale can do for you" },
            { "title": "Community Site",
              "url": "http://community.appscale.com", 
              "description": "Check out what features we're working on!" },
            { "title": "Download AppScale",
              "url": "http://download.appscale.com", 
              "description": "Download VirtualBox, Eucalyptus, and EC2 images"},
            { "title": "Source", 
              "url": "http://www.github.com/AppScale/appscale", 
              "description": "Fork us on GitHub!" },
            { "title": "Wiki", 
              "url": "http://www.github.com/AppScale/appscale/wiki", 
              "description": "Read our documentation" },
            { "title": "Mailing List", 
              "url": "http://groups.google.com/group/appscale_community", 
              "description": "Join our community!" }
        ]
    },
    "featuredOthersPages": {
        "title": "Google App Engine",
        "description": "Developer Resources",
        "entries": [
            { "title": "Google App Engine", 
              "url": "http://code.google.com/appengine/", 
              "description": "The mothership" },
            { "title": "App Engine Group", 
              "url": "http://groups.google.com/group/google-appengine", 
              "description": "Developer group" },
            { "title": "App Engine Open Source", 
              "url": "http://groups.google.com/group/google-appengine/web/google-app-engine-open-source-projects", 
              "description": "Code!" },
            { "title": "App Engine Console", 
              "url": "http://appengine.google.com", 
              "description": "Your apps" }
        ]
    },
}
