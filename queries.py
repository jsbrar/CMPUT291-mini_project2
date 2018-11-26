import sys
import fileinput
import re
import pdb
import os
from bsddb3 import db

def query1():
    database = db.DB()
    DB_File = "terms.idx"
    database.open(DB_File, None, db.DB_BTREE)
    curs = database.cursor()

    iter = curs.set_range("camera".encode("utf-8")) 
    ad_ids_list = []
    while str(iter[0].decode("utf-8")) == "camera":
            ad_ids_list.append(str(iter[1].decode("utf-8")))  
            iter = curs.next()
    #print(ad_ids_list)
    
    database.close()
    database = db.DB()
    DB_File = "ads.idx"
    database.open(DB_File, None, db.DB_HASH)
    curs = database.cursor()    
    for ad in ad_ids_list:
        iter = curs.set_range(ad.encode("utf-8"))
        while str(iter[0].decode("utf-8")) == ad:
            print("Record: " + str(iter[1].decode("utf-8")))  
            print(" ")
            iter = curs.next()   
    



def main():
    print("------------------------------")
    #query1()
  
main()