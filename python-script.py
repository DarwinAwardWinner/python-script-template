#!/usr/bin/env python

import plac
import logging

@plac.annotations(
    # arg=(helptext, kind, abbrev, type, choices, metavar)
    # [INSERT ARGS HERE]
    quiet=("Do not print informational messages.", "flag", "q"),
    verbose=("Print debug messages that are probably only useful if something is going wrong.", "flag", "v"),
    )
def main(# [INSERT ARGS HERE],
         quiet=False, verbose=False,
         ):
    """Short description

Long description."""
    if quiet:
        logging.basicConfig(level=logging.WARN)
    elif verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)
    # [INSERT CODE HERE]
    pass

# Entry point
def plac_call_main():
    return plac.call(main)

if __name__=="__main__":
    plac_call_main()
