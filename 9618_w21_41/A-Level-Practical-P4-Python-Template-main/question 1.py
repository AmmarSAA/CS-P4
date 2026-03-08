
# Write program code to declare the function Unknown().

def Unknown(x, y):
    if (x < y):
        print(x + y)
        return (Unknown(x + 1, y) * 2)
    elif (x == y):
        return 1
    else:
        print(x + y)
        return (Unknown(x - 1, y) // 2)


# The main program needs to run all three of the following function calls and output the result of each call:

def main():

    print("---recursive---")
    print("----------------")
    print(f"x: 10, y: 15")
    print(Unknown(10, 15))
    print("----------------")
    print(f"x: 10, y: 10")
    print(Unknown(10, 10))
    print("----------------")
    print(f"x: 15, y: 10")
    print(Unknown(15, 10))
    print("----------------")

    print("---iterative---")
    print("----------------")
    print(f"x: 10, y: 15")
    print(IterativeUnknown(10, 15))
    print("----------------")
    print(f"x: 10, y: 10")
    print(IterativeUnknown(10, 10))
    print("----------------")
    print(f"x: 15, y: 10")
    print(IterativeUnknown(15, 10))
    print("----------------")


# Rewrite the function Unknown() as an iterative function, IterativeUnknown()

def IterativeUnknown(x, y):
    Sum = 1
    while (x == y):
        return 1

    while (x != y):
        if (x > y):
            print(x + y)
            x -= 1
            Sum //= 2
        else:
            print(x + y)
            x += 1
            Sum *= 2

    return Sum


main()
