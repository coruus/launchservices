#!/usr/bin/env python
"""Get and set OSX Launch Services's default URL handler for a URL scheme.

Usage:
  urlhandler.py list <scheme>...
  urlhandler.py set-default --handler=<bundle_id> <scheme>...

Commands:
  list          List all applications that are registered with Launch Services
                as being able to handle each of the given URI schemes.
  set-default   Set the default application to <bundle_id> for each scheme
                passed. (If you don't know the bundle ID, use list first.)

"""
from clint.textui import puts, puts_err, indent
from clint.textui.colored import red, green, blue
from docopt import docopt

from LaunchServices import LSCopyAllHandlersForURLScheme, \
        LSCopyDefaultHandlerForURLScheme, LSSetDefaultHandlerForURLScheme


def list_schemes(schemes):
    """List the bundles that can handle each of the URI schemes"""
    for scheme in schemes:
        puts('{}:'.format(blue(scheme)))
        default_handler = LSCopyDefaultHandlerForURLScheme(scheme)
        handlers = LSCopyAllHandlersForURLScheme(scheme)
        with indent(2):
            if not handlers:
                puts(red('No handlers registered for {}'.format(scheme)))
                continue
            for handler in handlers:
                if handler == default_handler:
                    puts(green(handler))
                else:
                    puts(handler)


def set_default(bundle_id, schemes):
    """Set the default bundle to handle a URI scheme"""
    for scheme in schemes:
        status = LSSetDefaultHandlerForURLScheme(scheme, bundle_id)
        if status == 0:
            puts('set handler for "{}" to "{}"'
                 .format(blue(scheme), green(bundle_id)))
        else:
            puts_err(red('An error occurred trying to set "{}" '
                         'to handle "{}"'.format(bundle_id, scheme)))


def run(arguments):
    """Entry point for command-line use"""
    if arguments['list']:
        list_schemes(arguments['<scheme>'])
        return
    if arguments['set-default']:
        set_default(arguments['--handler'], arguments['<scheme>'])


if __name__ == '__main__':
    arguments = docopt(__doc__, version="urlhandler.py 0.0.1")
    run(arguments)
