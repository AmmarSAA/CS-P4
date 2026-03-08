# a. declare and initialise Queue, HeadPointer and TailPointer
Queue = []
HeadPointer = -1
TailPointer = -1
Queue = [-1] * 50
Size = 0

# b. Enqueue()
def Enqueue(item):
    global Queue, HeadPointer, TailPointer
    Size = 0
    
    # Queue is empty insert data
    if HeadPointer == -1 and TailPointer == -1:
        HeadPointer = 0
        TailPointer = 0
        Size += 1
        Queue[TailPointer] = item
        return True
    
    # Queue is full
    if TailPointer >= 50:
        return False
    else:
        # Queue is not full 
        TailPointer += 1
        Queue[TailPointer] = item
        Size += 1
        return True
    
# c. Dequeue()
def Dequeue():
    
    global Queue, HeadPointer, TailPointer, Size
    
    # Queue is empty return -1
    if HeadPointer == -1 and TailPointer == -1:
        returnVal = -1
    
    # Queue has data so return the value
    if TailPointer >= 0 or HeadPointer >= 0:
        returnVal = Queue[TailPointer]
        TailPointer -= 1
        Size -= 1
        
    return returnVal

# e.i. CreateQueue()
def CreateQueue():
    sum = Dequeue()