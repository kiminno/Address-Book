def stateOptions():
    print("Enter the number corresponding to the action you wish to perform.")
    print("1. Add a contact")
    print("2. View all contacts")
    print("3. Delete a contact")
    print("4. Format address book")


def add():
    print("Enter the following information in the exact same format.")
    print("If information is unknown, write it as so: Name, , Phone, , ,")
    print("Name,Address,Phone,Mobile,E-mail")

    contact = input()
    
    file = open("Address Book.txt", 'a')
    file.write(contact + "\n")
    file.close()


def viewAll():
    file = open("Address Book.txt", 'r')
    contactList = file.readlines()
    file.close()

    if(len(contactList) == 0):
        print("Empty")
    
    for i in range(len(contactList)):
        contactInfo = contactList[i].split(",")
        print(i+1)
        print("Name:", contactInfo[0])
        print("Address:", contactInfo[1])
        print("Phone:", contactInfo[2])
        print("Mobile:", contactInfo[3])
        print("E-mail:", contactInfo[4])
        print("----------")


def delete():
    print("Enter the contact number that you wish to delete. It is located above 'Name'.")
    number = int(input())
    
    file = open("Address Book.txt", 'r')
    contactList = file.readlines()
    file.close()
    
    contactList.pop(number - 1)

    file = open("Address Book.txt", 'w')
    file.writelines(contactList)
    file.close()

    
def format():
    file = open("Address Book.txt", 'w')
    file.write("")
    file.close()


def chooseAction(option):
    if(option == 1):
        print("Add a contact")
        add()
    if(option == 2):
        print("View all contacts")
        viewAll()
    if(option == 3):
        print("Delete a contact")
        viewAll()
        delete()
        viewAll()
    if(option == 4):
        print("Format address book")
        format()
        viewAll()


def repeat():    
    print("Would you like to go back to the main menu?")
    print("1. Yes")
    print("2. No")
    
    yOrN = int(input())
    if(yOrN == 1):
        stateOptions()
        option = int(input())
        chooseAction(option)
        repeat()
    elif(yOrN == 2):
        quit()
    else:
        print("Please try again.")
        repeat()

        
stateOptions()
option = int(input())
chooseAction(option)
repeat()
