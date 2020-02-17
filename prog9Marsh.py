##Name: Ian Marsh
##Prog9Marsh.py
##
##Purpose: uses itemMarsh to return or change values of an item and also print all the info of name, quantity, and price
##
##Input: the choice from a list printed out at the start of the program will run different parts of the program
##
##Output: different outputs for different choices
##
## Certification of Authenticity:
##   I certify that this lab is entirely my own work.
##   

from itemMarsh import Item

# addItem
#
# ask for intput about name, quantity, and price and adds it to list
#
# Parameters:  listOfItems
#
# Returns:  newItem
def addItem(listOfItems):
    #get start vals
    print()
    print("Please provide information about the item to add.")
    userName = input("Please enter the name: ")
    userQuantity = int(input("Please enter the quantity: "))
    #checks val
    while(not(userQuantity>=1)):
        userQuantity = int(input("Please reenter the quantity: "))

    userPrice = float(input("Please enter the unit price: "))
    #checks val
    while(not(userPrice>0)):
        userPrice = float(input("Please reenter the unit price: "))
    newItem = Item(userName, userQuantity, userPrice)
    #prints info
    print()
    print(userName,"has been added to the cart.")
    return newItem

# deleteItem
#
# deletes item that user enters
#
# Parameters:  listOfItems and userCheck
#
# Returns:  the item to delete
def deleteItem(listOfItems, userCheck):
    itemLookFor = None
    userCheck = userCheck.lower()

    #Loop to check if it is = 
    for item in listOfItems:
        nameCheck = item.getName().lower()
        if(nameCheck == userCheck):
            itemLookFor = item
    return itemLookFor
    

# printList
#
# tkaes in list and prints it out and it it is empty it will say that
#
# Parameters:  nlistOfItemsone
#
# Returns:  none
def printList(listOfItems):
    #loop to get items and print
    for item in listOfItems:
        print(item)
    #if empty do this
    if(isListEmpty is True):
        print("The list is empty")

# search
#
# ask for intput of the item you are looking for and prints if they have it
#
# Parameters:  listOfItems userCheck
#
# Returns:  none
def search(listOfItems, userCheck):
    #start vals
    total = 0
    itemLookFor = None
    
    userCheck = userCheck.lower()

    #Loop to check if it is = 
    for item in listOfItems:
        nameCheck = item.getName().lower()
        if(nameCheck == userCheck):
            total += 1
            itemLookFor = item
    print()
    #prints info
    if(total == 0):
        print("No, you do not have any of that item.")
    else:
        print("Yes, you have", itemLookFor.getQuantity(), itemLookFor.getName(), "at ${0:0.2f}".format(itemLookFor.getPrice()),"each.")

# countItems
#
# ask for intput of neg and then runs through the loop until user stops or hits 10
#
# Parameters:  none
#
# Returns:  none
def countItems(listOfItems):
    #start vals and loops to get the amount of every item
    total = 0
    for item in listOfItems:
        total += item.getQuantity()
    print()
    print("Your cart contains a total of", total,"items.")

# totalCost
#
# finds the total of all items
#
# Parameters:  none
#
# Returns:  none
def totalCost(listOfItems):
    #loops to get price * amount and prints
    total = 0
    for item in listOfItems:
        total += item.getPrice()*item.getQuantity()
    print()
    print("The total price of all of your items is ${0:0.2f}.".format(total))

# isListEmpty
#
# checks if list is empty
#
# Parameters:  listOfItems
#
# Returns:  true or flase
def isListEmpty(listOfItems):
    #checks if the len is 0
    print()
    flag = None
    if(len(listOfItems) == 0):
        print("The list is empty")
        flag = True
    else:
        print("The list is not empty")
        flag = False
    return flag

# clearList
#
# clears the list
#
# Parameters:  none
#
# Returns:  none
def clearList():
    listOfItems = []
    print("The list is now empty")

def main():
    shoppingList = []
    #inputs
    file = input("Please enter the path and name for the data file: ")
    theFile = open(file,"r")
    numerOfIteams = int(theFile.readline())
    
    #gets info from file
    for line in range(numerOfIteams):
        
        namee = theFile.readline().strip()
        quantitye = int(theFile.readline())
        coste = float(theFile.readline())
        
        newItem = Item(namee, quantitye, coste)
        shoppingList.append(newItem)

    print()
    print("1. Add an item to the list")
    print("2. Delete an item from the list")
    print("3. Print each item in the list")
    print("4. Search for a user-specified item in the list")
    print("5. Count the total number of items in the list")
    print("6. Total the cost of the items in the list")
    print("7. Determine whether the list is empty")
    print("8. Clear the list")
    print("0. Quit")
    print()

    
    userInput = input("Enter an input: ")
    

    #if the user does not put in 0 then it will still run
    while(userInput != "0"):
        
        if(userInput == "1"):
            newItem = addItem(shoppingList)
            shoppingList.append(newItem)

        elif(userInput == "2"):
            print()
            userInput = input('Please enter the name of the item to delete in your cart: ')
            
            itemToDel = deleteItem(shoppingList,userInput)
            if(itemToDel is None):
                print("Sorry, but your cart does not contain the item")

            else:
                shoppingList.remove(itemToDel)
                print("The item has been deleted")
            
        elif(userInput == "3"):
            print()
            printList(shoppingList)
             
        elif(userInput == "4"):
            print()
            userSearch = input('Please enter the name of the item to find in your cart: ')
            
            search(shoppingList, userSearch)
            

        elif(userInput == "5"):
            countItems(shoppingList)
                

        elif(userInput == "6"):
            totalCost(shoppingList)

        elif(userInput == "7"):
            isListEmpty(shoppingList)

        elif(userInput == "8"):
            shoppingList =[]
            print("The list is now empty")
            
        else:
            print()
            print("Please enter a valid chocie")
            
            
        print()
        print("1. Add an item to the list")
        print("2. Delete an item from the list")
        print("3. Print each item in the list")
        print("4. Search for a user-specified item in the list")
        print("5. Count the total number of items in the list")
        print("6. Total the cost of the items in the list")
        print("7. Determine whether the list is empty")
        print("8. Clear the list")
        print("0. Quit")
        print()
        
        userInput = input("Enter an input: ")


        
    print()
    print("THANK YOU")
    theFile.close()
    
main()
