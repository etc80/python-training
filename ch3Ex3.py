#!/usr/bin/env python3

import collections
import sys


ID, FORENAME, MIDDLENAME, SURNAME, DEPARTMENT = range(5)

User = collections.namedtuple("User",
            "username forename middlename surname id")

NAMEWIDTH = 17
USERNAMEWIDTH = 9

def main():
    if len(sys.argv) == 1 or sys.argv[1] in {"-h", "--help"}:
        print("usage: {0} file1 [file2 [... fileN]]".format(
              sys.argv[0]))
        sys.exit()

    usernames = set()
    users = {}
    for filename in sys.argv[1:]:
        with open(filename, encoding="utf8") as file:
            for line in file:
                line = line.rstrip()
                if line:
                    user = process_line(line, usernames)
                    users[(user.surname.lower(), user.forename.lower(),
                            user.id)] = user
    print_users(users)


def process_line(line, usernames):
    fields = line.split(":")
    username = generate_username(fields, usernames)
    user = User(username, fields[FORENAME], fields[MIDDLENAME],
                fields[SURNAME], fields[ID])
    return user


def generate_username(fields, usernames):
    username = ((fields[FORENAME][0] + fields[MIDDLENAME][:1] +
                 fields[SURNAME]).replace("-", "").replace("'", ""))
    username = original_name = username[:8].lower()
    count = 1
    while username in usernames:
        username = "{0}{1}".format(original_name, count)
        count += 1
    usernames.add(username)
    return username


def print_headers():
    print("{0:<{nw}} {1:^6} {2:{uw}} {0:<{nw}} {1:^6} {2:{uw}}".format(
        "Name", "ID", "Username", nw=NAMEWIDTH, uw=USERNAMEWIDTH))
    print("{0:-<{nw}} {0:-<6} {0:-<{uw}} {0:-<{nw}} {0:-<6} {0:-<{uw}}".format(
        "", nw=NAMEWIDTH, uw=USERNAMEWIDTH))


def print_users(users):

    print_headers()

    lineend = ''
    counter = 1

    for key in sorted(users):
        user = users[key]
        initial = ""
        if user.middlename:
            initial = " " + user.middlename[0]
        name = "{0.surname}, {0.forename}{1}".format(user, initial)
        if len(name) >= 17:
            name = name[:17]
        if counter % 2 == 0:
            lineend = '\n'
        else:
            lineend = ' '
        print("{0:.<{nw}} ({1.id:4}) {1.username:{uw}}".format(
              name, user, nw=NAMEWIDTH, uw=USERNAMEWIDTH), end=lineend)
        if counter % 128 == 0:
            print('\f')

        counter += 1


main()
