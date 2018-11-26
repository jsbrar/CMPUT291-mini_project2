import sys
import fileinput
import re
import pdb
import os
import time
from bsddb3 import db

# Finds term
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
    #print(ad_ids_list)
    curs.close()
    database.close()
    #print(ad_ids_list)
    return ad_ids_list

# Prints based on brief or full
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
                try:    
                    print("Record: " + str(iter[1].decode("utf-8")))  
                    print(" ")   
                except:
                    pass
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
                    
                    iter = curs.next() 
                try:
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
                except:
                    pass
                        
                    
                #print(str(iter[0].decode("utf-8")))
                        
        except:
            pass
    
        

# Price <         
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

#price >
def query5b(MAX):
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
        if int(iter[0].decode("utf-8")) >= MIN and int(iter[0].decode("utf-8")) > MAX:
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

# Price >=
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

#price <= 
def query6b(MAX):
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
        if int(iter[0].decode("utf-8")) >= MIN and int(iter[0].decode("utf-8")) <= MAX:
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

# Term%
def query2(word, pile=[]):
    new_pile = []
    database = db.DB()
    dafile = "ads.idx"
    database.open(dafile, None, db.DB_HASH)
    curs = database.cursor()
    
    if len(pile) != 0:
        for item in pile:
            iter = curs.first()
            while iter != None:
                a1 = True
                a2 = True                
                aid = iter[0].decode("utf-8")
                total = iter[1].decode("utf-8")
                total = re.split("<|>", total)
                for x in range(len(total)):
                    if total[x] == "ti":
                        answer1 = total[x+1]
                    if total[x] == "desc":
                        answer2 = total[x+1]
                for letter in range(len(word)):
                    if word[letter] != answer1[letter]:
                        a1 = False
                    if word[letter] != answer2[letter]:
                        a2 = False
                if (a1 == True or a2 == True) and aid == item:
                    new_pile.append(aid)
                iter = curs.next()
                
    else:
        iter = curs.first()
        while iter != None:
            a1 = True
            a2 = True                
            aid = iter[0].decode("utf-8")
            total = iter[1].decode("utf-8")
            total = re.split("<|>", total)
            for x in range(len(total)):
                if total[x] == "ti":
                    answer1 = total[x+1]
                if total[x] == "desc":
                    answer2 = total[x+1]
            #print(answer1, answer2)
            for letter in range(len(word)):
                if word[letter] != answer1[letter]:
                    a1 = False
                if word[letter] != answer2[letter]:
                    a2 = False
            if (a1 == True or a2 == True):
                new_pile.append(aid)
            iter = curs.next()        
            
    database.close()
    return new_pile 

# Date <=
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

# Date >=
def query3b(one_date):
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
        if  newdate2 >= newdate1:
            ad_id = str(iter[1].decode("utf-8"))
            ad_id2 = ad_id.split(",")
            a = ad_id2[0]
            full_list.append(a)      
            
                
        iter = curs.next()
    #print(full_list)  
    curs.close()
    database.close()  
    
    return full_list

# Date >
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
    
# Date <
def query4b(one_date):
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
        if  newdate2 < newdate1:
            ad_id = str(iter[1].decode("utf-8"))
            ad_id2 = ad_id.split(",")
            a = ad_id2[0]
            full_list.append(a)      
        iter = curs.next()
    #print(full_list)  
    curs.close()
    database.close()  
    return full_list 
    
