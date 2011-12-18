#!/usr/bin/env python

import plac
import logging

@plac.annotations(
    # arg=(helptext, kind, abbrev, type, choices, metavar)
    traditional=("use traditional greeting format", "flag", "t"),
    next_generation=("use next-generation greeting format", "flag", "n"),
    greeting=("use TEXT as the greeting message", "option", "g", str, None, "TEXT"),
    quiet=("Do not print informational messages.", "flag", "q"),
    verbose=("Print debug messages that are probably only useful if something is going wrong.", "flag", "v"),
    )
def main(traditional, next_generation, greeting=None,
         quiet=False, verbose=False,
         ):
    """Implementation of the standard 'hello world' program.

For the reference implementation, see http://www.gnu.org/s/hello/

This version differs from the reference implementation in some ways.
Its purpose is to demonstrate how to write a Python program using
'plac' for argument processing and 'logging' for status messages."""
    if quiet:
        logging.basicConfig(level=logging.WARN)
    elif verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)
    if traditional:
        logging.info("Using traditional greeting")
        if greeting:
            logging.warning("Overriding custom greeting with traditional one")
        greeting = "hello, world"
    elif greeting is None:
        logging.debug("Using default greeting")
        greeting = "Hello, world!"
    if next_generation:
        logging.info("Adding next-generation graphics.")
        glen = len(greeting)
        hline = '+-' + ('-' * glen) + '-+'
        greeting = "%s\n| %s |\n%s" % (hline, greeting, hline)
    print greeting

# Entry point
def plac_call_main():
    return plac.call(main)

if __name__=="__main__":
    plac_call_main()
