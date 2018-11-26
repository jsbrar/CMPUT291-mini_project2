import sys
import fileinput
import re
import pdb
import os
import time
from bsddb3 import db

def query1():
    word = "camera"
    database = db.DB()
    DB_File = "terms.idx"
    database.open(DB_File, None, db.DB_BTREE)
    curs = database.cursor()

    iter = curs.set_range(word.encode("utf-8")) #change camera to input string
    ad_ids_list = []
    while str(iter[0].decode("utf-8")) == word: #here as well
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
    database.close()

def query2(): #query 2 need major changes
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
    
    curs.close()
    database.close()
    database = db.DB()
    DB_File = "ads.idx"
    database.open(DB_File, None, db.DB_HASH)
    curs = database.cursor()    
    for ad in ad_ids_list:
        iter = curs.set_range(ad.encode("utf-8"))
        while str(iter[0].decode("utf-8")) == ad:
            line = str(iter[1].decode("utf-8"))
            for i in range(len(line)):
                if i <= (len(line) - 9):
                    if line[i] == "t" and line[i+1] == "i" and line[i+2] == ">" and line[i+3] == "c" and line[i+4] == "a" and line[i+5] == "m" and line[i+6] == "e" and line[i+7] == "r" and line[i+8] == "a":
                        print(" ")
                        print("Record: " + str(iter[1].decode("utf-8")))
                    if i <= (len(line) - 9):
                        if line[i] == "s" and line[i+1] == "c" and line[i+2] == ">" and line[i+3] == "c" and line[i+4] == "a" and line[i+5] == "m" and line[i+6] == "e" and line[i+7] == "r" and line[i+8] == "a":
                            print(" ")
                            print("Record: " + str(iter[1].decode("utf-8")))                     
            iter = curs.next() 
            
    curs.close()
    database.close()
# <        
def query5():
    MIN = 0
    MAX = 20
    database = db.DB()
    DB_File = "prices.idx"
    database.open(DB_File, None, db.DB_BTREE)
    curs = database.cursor()
    

    iter = curs.first()
    full_list = []
    while (iter):
        #print(int(iter[0].decode("utf-8"))>= MIN)
        #print(int(iter[0].decode("utf-8"))< MAX)
        if int(iter[0].decode("utf-8")) >= MIN and int(iter[0].decode("utf-8")) < MAX:
            ad_id = str(iter[1].decode("utf-8"))
            ad_id2 = ad_id.split(",")
            a = ad_id2[0]
            full_list.append(a)      
            
            print(full_list)
            curs.next()            
        iter = curs.next()
    
    curs.close()
    database.close()  
    
    database = db.DB()
    DB_File = "ads.idx"
    database.open(DB_File, None, db.DB_HASH)
    curs = database.cursor()    
    for ad in full_list:
        iter = curs.set_range(ad.encode("utf-8"))
        while str(iter[0].decode("utf-8")) == ad:
            print("Record: " + str(iter[1].decode("utf-8")))  
            print(" ")
            iter = curs.next() 
            
    curs.close()
    database.close()

def query6():
    MIN = 0
    MAX = 20
    database = db.DB()
    DB_File = "prices.idx"
    database.open(DB_File, None, db.DB_BTREE)
    curs = database.cursor()
    

    iter = curs.first()
    full_list = []
    while (iter):
        #print(int(iter[0].decode("utf-8"))>= MIN)
        #print(int(iter[0].decode("utf-8"))< MAX)
        if int(iter[0].decode("utf-8")) >= MIN and int(iter[0].decode("utf-8")) <= MAX:
            ad_id = str(iter[1].decode("utf-8"))
            ad_id2 = ad_id.split(",")
            a = ad_id2[0]
            full_list.append(a)      
            
            print(full_list)
            curs.next()            
        iter = curs.next()
    
    curs.close()
    database.close()  
    
    database = db.DB()
    DB_File = "ads.idx"
    database.open(DB_File, None, db.DB_HASH)
    curs = database.cursor()    
    for ad in full_list:
        iter = curs.set_range(ad.encode("utf-8"))
        while str(iter[0].decode("utf-8")) == ad:
            print("Record: " + str(iter[1].decode("utf-8")))  
            print(" ")
            iter = curs.next() 
            
    curs.close()
    database.close()   

#
def query3():
    one_date = "2018/10/05"
    #one_date = one_date.split("/")
    
    database = db.DB()
    DB_File = "pdates.idx"
    database.open(DB_File, None, db.DB_BTREE)
    curs = database.cursor()
    

    iter = curs.first()
    full_list = []
    while (iter):
        #print(int(iter[0].decode("utf-8"))>= MIN)
        #print(int(iter[0].decode("utf-8"))< MAX)
        index_date = str(iter[0].decode("utf-8"))
        #index_dates = index_dates.split("/")
        #dates <= input
        
        #print(datetime(int(one_date[0]),int(one_date[1]),int(one_date[2])) <= datetime(int(one_date[0]),int(one_date[1]),int(one_date[2])))
        
        newdate1 = time.strptime(one_date,"%d/%m/%Y")
        newdate2 = time.strptime(index_date,"%d/%m/%Y")
        if  newdate2 <= newdate1:
            ad_id = str(iter[1].decode("utf-8"))
            ad_id2 = ad_id.split(",")
            a = ad_id2[0]
            full_list.append(a)      
            
                
        iter = curs.next()
    print(full_list)  
    curs.close()
    database.close()  
    
    #database = db.DB()
    #DB_File = "ads.idx"
    #database.open(DB_File, None, db.DB_HASH)
    #curs = database.cursor()    
    #for ad in full_list:
        #iter = curs.set_range(ad.encode("utf-8"))
        #while str(iter[0].decode("utf-8")) == ad:
            #print("Record: " + str(iter[1].decode("utf-8")))  
            #print(" ")
            #iter = curs.next() 
            
    #curs.close()
    #database.close()    

    
    
    

def main():
    print("------------------------------")
    #query1()
    #query2()
    query3()
    #query5()
    #query6()
    
  
main()