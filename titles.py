import re
from bsddb3 import db

def titles(pile):
    tis = []
    database = db.DB()
    dafile = "ads.idx"
    database.open(dafile, None, db.DB_HASH)
    curs = database.cursor()
    
    for item in pile:
        iter = curs.first()
        while iter != None:
            aid = iter[0].decode("utf-8")
            total = iter[1].decode("utf-8")
            total = re.split("<|>", total)
            #print(aid)
            for x in range(len(total)):
                if total[x] == "ti":
                    #print("flag")
                    answer1 = total[x+1]
            #print(aid, item)
            if aid == item:
                tis.append(answer1) 
            iter = curs.next()
            
    database.close()
    return tis 
        
    
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

def main():
    #pile = []
    #pile = query2("Ken", [])
    #print(pile)
    pile = ['1002787981']
    ti = titles(pile)
    print(ti)
    
main()