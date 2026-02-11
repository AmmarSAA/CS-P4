#q1
#a
DataStored = [''] * 20 #ARRAY [0:19]
NumberItems = 0 # integer variable is defined
#b
def Initialise():
    global DataStored
    global NumberItems
    NumberItems = int(input("how many numbers would you like to input? "))
    while NumberItems < 1 or NumberItems > 20:
        NumberItems = int(input("how many numbers would you like to input? "))
    for x in range(NumberItems):
        DataStored[x] = int(input("Write the number to insert in array "))

#d(i)
def BubbleSort():
    global DataStored
    global NumberItems
    for t in range(NumberItems):
        for x in range(NumberItems-1):
            if DataStored[x] > DataStored[x+1]:
                temp = DataStored[x]
                DataStored[x] = DataStored[x+1]
                DataStored[x+1] = temp

#e(i)

def BinarySearch(DataToFind):
    global DataStored
    global NumberItems
    ub = NumberItems
    lb = 0
    midp = int((lb+ub)/2)
    found = False
    while not found and lb <= ub:

        if DataStored[midp] == DataToFind:
            found = True
        if DataToFind < DataStored[midp]:
            ub = midp-1
        else:
            lb = midp+1
        midp = int((lb + ub) / 2)
    if found == True:
        return midp
    elif found == False:
        return -1


#e(ii)
#c(ii)
#d(ii)
def main():
    global DataStored
    global NumberItems
    NumberItems = 0
    Initialise()
    for x in range(20):
        print(DataStored[x] , end=" ")
    BubbleSort()
    print()
    for x in range(20):
        print(DataStored[x] , end=" ")
    DataToFind = int(input("Enter the number you would like to find: "))
    bs = BinarySearch(DataToFind)
    print(bs)
main()