# a:
class NewRecord:
    def __init__(self, key, item1, item2):
        self.key = key
        self.item1 = item1
        self.item2 = item2


# b:i:
# Write program code to declare the global arrays HashTable and Spare
HashTable = [NewRecord] * 200
Spare = [NewRecord] * 100


# b:ii:
# procedure Initialise() stores an empty record in each element in HashTable and Spare
def Initialise():
    global HashTable, Spare
    # HashTable = [NewRecord(-1, -1, -1)] * 200
    # Spare = [NewRecord(-1, -1, -1)] * 100
    for i in range(100):
        Spare[i] = NewRecord(-1, -1, -1)
    for i in range(200):
        HashTable[i] = NewRecord(-1, -1, -1)


# c:
def CalculateHash(HashKey):
    HashValue = HashKey % 200
    return HashValue


# d:
def InsertIntoHash(Record):
    global HashTable, Spare
    # print(NewRecord.key)
    key = CalculateHash(Record.key)
    if HashTable[key].key == -1:
        HashTable[key] = Record
    else:
        Spare.append(Record)


# e:
def CreateHashTable():
    Record = NewRecord(-1, -1, -1)
    with open("F:\\Data\\CS-P4\\9618_s25_42\\9618_s25_sf_42\\HashData.txt", "r") as f:
        wholeFile = f.read().splitlines()
        # print("Key\tItem1\tItem2")
        for line in wholeFile:
            rawRecord = line.split(",")
            key = int(rawRecord[0])
            item1 = int(rawRecord[1])
            item2 = int(rawRecord[2])

            Record = NewRecord(key, item1, item2)
            # print(f"{Record.key}\t{Record.item1}\t{Record.item2}")
            InsertIntoHash(Record)


# f:i:
def PrintSpare():
    global Spare
    if Spare.key != -1:
        print(Spare.key)


# f:ii:
def main():
    Initialise()
    CreateHashTable()
    PrintSpare()


main()
