#Task 1
def addAll(args):
    total = 0.0
    for arg in args:
        total += float(arg)
    return total

def subtractAll(args):
    total = float(args[0])
    leftover_args = args[1:]
    for arg in leftover_args:
        total -= float(arg)
    return total

def multiplyAll(args):
    total = 1.0
    for arg in args:
        total = total * float(arg)
    return total

def divideAll(args):
    total = float(args[0])
    leftover_args = args[1:]
    for arg in leftover_args:
        total = total / float(arg)
    return total

#Task 2

def askOperation():
    print("What operation would you like to do?\n(1) Add\n(2) Subtract\n(3) Multiply\n(4) Divide")
    operation = input("Operation: ")
    return operation

def askNumbers():
    print("Please input numbers separated by spaces and/or commas below.")
    numbers = input("Numbers: ").replace(',', '').split(" ")
    for number in numbers:
        number.replace(' ', '')
        if number == "":
            numbers.remove(number)
    return numbers

#Task 3

def checkDivideByZero(numbers):
    for number in numbers:
        if len(number) == 1 and number == "0":
            return -1

#Program loop
def mainCalc():
    busy = 0
    while busy == 0:
        busy = 1
        operation = int(askOperation())
        numbers = askNumbers()
        result = 0
        
        if len(numbers) > 1:
            if operation == 1:
                print("Adding!" , numbers)
                result = addAll(numbers)
            elif operation == 2:
                print("Subtracting!", numbers)
                result = subtractAll(numbers)
            elif operation == 3:
                print("Multiplying!", numbers)
                result = multiplyAll(numbers)
            elif operation == 4:
                print("Dividing!", numbers)
                validate = checkDivideByZero(numbers)
                if validate == -1:
                    print("Division by 0 warning! Cancelled operation.")
                    result = "Try again!"
                else:
                    result = divideAll(numbers)
            else:
                print(operation, "is not a valid choice!")
                result = "Try again!"
            print(result)
            print("--------------------------------")
        else:
            print("You need to add more than one number!")
            print("--------------------------------")
        busy = 0


mainCalc()