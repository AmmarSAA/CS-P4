# a: Write program code to declare and initialise Queue, HeadPointer, TailPointer and NumberItems

HeadPointer = -1
TailPointer = -1
NumberItems = 0
Queue = [-1]*20


# b: function Enqueue()
# takes an integer as a parameter
def Enqueue(data):
    global HeadPointer, TailPointer, NumberItems, Queue
    # checks if the queue is full
    if NumberItems >= 20:
        # returns FALSE if the queue is full
        return False
    # stores the parameter in the next position in the queue and returns TRUE if the queue is not full
    else:
        # updates the appropriate pointers and NumberItems
        NumberItems += 1
        if HeadPointer < 0 and TailPointer < 0:
            HeadPointer += 1
            TailPointer += 1
            Queue[TailPointer] = data
        else:
            TailPointer += 1
            Queue[TailPointer] = data
        return True



# d: function Dequeue()

def Dequeue():
    global NumberItems, HeadPointer, TailPointer, Queue
    # returns –1 if the queue is empty
    if NumberItems <= 0:
        return -1
    else:
        # updates the appropriate pointers and updates NumberItems
        returnVal= Queue[HeadPointer]
        HeadPointer += 1
        if HeadPointer >= 20:
            HeadPointer = 0
        NumberItems-=1
        if NumberItems <=0:
            HeadPointer = -1
            TailPointer = -1
        # returns the next item in the queue
        return returnVal


# c: The main program

def main():
    # attempts to store each of the integers 1 to 25 (inclusive)
    for i in range(1,26):
        result = Enqueue(i)
        # "Successful" if it was stored
        if result:
            result = "Successful"
            print(f"{i} {result}")
        # "Unsuccessful" if it was not stored
        else:
            result = "Unsuccessful"
            print(f"{i} {result}")
            
    #e:i: call Dequeue() twice and output the return value each time
    
    print(Dequeue())
    print(Dequeue())
    
main()