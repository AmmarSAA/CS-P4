# a
class Queue:
    def __init__(self):
        self.QueueArray = []  # integer
        self.HeadPointer = -1  # integer
        self.TailPointer = 0  # integer
        for x in range(0, 100):
            self.QueueArray.append(-1)


TheQueue = ""


# c
def Enqueue(AQueue, TheData):
    if AQueue.HeadPointer == -1:
        AQueue.QueueArray[AQueue.TailPointer] = TheData
        AQueue.HeadPointer = 0
        AQueue.TailPointer += 1
        return 1
    else:
        if AQueue.TailPointer >= 100:
            return -1
        else:
            AQueue.QueueArray[AQueue.TailPointer] = TheData
            AQueue.TailPointer += 1
            return 1


# f
def Dequeue(AQueue):
    if AQueue.HeadPointer == -1:
        return -1
    else:
        DeValue = AQueue.QueueArray[AQueue.HeadPointer]
        AQueue.HeadPointer += 1
        return DeValue


# d
def ReturnAllData():
    global TheQueue
    data = ""
    for item in range(TheQueue.HeadPointer, TheQueue.TailPointer):
        data = str(data) + " " + str(TheQueue.QueueArray[item])

    return data


# b
def main():
    global TheQueue
    TheQueue = Queue()

    # e)i
    count = 0

    while count < 10:
        number = int(input("Please enter a number: "))
        if number < 0:
            print("The number is negative, please re enter")
            number = int(input("Please enter a number: "))
        if Enqueue(TheQueue, number) == -1:
            print("The queue is full")
            break
        else:
            print("The number has been added to the queue")
            count += 1

    if count >= 10:
        print(ReturnAllData())

    # g)i
    for i in range(2):
        DequeuedValue = Dequeue(TheQueue)
        if DequeuedValue == -1:
            print("The queue is empty")
        else:
            print("The value that has been dequeued is: " + str(DequeuedValue))
        # i += 1
    print(ReturnAllData())


main()
