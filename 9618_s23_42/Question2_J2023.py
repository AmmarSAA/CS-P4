# a
class SaleData:
    def __init__(self, id, quantity):
        self.id = id  # string
        self.quantity = quantity  # integer


# b
CircularQueue = [SaleData("", -1) for _ in range(0, 6)]
Head = 0
Tail = 0
NumberOfItems = 0


# c
def Enqueue(record):
    global CircularQueue, Head, Tail, NumberOfItems

    if NumberOfItems != len(CircularQueue):
        CircularQueue[Tail] = record
        Tail += 1
        NumberOfItems += 1
        return 1
    else:
        return -1


# d
def Dequeue():
    global CircularQueue, Head, Tail, NumberOfItems
    if NumberOfItems == 0:
        return SaleData("", -1)
    else:
        record = CircularQueue[Head]
        Head += 1
        NumberOfItems -= 1
        return record


# e
def EnterRecord():
    id = input("Please enter the ID: ")
    quantity = int(input("Please enter the quantity: "))
    record = Enqueue(SaleData(id, quantity))
    if record == 1:
        print("Stored")
    else:
        print("Full")


# f)i
EnterRecord()
EnterRecord()
EnterRecord()
EnterRecord()
EnterRecord()
if Dequeue() == SaleData("", -1):
    print("Empty")
else:
    print(Dequeue().id, Dequeue().quantity)
EnterRecord()
for i in range(NumberOfItems):
    print(CircularQueue[i].id, CircularQueue[i].quantity)

print(CircularQueue[0].quantity)
