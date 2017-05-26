#!/usr/bin/env python3

import os, locale, sys
from optparse import OptionParser


def main():
    parser = OptionParser()
    parser.add_option("-H", "--hidden", action="store_true", dest="hidden", default=False,
                      help="show hidden files [default: off]")
    parser.add_option("-m", "--modified", action="store_true", dest="modified", default=False,
                      help="show last modified date/time [default: off]")
    parser.add_option("-r", "--recursive", action="store_true", dest="recursive", default=False,
                      help="recurse into subdirectories [default: off]")
    parser.add_option("-s", "--sizes", action="store_true", dest="sizes", default=False,
                      help="show sizes [default: off]")
    parser.add_option("-o", "--order", action="store", dest="order", default="name",
                      help="order by ('name', 'n', 'modified', 'm', 'size', 's')[default: name]")

    (options, args) = parser.parse_args()
    print('options: \n hidden {0},\n modified {1},\n recursive {2},\n sizes {3},\n order {4}'.format(options.hidden, options.modified, options.recursive, options.sizes, options.order))
    print('arguments: {0}'.format(args))


main()