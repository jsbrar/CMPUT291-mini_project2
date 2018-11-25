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

for line in adfile:
    fix = line.split(":")
    curs.put(fix[0], fix[1], db.DB_KEYFIRST)

iter = curs.first()
while iter:
    print(iter)
    iter = curs.next()