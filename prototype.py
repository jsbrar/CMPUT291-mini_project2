import os
from bsddb3 import db

def query4(oper, value, pile=[]):
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

def query6(oper, value, pile=[]):
    new_pile = []
    key = ["<=", ">=", "=", "<", ">"].index(oper)
    database = db.DB()
    dafile = "prices.idx"
    database.open(dafile, None, db.DB_BTREE)
    curs = database.cursor()    

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
            print(int(iter[0].decode("utf-8")), oper, value, aid[0])
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

def query7(loc, pile=[]):
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

def query8(cat, pile=[]):
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
    

def final(pile, setting):
    answer = []
    if setting == "brief":
        titles = open("titles.txt", "r")
        for item in pile:
            for title in titles:
                test = title.split(":")
                if test[1] == item:
                    answer.append(test[0])
    elif setting == "full":
        ads = open(ads.txt, "r")
        for item in pile:
            for ad in ads:
                test = ad.split(":")
                if test[0] == item:
                    answer.append(test[1])
    return answer

def main():
    pile = []
    pile = query6(">", 0, [])
    print(pile)
    print(len(pile))
    pile = query6("<", 300, pile)
    print(pile)
    print(len(pile))
    pile = query4(">", "2018/11/6", pile)
    print(pile)
    print(len(pile))
    
main()