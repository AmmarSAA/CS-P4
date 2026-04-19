# a
# global array of datatype integer
arrayData = [-1 for _ in range(0, 10)]

# main
i = 0
arrayData[i] = 10
i += 1
arrayData[i] = 5
i += 1
arrayData[i] = 6
i += 1
arrayData[i] = 7
i += 1
arrayData[i] = 1
i += 1
arrayData[i] = 12
i += 1
arrayData[i] = 13
i += 1
arrayData[i] = 15
i += 1
arrayData[i] = 21
i += 1
arrayData[i] = 8

# print(arrayData)


# b.i.
def linearSearch(search):
    global arrayData
    Found = False
    while not Found:
        for data in arrayData:
            if data == search:
                Found = True
                break
            else:
                Found = False
    return Found


# main
search = int(input("Enter value to search: "))
if linearSearch(search):
    print(f"{search} found successfully!")
else:
    print(f"{search} not found!")


# c
def bubbleSort():
    global arrayData
    # temp : Integer
    for x in range(len(arrayData)):
        for y in range(len(arrayData) - 1):
            if arrayData[y] < arrayData[y + 1]:
                temp = arrayData[y]
                arrayData[y] = arrayData[y + 1]
                arrayData[y + 1] = temp


bubbleSort()
