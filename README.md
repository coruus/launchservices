# Utilities to manage Mac OS X Launch Services.

Depends on [_pyobjc_](http://pythonhosted.org/pyobjc/).

At the moment, the only bit of this up here is _urlhandler.py_:

```
  Get and set OSX Launch Services's default handler for a URI scheme.
  
  Usage:
    urlhandler.py list <scheme>...
    urlhandler.py set-default --handler=<bundle_id> <scheme>...
  
  Commands:
    list          List all applications that are registered with Launch Services
                  as being able to handle each of the given URI schemes.
    set-default   Set the default application to <bundle_id> for each scheme
                  passed. (If you don't know the bundle ID, use list first.)
```

(Brew's version of _duti_ was not building on Mavericks and I really wanted `open https://...` to start Chrome Canary.)
