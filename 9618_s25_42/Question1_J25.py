# 1:a:

# TopOfStack is a global variable initialised to –1
TopOfStack = -1
# Stack is a global array of strings with all elements initialised to "-1"
Stack = [-1] * 20


# b:


# Push() takes a string parameter and attempts to store it on the stack
def Push(data):
    global Stack, TopOfStack
    # returns –1 if the stack is full
    if TopOfStack >= 20:
        return -1
    #  returns 1 if the parameter is successfully pushed onto the stack
    else:
        TopOfStack += 1
        Stack[TopOfStack] = data
        return 1


# c:


# Pop() returns the next item from the stack
def Pop():
    global Stack, TopOfStack
    # returns "–1" if the stack is empty
    if TopOfStack == -1:
        return -1
    else:
        returnVal = Stack[TopOfStack]
        TopOfStack -= 1
        return returnVal


# d:


def ReadData(fileName):
    global Stack, TopOfStack
    try:
        file = open(fileName, "r")
        wholeFile = file.read().splitlines()
        for line in wholeFile:
            # print(line)
            success = Push(line)
            if success == -1:
                print("Stack full!")
    except Exception as e:
        print(f"Error: {e}")


# e:


def Calculate():
    data = 0
    total = int(Pop())
    num2 = 0
    operators = ["+", "-", "*", "/", "^"]
    while data != -1:
        data = Pop()
        if data == -1:
            break

        if data in operators:
            operator = data
        else:
            num2 = int(data)

            # Actual calcualtion

            if operator == "+":
                total += num2
            elif operator == "-":
                total -= num2
            elif operator == "*":
                total *= num2
            elif operator == "/":
                total /= num2
            elif operator == "^":
                total **= num2

    return total


# f.i.
def main():
    fileName = input("Please enter file name: ")
    ReadData(f"F:/Data/CS-P4/9618_s25_42/9618_s25_sf_42/{fileName}")
    print(Calculate())


main()
