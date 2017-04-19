#!/usr/bin/env python3

import sys
import unicodedata


def print_unicode_table(words):
    filename = "unicode-table.txt"
    with open(filename, "w", encoding="utf8") as file:
        file.write("decimal   hex   chr  {0:^40}\n".format("name"))
        file.write("-------  -----  ---  {0:-<40}\n".format(""))

        code = ord(" ")
        end = min(0xD800, sys.maxunicode) # Stop at surrogate pairs

        while code < end:
            c = chr(code)
            name = unicodedata.name(c, "*** unknown ***")
            toprint = True
            for word in words:
                if word.lower() not in name.lower():
                    toprint = False
                    break
                if word is None or word.lower() in name.lower():
                    continue
                else:
                    toprint = False
            if toprint:
                file.write("{0:7}  {0:5X}  {0:^3c}  {1}\n".format(code, name.title()))
            code += 1
    print("wrote results to", filename)


words = None
if len(sys.argv) > 1:
    if sys.argv[1] in ("-h", "--help"):
        print("usage: {0} [string]".format(sys.argv[0]))
        words = 0
    else:
        words = sys.argv[1:]
if words != 0:
    print_unicode_table(words)
