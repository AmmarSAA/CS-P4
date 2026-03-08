# a.
class node:
    def __init__(self, data, next_node):
        self.data = data
        self.nextNode = next_node


# b.
startPointer = 0
emptyList = 5
linkedList = [
    node(1, 1),
    node(5, 4),
    node(6, 7),
    node(7, -1),
    node(2, 2),
    node(0, 6),
    node(0, 8),
    node(56, 3),
    node(0, 9),
    node(0, -1),
]


# c.i.
def outputNodes(linkedList, startPointer):
    print(f"Outputting Nodes from {startPointer}")

    while startPointer != -1:
        print(linkedList[startPointer].data)
        startPointer = linkedList[startPointer].nextNode


# d.i.
def addNode(linkedList, startPointer, emptyList):
    success = False
    data = int(input("Enter data to add: "))

    # Getting end of the list:
    while startPointer != -1:
        prevPointer = startPointer
        startPointer = linkedList[startPointer].nextNode

    while linkedList[emptyList].nextNode != -1:
        # New Node:
        linkedList[emptyList].data = data
        linkedList[emptyList].nextNode = -1

        # updating to join th new Node in linked list
        linkedList[prevPointer].nextNode = emptyList

        # Empty List updating
        emptyList = linkedList[emptyList].nextNode
        success = True

        # Return true if inserted successfully
        return success

    # List is full as no space in emptyList
    return success


# c.ii.
# d.ii
def main():
    outputNodes(linkedList, startPointer)
    if addNode(linkedList, startPointer, emptyList):
        print("Successfully added node")
    else:
        print("No space left to add node")
    outputNodes(linkedList, startPointer)


main()
