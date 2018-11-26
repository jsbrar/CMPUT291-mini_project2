def main():
    exit = False
    while exit == False:
        pile = [0]
        print("Welcome to Mini-project 2.")
        print("--------------------------")
        print("Option 1: Search Terms.")
        print("Option 2: Search Starting Terms.")
        print("Option 3: Search Dates.")
        print("Option 4: Search Prices.")
        print("Option 5: Search Locations.")
        print("Option 6: Search Categories.")
        print("Option 7: Finalize Query.")
        print("Option 8: Exit.")
        option = input("Choose an option: ")
        if option == 1:
            term = input("Enter a term to search: ")
            pile = query1(term, pile)
        elif option == 2:
            term = input("Enter a term to search: ")
            pile = query2(term, pile)
        elif option == 3:
            oper = input("Enter an operation: ")
            date = input("Enter a date to search (YYYY/MM/DD): ")
            pile = query3(oper, date, pile)
        elif option == 4:
            oper = input("Enter an operation: ")
            price = input("Enter a price to search: ")
            pile = query4(oper, price, pile)
        elif option == 5:
            loc = input("Enter a location to search: ")
            pile = query5(loc, pile)
        elif option == 6:
            cat = input("Enter a category to search: ")
            pile == query6(cat, pile)
        elif option == 7:
            for item in pile:
                print(item)
        elif option == 8:
            exit = True
        else:
            print("Invalid input.")
        
        if len(pile) == 0:
            print("No entries match your query.")