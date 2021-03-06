import sys
import fileinput
import re
import pdb

#Liam McDonald
#Note to self: use cmd on windows computer, cd to a2 and do python parse.py < test.txt

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
        prfile.write(str(prices[item]) + ":" + str(ids[item]) + ":" + str(cats[item]) + ":" + str(locs[item]) + '\n')
        adfile.write(str(ids[item]) + ":" + str(save[item+2]))
        for line in term:
            for t in line[0]:
                tefile.write(str(t) + ":" + str(line[1]) + '\n')
                print(t, line[1])
    
    tefile.close()
    pdfile.close()
    prfile.close()
    adfile.close()

def main():
    print("------------------------------")
    parse()

main()