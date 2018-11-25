import sys
import fileinput
import re
import pdb
import os

from bsddb3 import db

database = db.DB()
DB_File = "ads.idx"
database.open(DB_File, None, db.DB_HASH, db.DB_CREATE)

curs = database.cursor()

adfile = open("ads.txt", "r")

"""
for line in adfile:
    fix = line.split(":")
    'testa' = fix[0]
    'checka' = fix[1]
"""
    
curs.put(b'fix[0]', 'checka', db.DB_KEYFIRST)
curs.put(b'testb', 'checkb', db.DB_KEYFIRST)
curs.put(b'testc', 'checkc', db.DB_KEYFIRST)

itera = curs.first()
while itera:
    print(itera)
    itera = curs.next()