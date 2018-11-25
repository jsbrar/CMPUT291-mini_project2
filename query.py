import re

def query():
    mess = []
    quest = input("Enter valid query: ")
    for char in range(len(quest)):
        if quest[char] != '<' or quest[char] != '>' or quest[char] != '=':
            mess.append(quest[char])
            check = 0
        else:
            if quest[char] == '=' and check == 0:
                mess.append(quest[char])
            else:
            check = 1
            
        #print(mess) 
    
    for char in range(len(mess)):
        if mess[char] == '<'
      

def main():
    query()
    
main()