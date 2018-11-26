import sys
import fileinput
import re
import pdb
import os
from bsddb3 import db

def parse():
    ids = []
    dates = []
    locs = []
    cats = []
    tis = []
    descs = []
    prices = []
    inf = []
    total = []
    save = []
    for line in sys.stdin:
        inf.append(line)
        save.append(line)

    #print(save)

    for i in range(len(inf)):
        total.append([])

    count = 0
    for item in inf:
        #print("Before", item)
        item = re.split('<|>|\n', item)
        #print("After", item)
        for piece in item:
            if piece != '' and piece != '\n':
                total[count].append(piece)
        count += 1
    #print(total)
    
    for line in total:
        for item in range(len(line)):
            if line[item] == "aid":
                ids.append(line[item+1])
            elif line[item] == "date":
                dates.append(line[item+1])
            elif line[item] == "loc":
                locs.append(line[item+1])
            elif line[item] == "cat":
                cats.append(line[item+1])
            elif line[item] == "ti":
                tis.append(line[item+1])
            elif line[item] == "desc":
                descs.append(line[item+1])
            elif line[item] == "price":
                prices.append(line[item+1])
            else:
                pass

    term = [[0 for i in range(2)] for j in range(len(tis) + len(descs))]#[0][0] * (len(tis) + len(descs))
    count = 0
    for item in range(len(tis)):
        #print(item, tis[item])
        #pdb.set_trace()
        term[item][0] = re.findall('[a-z0-9_-][a-z0-9_-][a-z0-9_-]+', tis[item], flags=re.IGNORECASE)
        term[item][1] = ids[item]
        count += 1
        #print(tis[item], ' ', term[item][0])

    for item in range(len(descs)):
        term[item+count][0] = re.findall('[a-z0-9_-][a-z0-9_-][a-z0-9_-]+', descs[item], flags=re.IGNORECASE)
        term[item+count][1] = ids[item]

    tefile = open("terms.txt", "w+")
    pdfile = open("pdates.txt", "w+")
    prfile = open("prices.txt", "w+")
    adfile = open("ads.txt", "w+")

    count = 0
    for item in range(len(dates)):
        pdfile.write(str(dates[item]) + ":" + str(ids[item]) + ":" + str(cats[item]) + ":" + str(locs[item]) + '\n')
        prfile.write(str(prices[item]) + ":" + str(ids[item]) + "," + str(cats[item]) + "," + str(locs[item]) + '\n')
        adfile.write(str(ids[item]) + ":" + str(save[item+2]))
        for line in term:
            for t in line[0]:
                tefile.write(str(t).lower() + ":" + str(line[1]) + '\n')
                #print(t, line[1])
    
    tefile.close() 
    pdfile.close() 
    prfile.close() 
    adfile.close()    



def indexes():
    
    os.system('sort -u terms.txt > terms_sorted.txt')
    os.system('sort -u pdates.txt > pdates_sorted.txt')
    os.system('sort -u prices.txt > prices_sorted.txt')
    os.system('sort -u ads.txt > ads_sorted.txt')    
    
    #run perl script on all files, make new file
    os.system("perl break.pl < terms_sorted.txt > terms_new.txt")
    os.system("perl break.pl < pdates_sorted.txt > pdates_new.txt")
    os.system("perl break.pl < prices_sorted.txt > prices_new.txt")
    os.system("perl break.pl < ads_sorted.txt > ads_new.txt")
    
    # old file = new file
    os.system("mv terms_new.txt terms.txt")
    os.system("mv pdates_new.txt pdates.txt")
    os.system("mv prices_new.txt prices.txt")
    os.system("mv ads_new.txt ads.txt")
    
    #db_load
    os.system("db_load -c duplicates=1 -T -t btree -f terms.txt terms.idx")
    os.system("db_load -c duplicates=1 -T -t btree -f pdates.txt pdates.idx")
    os.system("db_load -c duplicates=1 -T -t btree -f prices.txt prices.idx")
    os.system("db_load -c duplicates=1 -T -t hash -f ads.txt ads.idx")


def main():
    print("------------------------------")
    parse()
    print("h")
    indexes()
    print("h")
  
    

main()