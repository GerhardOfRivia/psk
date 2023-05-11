#!/usr/bin/env python3

# ./change [ options ] [ command ]
# options [ --debug or --list ]

import argparse
import os, sys
import subprocess
import difflib
import hashlib
import shlex

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        [hash_md5.update(c) in c for chunk in iter(lambda: f.read(4096), b"")]
    return hash_md5.hexdigest()

def list():
    fileName = str(__file__).strip('./')
    CONFIG_DIR = os.environ['HOME'] + "/.{}/".format(fileName)
    if not os.path.exists(CONFIG_DIR):
        print("Error: {} no commands have been entered.".format(__file__), file=sys.stderr)
        sys.exit(0)

    infoList = [f for f in os.listdir(CONFIG_DIR) if os.path.isfile(os.path.join(CONFIG_DIR, f))]
    if len(infoList) == 0:
        print("Error: {} no commands have been entered.".format(__file__), file=sys.stderr)
        sys.exit(0)

    regFile = CONFIG_DIR + "registry"
    if not os.path.exists(regFile):
        print("Error: {} no commands have been entered.".format(__file__), file=sys.stderr)
        sys.exit(0)

    with open(regFile, 'r') as r:
        info = r.readlines()

    for i in info:
        print(i.split(',')[0])

def run(COMMAND, MODE):
    if (MODE):
        print('{} started with command {}'.format(__file__, COMMAND))
    fileName = str(__file__).strip('./')
    CONFIG_DIR = os.environ['HOME'] + '/.{}/'.format(fileName)
    if not os.path.exists(CONFIG_DIR):
        os.makedirs(CONFIG_DIR)
    
    commandInput = "sh -c \"" + " ".join(COMMAND) + "\""
    commandStyle = shlex.split(commandInput)
    commandInfo = ""

    with subprocess.Popen(commandStyle, stdout=subprocess.PIPE) as proc:
        out, err = proc.communicate()
        commandInfo = out.decode().strip()
    
    changeReg = False
    md5Hash = hashlib.md5()
    md5Hash.update(" ".join(COMMAND).encode())
    hashVal = md5Hash.hexdigest()

    fileName = CONFIG_DIR + hashVal
    if os.path.exists(fileName):
        if (MODE):
            print("database contains info for command {}".format(COMMAND))
        fileInfo = ''
        with open(fileName, 'r') as w:
            fileInfo = ''.join(w.readlines()).strip()

        diff = difflib.ndiff(fileInfo.splitlines(keepends=True), 
                commandInfo.splitlines(keepends=True))
        changes = [l.rstrip() for l in diff if l.startswith('+ ') or l.startswith('- ')]
        if len(changes) > 0:
            for c in changes:
                print(c)
        elif (MODE):
            print("no changes to the command response {}".format(COMMAND))


    else:
        changeReg = True
        if (MODE):
            print("database will add command information {}".format(COMMAND))

    with open(fileName, "w") as w:
        w.write(commandInfo+"\n")

    if changeReg:
        commandString = ' '.join(COMMAND)
        if (MODE):
            print("adding [{}] to the database.".format(commandString))
        regFile = CONFIG_DIR + "registry"
        with open(regFile, 'a') as w:
            w.write(commandString+", "+hashVal+"\n")

def print_help():
    print("Usage: {} [ --list | --debug ] [ command ]".format(__file__), file=sys.stderr)
    print("[ --list  ] Show commands in database.", file=sys.stderr)
    print("[ --debug ] Show additional debugging info.", file=sys.stderr)
    sys.exit(0)

def main():
    fileName = str(__file__).strip('./')
    sys.argv.pop(0)
    command = sys.argv
    debug = False

    if len(command) == 1 and "--list" in command[0]:
        list()
        sys.exit(0)
    elif len(command) > 0 and "--list" in command[0]:
        print_help()
        sys.exit(1)
    elif len(command) > 1 and "--debug" in command[0]:
        command.pop(0)
        debug = True
    elif not len(command) > 0:
        print_help()
        sys.exit(1)

    run(command, debug)

if __name__ == "__main__":
    main()
