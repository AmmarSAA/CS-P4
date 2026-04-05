# a
QueueData = [None] * 20
QueueHead = -1
QueueTail = -1


# b
def Enqueue(data):
    global QueueData, QueueHead, QueueTail
    if QueueTail > 20:
        return False
    else:
        QueueTail += 1
        QueueData[QueueTail] = data
        return True


# c
def Dequeue():
    global QueueData, QueueHead, QueueTail
    if QueueHead == QueueTail:
        return "false"
    else:
        QueueHead += 1
        return QueueData[QueueHead]
    
# d)i
def StoreItems(items):
    for i in range(10):
        while i > 11:
            sampleData = int(input("Enter 7 digit long character: "))
            if len(sampleData) == 7:
                Enqueue(sampleData)
                i += 1
