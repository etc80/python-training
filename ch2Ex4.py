#!/usr/bin/env python3


import sys
import xml.sax.saxutils


def main():
    maxwidth, formatte = process_options(sys.argv)
    if maxwidth == None or formatte == None:
        sys.exit()
    print_start()
    count = 0
    while True:
        try:
            line = input()
            if count == 0:
                color = "lightgreen"
            elif count % 2:
                color = "white"
            else:
                color = "lightyellow"
            print_line(line, color, maxwidth, formatte)
            count += 1
        except EOFError:
            break
    print_end()


def print_start():
    print("<table border='1'>")


def print_line(line, color, maxwidth, formatt):
    print("<tr bgcolor='{0}'>".format(color))
    fields = extract_fields(line)
    for field in fields:
        if not field:
            print("<td></td>")
        else:
            number = field.replace(",", "")
            try:
                x = float(number)
                s = "<td align='right'>{0:" + formatt + "}</td>"
                print(s.format(round(x)))
            except ValueError:
                field = field.title()
                field = field.replace(" And ", " and ")
                if len(field) <= maxwidth:
                    field = xml.sax.saxutils.escape(field)
                else:
                    field = "{0} ...".format(
                        xml.sax.saxutils.escape(field[:maxwidth]))
                print("<td>{0}</td>".format(field))
    print("</tr>")


def extract_fields(line):
    fields = []
    field = ""
    quote = None
    for c in line:
        if c in "\"'":
            if quote is None:  # start of quoted string
                quote = c
            elif quote == c:  # end of quoted string
                quote = None
            else:
                field += c    # other quote inside quoted string
            continue
        if quote is None and c == ",":  # end of a field
            fields.append(field)
            field = ""
        else:
            field += c        # accumulating a field
    if field:
        fields.append(field)  # adding the last field
    return fields


def print_end():
    print("</table>")


def process_options(arguments):
    if len(arguments) <= 1:
        return 100, ".0f"
    elif arguments[1] == '-h' or arguments[1] == '--help':
        usage = ''' usage:
                    csv2html.py [maxwidth=int] [format=str] < infile.csv > outfile.html
                    
                    maxwidth is an optional integer; if specified, it sets the maximum
                    number of characters that can be output for string fields,
                    otherwise a default of 100 characters is used.
                    
                    format is the format to use for numbers; if not specified it
                    defaults to ".0f". '''
        print(usage)
        return None, None
    else:
        args = arguments[1:]
        for a in args:
            ar = a.split('=')
            key = ar[0]
            maxwidth, formatt = None, None
            if key == 'maxwidth':
                maxwidth = int(ar[1])
            elif key == 'format':
                formatt = str(ar[1])
        if maxwidth == None:
            maxwidth = 100
        if formatt == None:
            formatt = '.0f'
        return maxwidth, formatt


main()
