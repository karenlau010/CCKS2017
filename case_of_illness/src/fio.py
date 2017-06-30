# coding:utf-8
import sys
import os
import codecs

datadir = "../data2/training dataset v4"

def ReadFile(file):

    f = open(file,'r')
    lines = f.readlines()
    f.close()
    
    return [line.rstrip('\r\n') for line in lines]

def ReadFileUTF8(file):

    f = codecs.open(file,'r', 'utf8')
    lines = f.readlines()
    f.close()
    
    return [line.rstrip() for line in lines]

def SaveFeatures(features, file, linetag="\n"):

    reload(sys)
    sys.setdefaultencoding('utf8')
    
    f = open(file, "w")
    for [token,tag] in features:
        f.write(token + " " + tag)
        f.write(linetag)
    f.flush()
    f.close()

def AddTrain(features, file, linetag="\n"):
    
    reload(sys)
    sys.setdefaultencoding('utf8')
    
    f = open(file, "a")
    for [token,tag1,tag2] in features:
        f.write(token + " " + tag1 + " " + tag2)
        f.write(linetag)
    f.flush()
    f.close()

def AddTest(features, file, linetag="\n"):
    
    reload(sys)
    sys.setdefaultencoding('utf8')
    
    f = open(file, "a")
    for token in features:
        f.write(token)
        f.write(linetag)
    f.flush()
    f.close()

if __name__ == '__main__':
    lines = ReadFileUTF8(datadir+'/病史特点/病史特点-1.txtoriginal.txt');
    for line in lines:
        print line