# a
class Queue:
    def __init__(self):
        self.QueueArray = [] # integer
        self.HeadPointer = 0 # integer
        self.TailPointer = 0 # integer
        for x in range(0, 100):
            self.QueueArray.append(-1)
TheQueue = ""
# c
def Enqueue(AQueue, TheData):
    if AQueue.HeadPointer == -1:
        AQueue.QueueArray[AQueue.TailPointer] = TheData
        AQueue.HeadPointer = 0
        AQueue.TailPointer +=1
        return 1
    else:
        if AQueue.AQueue.TailPointer >= 100:
            return -1
        else:
            AQueue.QueueArray[AQueue.TailPointer] = TheData
            AQueue.TailPointer += 1
            return 1

# d
def ReturnAllData():
    global TheQueue
    data = ""
    for item in range(TheQueue.HeadPointer(),TheQueue.TailPointer()):
        data = tmp + str(TheQueue.QueueArray[item]) + ""

    return data

# b
def main():
    global TheQueue
    TheQueue = Queue()

    #e)i
    number = int(input("Please enter a number: "))
    while number >0:
        


main()
