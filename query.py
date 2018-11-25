import re

def query():
    mess = []
    temp = []
    final = []
    quest = input("Enter valid query: ")
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
    
    oper = ["<=", ">=", "<", ">", "=", "%"]
    
    for item in range(len(final)):
        if final[item] == ">=":
            #query(final[item-1] >= final[item+1])
            pass
        elif final[item] == "<=":
            pass
        elif final[item] == "<":
            pass
        elif final[item] == ">":
            pass
        elif final[item] == "=":
            pass
        elif final[item] == "%":
            pass
        else:
            if item == 0:
                if final[item+1] not in oper:
                    pass
            elif item == len(final)-1:
                if final[item-1] not in oper:
                    pass
            else:
                if final[item-1] not in oper and final[item+1] not in oper:
                    pass

def main():
    query()
    
main()