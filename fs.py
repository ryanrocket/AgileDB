# ~/agileDB/src/fs.py

import sys
import os
import time
import logging
import main
import pprint
import json

global curDb

## handlr
def handle(func):
    global curDb
    try:
        func()
    except:
        print("an internal error occured") if curDb else print("please define the database to use")

def use(dbname):
    global curDb
    curDb = str(dbname)
    main.sysout("database is now set to: " + curDb)

def back():
    global curDb
    curDb = ""
    main.sysout("no database selected")

def bscLog(mes):
    mes = ("[ agile ] " + mes) 
    logging.info(mes)

def init():
    # initialize the folder where data is stored
    os.system("mkdir agile_data")
    os.system("mkdir agile_data/stored_local")
    os.system("mkdir agile_data/stored_cloud")
    os.system("mkdir agile_data/metadata")
    os.system("touch agile_data/metadata/syslog.log")
    os.system("touch agile_data/metadata/verification.txt")
    logging.basicConfig(filename='agile_data/metadata/syslog.log', level=logging.DEBUG)
    main.sysout("filesystem initilized")
    bscLog("filesystem initilized")

def crtEmptDb(absFilNam):
    absFilNam = str(absFilNam)
    finFilNam = absFilNam + ".json"
    os.system("touch agile_data/stored_local/" + finFilNam)
    initStruct = {'<DB_NAME>': absFilNam}
    with open("agile_data/stored_local/" + finFilNam, 'w') as f:
        json.dump(initStruct, f)
        f.close()
    main.sysout("created database " + absFilNam)
    bscLog("created database " + absFilNam)

def delRegDb(reqDelNam):
    reqDelNam = str(reqDelNam)
    finDelNam = reqDelNam + ".json"
    os.system("rm -rf agile_data/stored_local/" + finDelNam)
    main.sysout("deleted database " + reqDelNam)
    bscLog("deleted database " + reqDelNam)


def addRelData(key, val):
    global curDb
    jsonfl = curDb + ".json"
    key = str(key)
    val = str(val)
    if "<" in key:
        print("you cannot include the characters < or > in your key")
    else:
        structUp = {key: val}
        with open("agile_data/stored_local/" + jsonfl, 'r') as f:
            localData = json.load(f)
            f.close()
        localData.update(structUp)
        with open("agile_data/stored_local/" + jsonfl, 'w') as f:
            json.dump(localData, f)
            f.close()
        main.sysout("relational value updated")
        bscLog("relational value updated")

def updRelData(key, val):
    addRelData(key, val)

 
def addListData(name):
    global curDb
    jsonfl = curDb + ".json"
    name = str(name)
    structUp = {name: []}
    with open("agile_data/stored_local/" + jsonfl, 'r') as f:
        localData = json.load(f)
        f.close()
    localData.update(structUp)
    with open("agile_data/stored_local/" + jsonfl, 'w') as f:
        json.dump(localData, f)
        f.close()
    main.sysout("list has been added")
    bscLog("list has been added")


def appListData(listname, val):
    global curDb
    jsonfl = curDb + '.json'
    listname = str(listname)
    val = str(val)
    ## structUp = {listname: [val]}
    with open("agile_data/stored_local/" + jsonfl, 'r') as f:
        localData = json.load(f)
        f.close()
    localData[listname].append(val)
    with open("agile_data/stored_local/" + jsonfl, 'w') as f:
        json.dump(localData, f)
        f.close()
    main.sysout("data was added to the list")
    bscLog("data was added to the list")


def display():
    global curDb
    jsonfl = curDb + '.json'
    with open("agile_data/stored_local/" + jsonfl, 'r') as f:
        localData = json.load(f)
        f.close()
    print(json.dumps(localData, indent=2, sort_keys=True))

def listDatabases():
    print (os.popen("ls agile_data/stored_local/").read())


def addDictData(name):
    global curDb
    jsonfl = curDb + ".json"
    name = str(name)
    structUp = {name: {}}
    with open("agile_data/stored_local/" + jsonfl, 'r') as f:
        localData = json.load(f)
        f.close()
    localData.update(structUp)
    with open("agile_data/stored_local/" + jsonfl, 'w') as f:
        json.dump(localData, f)
        f.close()
    main.sysout("dict has been added")
    bscLog("dict has been added")


def updDictData(name, key, val):
    global curDb
    jsonfl = curDb + '.json'
    name = str(name)
    val = str(val)
    key = str(key)
    ## structUp = {listname: [val]}
    with open("agile_data/stored_local/" + jsonfl, 'r') as f:
        localData = json.load(f)
        f.close()
    structUp = {key: val}
    localData[name].update(structUp)
    with open("agile_data/stored_local/" + jsonfl, 'w') as f:
        json.dump(localData, f)
        f.close()
    main.sysout("data was added to the dict")
    bscLog("data was added to the dict")

def select(type, keyOrg):
    global curDb
    jsonfl = curDb + ".json"
    keyOrg = str(keyOrg)
    with open("agile_data/stored_local/" + jsonfl, 'r') as f:
        localData = json.load(f)
        f.close()
    if (type == "rel"):
        for key, value in localData.items():
            if (key == keyOrg):
                outVal = value
                print(outVal)
    elif (type == "list"):
        for key, value in localData.items():
            if (key == keyOrg):
                outVal = value
                print(json.dumps(outVal, indent=2, sort_keys=True))
    elif (type == "dict"):
        for key, value in localData.items():
            if (key == keyOrg):
                outVal = value
                print(json.dumps(outVal, indent=2, sort_keys=True))
    else:
        main.sysout("invalid key type")

def addTag(tag):
    global curDb
    jsonfl = curDb + '.json'
    try:
        tag = int(tag)
    except:
        main.sysout("tag must be an integer")
    tag = str(tag)
    fullTag = "adb" + tag
    initStruct = {'<DB_TAG>': fullTag}
    with open("agile_data/stored_local/" + jsonfl, 'r') as f:
        localData = json.load(f)
        f.close()
    localData.update(initStruct)
    with open("agile_data/stored_local/" + jsonfl, 'w') as f:
        json.dump(localData, f)
        f.close()
    main.sysout("added db tag")
    bscLog("added db tag")

        
        

