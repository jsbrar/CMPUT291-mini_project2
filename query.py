import re

def query():
    mess = []
    quest = input("Enter valid query: ")
    for char in range(len(quest)):
        if quest[char] != '<' and quest[char] != '>' and quest[char] != '=':
            #print("flag0", quest[char])
            mess.append(quest[char])
            check = 0
        else:
            #print("flag1", quest[char])
            if quest[char] == '=' and check == 0:
                mess.append(quest[char])
            elif quest[char] == '<' or quest[char] == '>':
                if quest[char+1] == '=':
                    check = 1
                    if quest[char] == '<':
                        mess.append('<=')
                    elif quest[char] == '>':
                        mess.append('>=')
                else:
                    mess.append(quest[char])
            
    print(mess) 
      

def main():
    query()
    
main()