def queryl4(oper, value, pile=[]):
    #print("flag 0 ", oper, value, pile)
    new_pile = []
    key = ["<=", ">=", "=", "<", ">"].index(oper)
    date = value.split("/")
    for item in range(len(date)):
        date[item] = int(date[item])
    database = db.DB()
    dafile = "pdates.idx"
    database.open(dafile, None, db.DB_BTREE)
    curs = database.cursor()

    if len(pile) != 0:
        for item in pile:
            iter = curs.first()
            while iter != None:
                aid = iter[1].decode("utf-8")
                aid = aid.split(",")
                temp = iter[0].decode("utf-8").split("/")
                for x in range(len(temp)):
                    temp[x] = int(temp[x])
                    
                if ((temp[0] < date[0]) or (temp[0] == date[0] and temp[1] < date[1]) or (temp[0] == date[0] and temp[1] == date[1] and temp[2] <= date[2])) and key == 0 and item == aid[0]: 
                    new_pile.append(aid[0]) 
                elif ((temp[0] > date[0]) or (temp[0] == date[0] and temp[1] > date[1]) or (temp[0] == date[0] and temp[1] == date[1] and temp[2] >= date[2])) and key == 1 and item == aid[0]:
                    new_pile.append(aid[0])
                elif temp == date and key == 2 and item == aid[0]:
                    new_pile.append(aid[0])
                elif ((temp[0] < date[0]) or (temp[0] == date[0] and temp[1] < date[1]) or (temp[0] == date[0] and temp[1] == date[1] and temp[2] < date[2])) and key == 3 and item == aid[0]:
                    new_pile.append(aid[0])
                elif ((temp[0] > date[0]) or (temp[0] == date[0] and temp[1] > date[1]) or (temp[0] == date[0] and temp[1] == date[1] and temp[2] > date[2])) and key == 4 and item == aid[0]:
                    new_pile.append(aid[0])
                iter = curs.next()
    else:
        iter = curs.first()
        while iter != None:
            aid = iter[1].decode("utf-8")
            aid = aid.split(",")
            temp = iter[0].decode("utf-8").split("/")
            for item in range(len(temp)):
                temp[item] = int(temp[item])

            if ((temp[0] < date[0]) or (temp[0] == date[0] and temp[1] < date[1]) or (temp[0] == date[0] and temp[1] == date[1] and temp[2] <= date[2])) and key == 0: 
                new_pile.append(aid[0])
            elif ((temp[0] > date[0]) or (temp[0] == date[0] and temp[1] > date[1]) or (temp[0] == date[0] and temp[1] == date[1] and temp[2] >= date[2])) and key == 1:
                new_pile.append(aid[0])
            elif temp == date and key == 2:
                new_pile.append(aid[0])
            elif ((temp[0] < date[0]) or (temp[0] == date[0] and temp[1] < date[1]) or (temp[0] == date[0] and temp[1] == date[1] and temp[2] < date[2])) and key == 3:
                new_pile.append(aid[0])
            elif ((temp[0] > date[0]) or (temp[0] == date[0] and temp[1] > date[1]) or (temp[0] == date[0] and temp[1] == date[1] and temp[2] > date[2])) and key == 4:
                new_pile.append(aid[0])
            iter = curs.next()

    database.close()
    return new_pile
# Price 
def queryl6(oper, value, pile=[]):
    new_pile = []
    key = ["<=", ">=", "=", "<", ">"].index(oper)
    database = db.DB()
    dafile = "prices.idx"
    database.open(dafile, None, db.DB_BTREE)
    curs = database.cursor()  
    
    value = int(value)

    if len(pile) != 0:
        for item in pile:
            iter = curs.first()
            while iter != None:
                aid = iter[1].decode("utf-8")
                aid = aid.split(",")
                #print(int(iter[0].decode("utf-8")), oper, value, "|", aid[0], "=", item)
                if int(iter[0].decode("utf-8")) <= value and key == 0 and aid[0] == item:
                    new_pile.append(aid[0])
                elif int(iter[0].decode("utf-8")) >= value and key == 1 and aid[0] == item:
                    new_pile.append(aid[0])
                elif int(iter[0].decode("utf-8")) == value and key == 2 and aid[0] == item:
                    new_pile.append(aid[0])
                elif int(iter[0].decode("utf-8")) < value and key == 3 and aid[0] == item:
                    new_pile.append(aid[0])
                elif int(iter[0].decode("utf-8")) > value and key == 4 and aid[0] == item:
                    new_pile.append(aid[0])
                iter = curs.next()
    else:
        iter = curs.first()
        while iter != None:
            aid = iter[1].decode("utf-8")
            aid = aid.split(",")
            #print(int(iter[0].decode("utf-8")), oper, value, aid[0])
            if int(iter[0].decode("utf-8")) <= value and key == 0:
                new_pile.append(aid[0])
            elif int(iter[0].decode("utf-8")) >= value and key == 1:
                new_pile.append(aid[0])
            elif int(iter[0].decode("utf-8")) == value and key == 2:
                new_pile.append(aid[0])
            elif int(iter[0].decode("utf-8")) < value and key == 3:
                new_pile.append(aid[0])
            elif int(iter[0].decode("utf-8")) > value and key == 4:
                new_pile.append(aid[0])
            iter = curs.next()
    
    database.close()
    return new_pile
# 
def queryl7(loc, pile=[]):
    new_pile = []
    database = db.DB()
    dafile = "pdates.idx"
    database.open(dafile, None, db.DB_BTREE)
    curs = database.cursor()

    if len(pile) != 0:
        for item in pile:
            iter = curs.first()
            while iter != None:
                aid = iter[1].decode("utf-8")
                aid = aid.split(",")

                if str(aid[2]) == loc and aid[0] == item:
                    new_pile.append(aid[0])
                iter = curs.next()
    else:
        iter = curs.first()
        while iter != None:
            aid = iter[1].decode("utf-8")
            aid = aid.split(",")
            
            if str(aid[2]) == loc:
                new_pile.append(aid[0])
            iter = curs.next()

    database.close()
    return new_pile

