import sys
import fileinput
import re
import pdb
import os
import time
from bsddb3 import db

def query1(word):
    database = db.DB()
    DB_File = "terms.idx"
    database.open(DB_File, None, db.DB_BTREE)
    curs = database.cursor()

    iter = curs.set_range(word.encode("utf-8")) #change camera to input string
    ad_ids_list = []
    while str(iter[0].decode("utf-8")) == word: #here as well
            ad_ids_list.append(str(iter[1].decode("utf-8")))  
            iter = curs.next()
    print(ad_ids_list)
    curs.close()
    database.close()
    print(ad_ids_list)
    return ad_ids_list

def borf(final_list,brief):
    if not brief:
        try:
            database = db.DB()
            DB_File = "ads.idx"
            database.open(DB_File, None, db.DB_HASH)
            curs = database.cursor()    
            for ad in final_list:
                iter = curs.set_range(ad.encode("utf-8"))
                while str(iter[0].decode("utf-8")) == ad:
                    print("Record: " + str(iter[1].decode("utf-8")))  
                    print(" ")
                    iter = curs.next() 
        except:
            pass
    else:
        try:
            database = db.DB()
            DB_File = "ads.idx"
            database.open(DB_File, None, db.DB_HASH)
            curs = database.cursor()    
            for ad in final_list:
                iter = curs.set_range(ad.encode("utf-8"))
                while str(iter[0].decode("utf-8")) == ad:
                    ad_code = str(iter[0].decode("utf-8"))
                    #print("Record: " + str(iter[1].decode("utf-8")))  
                    #print(" ")
                    line = str(iter[1].decode("utf-8"))
                    for i in range(len(line)-3):
                        if line[i] == "<" and line[i+1] == "t" and  line[i+2] == "i":
                            indexs = i+3
                            #print(indexs)
                    for i in range(len(line)-3):
                        if line[i] == "/" and line[i+1] == "t" and  line[i+2] == "i":
                            indexend = i-1
                            #print(indexend)
                    print(ad_code + ": "+line[indexs+1:indexend]) 
                        
                    
                #print(str(iter[0].decode("utf-8")))
                    iter = curs.next()     
        except:
            pass
    
        

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
def query5(MAX):
    MIN = 0
    #MAX = 20
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
            
            #print(full_list)
            curs.next()            
        iter = curs.next()
    
    curs.close()
    database.close()  
    return full_list
    
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

def query6(MAX):
    MIN = 0
    #MAX = 20
    database = db.DB()
    DB_File = "prices.idx"
    database.open(DB_File, None, db.DB_BTREE)
    curs = database.cursor()
    

    iter = curs.first()
    full_list = []
    while (iter):
        #print(int(iter[0].decode("utf-8"))>= MIN)
        #print(int(iter[0].decode("utf-8"))< MAX)
        if int(iter[0].decode("utf-8")) >= MIN and int(iter[0].decode("utf-8")) >= MAX:
            ad_id = str(iter[1].decode("utf-8"))
            ad_id2 = ad_id.split(",")
            a = ad_id2[0]
            full_list.append(a)      
            
            #print(full_list)
            curs.next()            
        iter = curs.next()
    
    curs.close()
    database.close()  
    
    return full_list
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

#date <= entered
def query3(one_date):
    #one_date = "2018/11/05"
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
        
        newdate1 = time.strptime(one_date,"%Y/%m/%d")
        newdate2 = time.strptime(index_date,"%Y/%m/%d")
        #print(newdate2 <= newdate1)
        if  newdate2 <= newdate1:
            ad_id = str(iter[1].decode("utf-8"))
            ad_id2 = ad_id.split(",")
            a = ad_id2[0]
            full_list.append(a)      
            
                
        iter = curs.next()
    #print(full_list)  
    curs.close()
    database.close()  
    
    return full_list

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
#date > entered
def query4(one_date):
    #one_date = "2018/11/05"
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
        
        newdate1 = time.strptime(one_date,"%Y/%m/%d")#date
        newdate2 = time.strptime(index_date,"%Y/%m/%d")# ///
        #print(newdate2 > newdate1)
        if  newdate2 > newdate1:
            ad_id = str(iter[1].decode("utf-8"))
            ad_id2 = ad_id.split(",")
            a = ad_id2[0]
            full_list.append(a)      
        iter = curs.next()
    #print(full_list)  
    curs.close()
    database.close()  
    return full_list 

    #database = db.DB()
    #DB_File = "ads.idx"
    #database.open(DB_File, None, db.DB_HASH)
    #curs = database.cursor()    
    #for ad in full_list:
        #try:
            #iter = curs.set_range(ad.encode("utf-8"))
            #while str(iter[0].decode("utf-8")) == ad:
                #print("Record: " + str(iter[1].decode("utf-8")))  
                #print(" ")
                #iter = curs.next() 
        #except:
            #pass
    #curs.close()
    #database.close()    
    
    
    

def main():
    continue_game = True
    while continue_game:    
        print("------------------------------")
        mess = []
        temp = []
        final = []
        quest = input("Enter valid query: ")
        
        brief = True
        change_o = input("modify output(y/n):")
        if change_o == "y":
            change = input("designate output:")
            if change == "output=full":
                brief = False
            elif change == "output=brief":
                brief = True
                
            
        for char in range(len(quest)):
            if quest[char] != '<' and quest[char] != '>' and quest[char] != '=' and quest[char] != '%':
                #print("flag0", quest[char])
                mess.append(quest[char])
                check = 0
            else:
                if quest[char] == '%':
                    mess.append(' % ')
                #print("flag1", quest[char])
                if quest[char] == '=' and check == 0:
                    mess.append(' ' + quest[char] + ' ')
                elif quest[char] == '<' or quest[char] == '>':
                    if quest[char+1] == '=':
                        check = 1
                        if quest[char] == '<':
                            mess.append(' <= ')
                        elif quest[char] == '>':
                            mess.append(' >= ')
                    else:
                        mess.append(' ' + quest[char] + ' ')
                
        print(mess) 
        mess = ''.join(mess)
        print(mess)
        
        temp = re.split(' ', mess)
        for part in temp:
            if part != '' and part != '\n':
                final.append(part)
        print(final)    
    
    
        #here
        if len(final) == 1:
            qresult = query1(str(final[0]))
            borf(qresult,brief)
            ans = input("contine(y/n)")
            if ans == "n":
                continue_game = False
                
        #if len(final) == 2 and final[1] == "%":
            #query2()
            #continue_game = False
            
        elif len(final) == 3 and final[0] == "date" and final[1] == "<=":
            qresult = query3(str(final[2]))
            borf(qresult,brief)
            ans = input("contine(y/n)")
            if ans == "n":
                continue_game = False    
                
        elif len(final) == 3 and final[0] == "date" and final[1] == ">":
            qresult = query4(str(final[2]))
            borf(qresult,brief)
            ans = input("contine(y/n)")
            if ans == "n":
                continue_game = False
        
        elif len(final) == 3 and final[0] == "price" and final[1] == "<": 
            qresult = query5(int(final[2]))
            borf(qresult,brief)
            ans = input("contine(y/n)")
            if ans == "n":
                continue_game = False 
            
        elif len(final) == 3 and final[0] == "price" and final[1] == ">=": 
            qresult = query6(int(final[2]))
            borf(qresult,brief)
            ans = input("contine(y/n)")
            if ans == "n":
                continue_game = False           
            
        
      
            
        
    #query1()
    #query2()
    #query3()
    #query4()
    #query5()
    #query6()
    
  
main()