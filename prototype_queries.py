import os

def query4(oper, value, pile=[]):
    new_pile = []
    key = ["<=", ">=", "=", "<", ">"].index(oper)
    date = value.split("/")
    for item in range(len(date)):
        date[item] = int(date[item])
    database = db.DB()
    dafile = "pdate.idx"
    database.open(dafile, None, db.BD_BTREE)
    curs = database.cursor()
    
    """
    if oper == "<=":
        iter = curse.set_range(value.encode("utf-8"), value.encode("utf-8"))
    elif oper == ">=":
        iter = curse.set_range(value.encode("utf-8"), None,  value.encode("utf-8"))
    elif oper == "=":
        iter = curs.set_range(value.encode("utf-8"))
    elif oper == "<":
        fixed = value.split("/")
        fixed[2] = str(int(fix[2] + 1))
        fixed = '/'.join(fixed)
        iter = curs.set_range(value.encode("utf-8"), fixed.encode("utf-8"))
    elif oper == ">":
        fixed = value.split("/")
        fixed[2] = str(int(fix[2] - 1))
        fixed = '/'.join(fixed)
        iter = curs.set_range(value.encode("utf-8"), None, fixed.encode("utf-8"))
        
    """

    iter = curs.set_range(value.encode("utf-8"))

    if len(pile) != 0:
        for item in pile:
            while iter != None:
                aid = iter[1].decode("utf-8")
                temp = iter[0].decode("utf-8").split("/")
                for item in range(len(temp)):
                    temp[item] = int(temp[item])

                if ((temp[0] < date[0]) or (temp[0] == date[0] and temp[1] < date[1]) or (temp[0] == date[0] and temp[1] == date[1] and temp[2] <= date[2])) and key == 0 and item == aid: 
                    #new_pile.append(aid) 
                    pass
                elif ((temp[0] > date[0]) or (temp[0] == date[0] and temp[1] > date[1]) or (temp[0] == date[0] and temp[1] == date[1] and temp[2] >= date[2])) and key == 1 and item == aid:
                    pass
                elif temp == date and key == 2 and item == aid:
                    pass
                elif ((temp[0] < date[0]) or (temp[0] == date[0] and temp[1] < date[1]) or (temp[0] == date[0] and temp[1] == date[1] and temp[2] < date[2])) and key == 3 and item == aid:
                    pass
                elif ((temp[0] > date[0]) or (temp[0] == date[0] and temp[1] > date[1]) or (temp[0] == date[0] and temp[1] == date[1] and temp[2] > date[2])) and key == 4 and item == aid:
                    pass
                iter = curs.next()
    else:
        while iter != None:
            aid = iter[1].decode("utf-8")
            temp = iter[0].decode("utf-8").split("/")
            for item in range(len(temp)):
                temp[item] = int(temp[item])

            if ((temp[0] < date[0]) or (temp[0] == date[0] and temp[1] < date[1]) or (temp[0] == date[0] and temp[1] == date[1] and temp[2] <= date[2])) and key == 0: 
                #new_pile.append(aid)
                pass
            elif ((temp[0] > date[0]) or (temp[0] == date[0] and temp[1] > date[1]) or (temp[0] == date[0] and temp[1] == date[1] and temp[2] >= date[2])) and key == 1:
                pass
            elif temp == date and key == 2:
                pass
            elif ((temp[0] < date[0]) or (temp[0] == date[0] and temp[1] < date[1]) or (temp[0] == date[0] and temp[1] == date[1] and temp[2] < date[2])) and key == 3:
                pass
            elif ((temp[0] > date[0]) or (temp[0] == date[0] and temp[1] > date[1]) or (temp[0] == date[0] and temp[1] == date[1] and temp[2] > date[2])) and key == 4:
                pass
            iter = curs.next()

    database.close()
    return new_pile

def query6(oper, value, pile=[]):
    new_pile = []
    key = ["<=", ">=", "=", "<", ">"].index(oper)
    database = db.DB()
    dafile = "price.idx"
    database.open(dafile, None, db.BD_BTREE)
    curs = database.cursor()

    iter = curs.set_range(value.encode("utf-8"))

    if len(pile) != 0:
        for item in pile:
            while iter != None:
                aid = iter[1].decode("utf-8")
                if int(iter[0].decode("utf-8")) <= value and key == 0 and aid == item:
                    #new_pile.append(aid)
                    pass
                elif int(iter[0].decode("utf-8")) >= value and key == 1 and aid == item:
                    pass
                elif int(iter[0].decode("utf-8")) == value and key == 2 and aid == item:
                    pass
                elif int(iter[0].decode("utf-8")) < value and key == 3 and aid == item:
                    pass
                elif int(iter[0].decode("utf-8")) > value and key == 4 and aid == item:
                    pass
                iter = curs.next()
    else:
        while iter != None:
            aid = iter[1].decode("utf-8")
            if int(iter[0].decode("utf-8")) <= value and key == 0:
                #new_pile.append(aid)
                pass
            elif int(iter[0].decode("utf-8")) >= value and key == 1:
                pass
            elif int(iter[0].decode("utf-8")) == value and key == 2:
                pass
            elif int(iter[0].decode("utf-8")) < value and key == 3:
                pass
            elif int(iter[0].decode("utf-8")) > value and key == 4:
                pass
            iter = curs.next()
    
    database.close()
    return new_pile

def query7(loc, pile=[]):
    new_pile = []
    database = db.DB()
    dafile = "pdates.idx"
    database.open(dafile, None, db.BD_BTREE)
    curs = database.cursor()

    iter = curs.set_range(loc.encode("utf-8"))

    if len(pile) != 0:
        for item in pile:
            while iter != None:
                aid = iter[1].decode("utf-8")
                if str(iter[0].decode("utf-8")) == loc and aid == item:
                    #new_pile.append(aid)
                    pass
                iter = curs.next()
    else:
        while iter != None:
            aid = iter[1].decode("utf-8")
            if str(iter[0].decode("utf-8")) == loc:
                #new_pile.append(aid)
                pass
            iter = curs.next()

    database.close()
    return new_pile

def query8(cat, pile=[]):
    new_pile = []
    database = db.DB()
    dafile = "pdates.idx"
    database.open(dafile, None, db.BD_BTREE)
    curs = database.cursor()

    iter = curs.set_range(cat.encode("utf-8"))

    if len(pile) != 0:
        for item in pile:
            while iter != None:
                aid = iter[1].decode("utf-8")
                if str(iter[0].decode("utf-8")) == cat and aid == item:
                    #new_pile.append(aid)
                    pass
                iter = curs.next()

    while iter != None:
        if str(iter[0].decode("utf-8")) == cat:
            #new_pile.append(aid)
            pass
        iter = curs.next()

    database.close()
    
"""
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
"""
