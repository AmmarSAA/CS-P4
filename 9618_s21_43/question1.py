#a
class node:
    def __init__(self, data, nextNode):
        self.data = data # Integer
        self.nextNode = nextNode # Integer

#b
linkedList = []
linkedList.append(node(1,1))
linkedList.append(node(5,4))
linkedList.append(node(6,7))
linkedList.append(node(7,-1))
linkedList.append(node(2,2))
linkedList.append(node(0,6))
linkedList.append(node(0,8))
linkedList.append(node(56,3))
linkedList.append(node(0,9))
linkedList.append(node(0,-1))

#c.i
def outputNodes(linkedList, startPointer):
    while startPointer != -1:
        print(linkedList[startPointer].data)
        startPointer = linkedList[startPointer].nextNode

#d.i
def addNode(linkedList, emptyList, startPointer):
    data = int(input("Enter the integer to include in linked list: "))

    if startPointer < len(linkedList):
        linkedList[emptyList].data = data

        while startPointer != -1:
            prevPointer = startPointer
            startPointer = linkedList[startPointer].nextNode

        linkedList[prevPointer].nextNode = emptyList
        linkedList[emptyList].nextNode = -1
        emptyList = linkedList[emptyList].nextNode
        return True
    else:
        return False

#c.ii
#d.ii
#main
startPointer = 0
emptyList = 5
outputNodes(linkedList, startPointer)
if addNode(linkedList, emptyList, startPointer):
    print("Node added successfully!")
else:
    print("List is full!")
outputNodes(linkedList, startPointer)

