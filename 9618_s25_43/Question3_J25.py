# a.i
class Node:
    # Private TheData: Integer
    # Private NextNode: Node
    def __init__(self, pTheData):
        self.__TheData = pTheData  # Integer
        self.__NextNode = None  # Node

    # a.ii
    def GetData(self):
        return self.__TheData

    def GetNextNode(self):
        return self.__NextNode

    # a.iii
    def SetNextNode(self, pNode):
        self.__NextNode = pNode


# b.i
class LinkedList:
    # Private HeadNode: Node
    def __init__(self):
        self.__HeadNode = None  # Node

    # b.ii
    def InsertNode(self, pNodeData):
        newNode = Node(pNodeData)
        newNode.SetNextNode(self.__HeadNode)
        self.__HeadNode = newNode

    # b.iii
    def Traverse(self):
        NodeData = ""
        currentNode = self.__HeadNode
        while currentNode != None:
            NodeData += f" {currentNode.GetData()}"
            currentNode = currentNode.GetNextNode()
        return NodeData

    # b.iv
    def RemoveNode(self, remove):
        currentNode = self.__HeadNode
        prevPointer = None
        nextPointer = self.__HeadNode.GetNextNode
        found = False

        # Check if list is empty and return false
        if currentNode == None:
            return False
        else:
            while currentNode != None and not found:
                if currentNode.GetData() == remove:
                    found = True
                    nextPointer = currentNode.GetNextNode()

                else:
                    prevPointer = currentNode.GetNextNode()
                    currentNode = currentNode.GetNextNode()
                    found = False
                    return False
            
            if found:
                prevPointer.SetNexNode()


def main():
    print("Hello World!")


main()
