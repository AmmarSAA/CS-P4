nullPointer = "-1"


# a.i
class Node:
    def __init__(self, pNodeData):
        global nullPointer
        self.__NodeData = pNodeData  # Integer
        self.__LeftNode = nullPointer  # Node
        self.__RightNode = nullPointer  # Node

    # a.ii
    def getLeft(self):
        return self.__LeftNode

    def getRigt(self):
        return self.__RightNode

    def getData(self):
        return self.__NodeData

    # a.iii
    def setLeft(self, pLeftNode):
        self.__LeftNode = pLeftNode

    def setRigt(self, pRightNode):
        self.__RightNode = pRightNode


# c.i
class Tree:
    def __init__(self, pFirstNode):
        self.__FirstNode = pFirstNode  # Node

    # c.ii
    def GetRootNode(self):
        return self.__FirstNode

    # c.iii
    def Insert(self, pnode):
        if pnode < self.__FirstNode.getData() {
            self.getLeft =
        }
    
    
    
    # def Insert(self, pnode):
    #     found = False
    #     while not found:
    #         if pnode.getData() < self.__FirstNode.getData():
    #             goLeft = True
    #         elif pnode > self.__FirstNode:
    #             goLeft = False
    #         else:
    #             found = True

    #     if goLeft:
    #         Node.setLeft(pnode)
    #     else:
    #         Node.setRight(pnode)
    
    # def Insert(self, NewNode):  
    #     CurrentNode = self.__FirstNode  
    #     Inserted = True 
    #     while Inserted: 
    #         if NewNode.getData() < CurrentNode.getData():  
    #             if CurrentNode.getLeft() == "-1": 
    #                 CurrentNode.setLeft(NewNode)  
    #                 return True 
    #             else: 
    #                 CurrentNode = CurrentNode.getLeft() 
    #         else: 
    #             if CurrentNode.getRight() == "-1":  
    #                 CurrentNode.setRight(NewNode)  
    #                 return True 
    #             else: 
    #                 CurrentNode = CurrentNode.getRight() 


# d
def OutputInOrder(pnode):

    complete = False
    while not complete:
        if Node.getLeft != -1:
            print(Node.getData())
            complete = False
            OutputInOrder()
        elif Node.getRigt != -1:
            print(Node.getData())
            complete = False
            OutputInOrder()
        else:
            complete = True
            return complete


def main():

    # b.
    Node_1 = Node(10)
    Node_2 = Node(20)
    Node_3 = Node(5)
    Node_4 = Node(15)
    Node_5 = Node(7)

    # e.i
    TreeObject = Tree(10)
    TreeObject.Insert(20)
    TreeObject.Insert(5)
    TreeObject.Insert(15)
    TreeObject.Insert(7)

    OutputInOrder(Tree.GetRootNode())


main()
