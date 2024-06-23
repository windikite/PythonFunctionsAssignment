#Task 1
def addToList(list, item):
    new_list = []
    new_list.extend(list)
    new_list.append(item)
    print("Added" , item)
    return new_list

#Task 2
def removeFromList(list, item):
    new_list = []
    new_list.extend(list)
    if item in new_list:
        new_list.remove(item)
        print("removed", item)
    else:
        print("Item not on list!")
    return new_list

#Task 3
def printList(list):
    new_list = []
    new_list.extend(list)
    new_list.sort()
    counter = 1
    for item in new_list:
        print("Item", counter, ": ", item)
        counter += 1

def askOperation():
    print("What operation would you like to do?\n(1) Add\n(2) Remove\n(3) Quit")
    operation = input("Operation: ")
    return operation

def askItem():
    print("Please input item below.")
    items = input("Item: ")
    return items

def mainLoop():
    list = []
    busy = 0
    while busy == 0:
        busy = 1
        operation = int(askOperation())
        item = askItem()
        if operation == 1:   
            list = addToList(list, item)
        elif operation == 2:
            list = removeFromList(list, item)
        elif operation == 3:
            print("Quitting!")
            busy = 2
            break
        else:
            print(operation, "is not a valid choice!")
            print("Try again!")
        printList(list)
        print("--------------------------------")
        busy = 0
    
mainLoop()
