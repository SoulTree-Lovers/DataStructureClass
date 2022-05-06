phonebook = dict()

def insert(name, number):
    phonebook[name] = number

def delete(name):
    return phonebook.pop(name)

def search(name):
    x = phonebook[name]
    return x

def scan():
    for i in phonebook:
        print(i, phonebook[i])




if __name__ == "__main__":
    while 1:
        choice = input("Select the menu. 1:insert, 2:delete, 3:search, 4:scan, 5:quit: ")
        if choice == "1":   #insert
            name = input("Type your name: ")
            number = input("Type your phone number: ")
            insert(name, number)
        elif choice == "2":     #delete
            name = input("Type your name: ")
            delete(name)
        elif choice == "3":     #search
            name = input("Type your name: ")
            number = search(name)
            print(number)
        elif choice == "4":     #scan
            scan()
        elif choice == "5":     #quit
            break
        else:
            print("Wrong number")
