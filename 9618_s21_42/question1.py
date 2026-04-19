# a
class node:
    def __init__(self, data, nextNode):
        self.data = data  # integer
        self.nextNode = nextNode  # integer


# b
linkedList = [node(-1, -1) for _ in range(0, 10)]
linkedList[0] = node(1, 1)
linkedList[1] = node(5, 4)
linkedList[2] = node(6, 7)
linkedList[3] = node(7, -1)
linkedList[4] = node(2, 2)
linkedList[5] = node(0, 6)
linkedList[6] = node(0, 8)
linkedList[7] = node(56, 3)
linkedList[8] = node(0, 9)
linkedList[9] = node(0, -1)


# c.i
def outputNodes(arr, startPointer):
    while startPointer != -1:
        print(arr[startPointer].data)
        startPointer = arr[startPointer].nextNode


# c.ii
outputNodes(linkedList, 0)


# d.i
def addNode(arr, startPointer, emptyList, data):
    if emptyList > len(arr):
        return False
    else:
        Found = False
        # # geting prev pointer
        while not Found:
            if startPointer != -1:
                prevPointer = startPointer
                startPointer = arr[startPointer].nextNode
                Found = False
            else:
                startPointer = prevPointer
                Found = True

        arr[startPointer].nextNode = emptyList
        arr[emptyList] = node(data, -1)
        emptyList = arr[emptyList].nextNode
        return True


# main
if addNode(linkedList, 0, 5, 5):
    print("Node Added Successfully!")
else:
    print("Failed to add node")
outputNodes(linkedList, 0)

# for i in range(0, 10):
#     print(linkedList[i].data)