def queryl8(cat, pile=[]):
    new_pile = []
    database = db.DB()
    dafile = "pdates.idx"
    database.open(dafile, None, db.DB_BTREE)
    curs = database.cursor()

    if len(pile) != 0:
        for item in pile:
            iter = curs.first()
            while iter != None:
                aid = iter[1].decode("utf-8")
                aid = aid.split(",")
                if aid[1] == cat and aid[0] == item:
                    new_pile.append(aid[0])
                iter = curs.next()
    else:
        iter = curs.first()
        while iter != None:
            aid = iter[1].decode("utf-8")
            aid = aid.split(",")
            if aid[1] == cat:
                new_pile.append(aid[0])
            iter = curs.next()

    database.close()
    return new_pile
   

def main():
    continue_game = True
    brief = True
    while continue_game: 
        qresult = []
        print("------------------------------")
        mess = []
        temp = []
        final = []
        quest = input("Enter valid query: ")
        
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
                
        #print(mess) 
        mess = ''.join(mess)
        #print(mess)
        
        temp = re.split(' ', mess)
        for part in temp:
            if part != '' and part != '\n':
                final.append(part)
        #print(final)    
    
    
        #here
        if len(final) == 1:
            qresult = query1(str(final[0]))
            borf(qresult,brief)
            ans = input("contine(y/n)")
            if ans == "n":
                continue_game = False
                
        elif len(final) == 2 and final[1] == "%": #-------------------------------------------
            qresult = query2(final[0], qresult)
            borf(qresult,brief)
            ans = input("continue(y/n)")
            if ans == "n":
                continue_game = False
            
        elif len(final) == 3 and final[0] == "date" and final[1] == "<=":
            qresult = query3(str(final[2]))
            borf(qresult,brief)
            ans = input("contine(y/n)")
            if ans == "n":
                continue_game = False    
        elif len(final) == 3 and final[0] == "date" and final[1] == ">=":
            qresult = query3b(str(final[2]))
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
        
        elif len(final) == 3 and final[0] == "date" and final[1] == "<":
            qresult = query4b(str(final[2]))
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
        
        elif len(final) == 3 and final[0] == "price" and final[1] == ">": 
            qresult = query5b(int(final[2]))
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
        elif len(final) == 3 and final[0] == "price" and final[1] == "<=": 
            qresult = query6b(int(final[2]))
            borf(qresult,brief)
            ans = input("contine(y/n)")
            if ans == "n":
                continue_game = False                 
        #elif what conditions it happens under
           #call function have it return ad ids
           #borf(qresult,brief)
            #ans = input("contine(y/n)")
            #if ans == "n":
                #continue_game = False 
                
        elif len(final) == 3 and final[0] == "location":
            qresult = queryl7(final[2], qresult)
            borf(qresult,brief)
            ans = input("continue(y/n)")
            if ans == "n":
                continue_game = False
                
        elif len(final) == 3 and final[0] == "cat":
            qresult = queryl8(final[2], qresult)
            borf(qresult,brief)
            ans = input("continue(y/n)")
            if ans == "n":
                continue_game = False            
                
        elif len(final) > 3:
            oper = ["<=", ">=", "=", "<", ">"]
            s = []
            f = []
            for q in range(len(final)):
                if final[q] in oper:
                    s.append(final[q-1])
                    s.append(final[q])
                    s.append(final[q+1])
            for q in range(len(final)):
                if final[q] not in oper:
                    f.append(final[q])
            if len(f) == 2:
                qresult = query2(f[0], qresult)
            elif len(f) == 1:
                qresult = query1(f[0])
                
            for t in range(int(len(s) / 3)):
                if s[t*3] == "price":
                    qresult = queryl6(s[(t*3)+1], s[(t*3)+2], qresult)
                elif s[t*3] == "location":
                    qresult = queryl7(s[(t*3)+2], qresult)
                elif s[t*3] == "cat":
                    qresult = queryl8(s[(t*3)+2], qresult)
                elif s[t*3] == "date":
                    qresult = queryl4(s[(t*3)+1], s[(t*3)+2], qresult)
                    
            borf(qresult,brief)
            ans = input("continue(y/n)")
            if ans == "n":
                continue_game = False
            
        
      
            
        
    #query1()
    #query2()
    #query3()
    #query4()
    #query5()
    #query6()
    
  
main()