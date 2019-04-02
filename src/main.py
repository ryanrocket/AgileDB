# ~/agileDB/src/main.py

import sys
import os
import time

global version
version = '0.1.3'

def getVer():
    return version

def sysout(absMes):
    # handle return messages from function and return to cli
    absMes = str(absMes)
    endStr = ("[ agile ] " + absMes)
    print(endStr)
