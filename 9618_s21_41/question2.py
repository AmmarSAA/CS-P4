# a.
arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]


# b.i.
def linearSearch(search):
    global arrayData
    found = False
    size = len(arrayData) - 1

    for i in range(size):
        if arrayData[i] == search:
            found = True

    # If not found, returns False
    return found


# c.
def bubbleSort():
    global arrayData
    size = len(arrayData)
    for x in range(size):
        for y in range(0, size):
            if arrayData[y] > arrayData[y + 1]:
                # swapping
                temp = arrayData[y]
                arrayData[y] = arrayData[y + 1]
                arrayData[y + 1] = temp


# b.ii
def main():

    search = int(input("Enter a number to search: "))

    if linearSearch(search):
        print(f"{search} is present in the list")
    else:
        print(f"{search} is not present in the list")


main()
