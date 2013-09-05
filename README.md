# Utilities to manage Mac OS X Launch Services.

Depends on pyobjc.

At the moment, the only bit of this up here is urlhandler.py:

  Get and set OSX Launch Services's default URL handler for a URL scheme.
  
  Usage:
    urlhandler.py list <scheme>...
    urlhandler.py set-default --handler=<bundle_id> <scheme>...
  
  Commands:
    list          List all applications that are registered with Launch Services
                  as being able to handle each of the given URI schemes.
    set-default   Set the default application to <bundle_id> for each scheme
                  passed. (If you don't know the bundle ID, use list first.)


