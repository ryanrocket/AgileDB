# ~/agileDB/src/cli.py

import sys
import os
import time
import logging
from main import *
import pprint
import json
from fs import *
import fs
import main

global fs
global main
global usrInp
global version
global status
global curDb
global stat

def getStat():
    global stat
    try:
        os.system("echo 'Scanning FS...'")
        stat ="WORKING"
    except:
        stat ="CORRUPT"

def run():
    global usrInp
    global version
    global status
    global curDb
    global stat
    # startup
    print("AgileDB by Ryan Wans")
    print("Running AgileDB Version " + main.version)
    print("AgileDB FS Configuration: " + stat)
    while (True):
        usrInp = input("[ agile ] ")
        cmd = usrInp.split()
        if (cmd[0] == 'use'):
            lcl = cmd[1]
            fs.use(lcl)
        elif (cmd[0] == ''):
            usrInp = input("[ agile ] ")
        elif (cmd[0] == 'exit'):
            exit()
        elif (cmd[0] == 'back'):
            fs.back()
        elif (cmd[0] == 'init'):
            fs.init()
        elif (cmd[0] == 'create'):
            lcl = cmd[1]
            fs.crtEmptDb(lcl)
        elif (cmd[0] == 'purge'):
            lcl = cmd[1]
            fs.delRegDb(lcl)
        elif (cmd[0] == 'add'):
            lcl = cmd[1]
            if (lcl == "rel"):
                ara = cmd[2]
                ere = cmd[3]
                fs.addRelData(ara, ere)
            elif (lcl == "list"):
                ara = cmd[2]
                fs.addListData(ara)
            elif (lcl == "dict"):
                ara = cmd[2]
                fs.addDictData(ara)
            elif (lcl == "tag"):
                ara = cmd[2]
                fs.addTag(ara)
        elif (cmd[0] == 'update'):
            lcl = cmd[1]
            ara = cmd[2]
            ere = cmd[3]
            if (lcl == 'rel'):
                fs.updRelData(ara, ere)
            elif (lcl == 'list'):
                fs.appListData(ara, ere)
            elif (lcl == 'dict'):
                eqe = cmd[4]
                fs.updDictData(ara, ere, eqe)
        elif (cmd[0] == 'display'):
            fs.display()
        elif (cmd[0] == 'list'):
            fs.listDatabases()
        elif (cmd[0] == 'select'):
            lcl = cmd[1]
            ara = cmd[2]
            fs.select(lcl, ara)
        else: 
            main.sysout("invalid command or arguments")

getStat()
while (True):
    run()
    continue
