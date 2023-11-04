class Node:
    
    def __init__(self, leftValue=1,rightValue=-1):
        self.LeftPointer= leftValue
        self.RightPointer = rightValue
        self.Data=""

#instantiate an array of 6 nodes
Tree = [Node(),Node(),Node(),Node(),Node(),Node(-1,-1)]

FreePtr = 0 #the next available array element
RootPtr = -1 #the root of the tree
NullPointer = -1 #invalid pointer value

def InsertNode(NewItem):
    global Tree, FreePtr, RootPtr #the global variables we can change in the function

    #local variables
    TurnedLeft = False
    Turnedright = False
    PreviousNodePtr = RootPtr
    
    #check there is space in the tree
    if FreePtr != NullPointer:
        #set the new node to be the next available space
        NewNodePtr = FreePtr
        Tree[NewNodePtr].Data= NewItem
        
        #set the new nodes children to null
        Tree[NewNodePtr].LeftPointer = NullPointer
        Tree[NewNodePtr].RightPointer = NullPointer

        #errata from the book code.
        #move the free pointer to the next available array location
        FreePtr = FreePtr + 1

        #check if the array is full
        if(FreePtr == len(Tree)):
            FreePtr = NullPointer

        #is the tree empty
        if(RootPtr == NullPointer):
            RootPtr = NewNodePtr
        else:
            #traverse the list for the insertion point
            ThisNodePtr = RootPtr

            while (ThisNodePtr != NullPointer):
                
                #errata from the book
                #these flags must be reset each iteration
                TurnedLeft = False
                Turnedright = False

                #tack the new new node's parent
                PreviousNodePtr = ThisNodePtr

                #check which direction of the tree we should traverse
                if( ord(Tree[ThisNodePtr].Data) > ord(NewItem) ):
                    TurnedLeft = True
                    ThisNodePtr = Tree[ThisNodePtr].LeftPointer
                else:
                    TurnedRight = True
                    ThisNodePtr = Tree[ThisNodePtr].RightPointer
            
            #set the new node's parent to point to the new node 
            if(TurnedLeft == True):
                Tree[PreviousNodePtr].LeftPointer = NewNodePtr
            else:
                Tree[PreviousNodePtr].RightPointer = NewNodePtr


def FindNode(SearchItem):

    #start and the beginning of the tree
    ThisNodePtr = RootPtr
    
    Found = False

    #traverse the binary tree
    while ((ThisNodePtr != NullPointer) and
           (Tree[ThisNodePtr].Data != SearchItem)):

            #go left or right depending on the comparison of the node
            if(Tree[ThisNodePtr].Data > SearchItem):
                ThisNodePtr = Tree[ThisNodePtr].LeftPointer
            else:
                ThisNodePtr = Tree[ThisNodePtr].RightPointer
    
    #check if the search value was found
    if(Tree[ThisNodePtr].Data == SearchItem):
        Found = True
    
    return Found
    
        



#Your implementation of InsertNode
def Student_InsertNode(NewItem):
    
    #global variables
    global Tree, FreePtr, RootPtr #the global variables we can change in the function

    #local variables

    #Your implementation here

#Your implementation of FindNode
def Student_FindNode(SearchItem):
    Found = False
    
    #Your implementation here

    return Found



#use this method to print your tree
#YOU DO NOT NEED TO UNDERSTAND THIS CODE FOR THE EXAM
def __PrintTree(TreeToPrint):
    #YOU DO NOT NEED TO UNDERSTAND THIS CODE FOR THE EXAM
    data = []
    for x in range(len(TreeToPrint)):
        data.append([x, TreeToPrint[x].LeftPointer,TreeToPrint[x].Data,TreeToPrint[x].RightPointer])
     
    h=['Index', 'Left', 'Data', 'Right']
    print( '{:<6s} {:<5s} {:<5s} {:<5s}'.format(*h) )

    for list_ in data:
        print( '{:<6d} {:<6d} {:<5s} {:<5d}'.format(*list_) )
    #YOU DO NOT NEED TO UNDERSTAND THIS CODE FOR THE EXAM
#YOU DO NOT NEED TO UNDERSTAND THIS FUNCTION FOR THE EXAM
def __ResetTree():  
    #YOU DO NOT NEED TO UNDERSTAND THIS FUNCTION FOR THE EXAM
    
    #reset tree back to an empty tree
    global Tree, FreePtr, RootPtr
    FreePtr = 0
    RootPtr = NullPointer
    
    NodeCounter = 1
    for Node in Tree:
        Node.Data=""
        Node.LeftPointer = NodeCounter
        NodeCounter = NodeCounter + 1
        Node.RightPointer = NullPointer
    Tree[len(Tree)-1].LeftPointer = NullPointer

    #YOU DO NOT NEED TO UNDERSTAND THIS CODE FOR THE EXAM
#YOU DO NOT NEED TO UNDERSTAND THIS FUNCTION FOR THE EXAM
def __CompareTrees(Tree1, Tree2):
    Error=False

    for x in range(len(Tree1)):
        node1 = Tree1[x]
        node2 = Tree2[x]

        if( (len(node1.Data) != 1) or (len(node2.Data)!=1) or     
            (ord(node1.Data) != ord(node2.Data)) or
          (node1.LeftPointer != node2.LeftPointer) or
          (node1.RightPointer != node2.RightPointer)):
            Error = True
            break
    return Error
#YOU DO NOT NEED TO UNDERSTAND THIS FUNCTION FOR THE EXAM        
def __InsertNodeTest():
    #YOU DO NOT NEED TO UNDERSTAND THIS CODE FOR THE EXAM
    
    __ResetTree()
    for data in TestValidData:
        InsertNode(data)

    print("\n****Testing Original Tree**** ")
    __PrintTree(Tree)

    
    import copy
    TreeCopy = copy.deepcopy(Tree)

    __ResetTree()


    print("\n****Testing Student Tree**** ")
    for data in TestValidData:
        Student_InsertNode(data)

    __PrintTree(Tree)

    return __CompareTrees(TreeCopy, Tree)
    #YOU DO NOT NEED TO UNDERSTAND THIS CODE FOR THE EXAM

 #YOU DO NOT NEED TO UNDERSTAND THIS CODE FOR THE EXAM
#YOU DO NOT NEED TO UNDERSTAND THIS FUNCTION FOR THE EXAM
def __FoundTest():
    __ResetTree()
    
    for data in TestValidData:
        InsertNode(data)
    
    Error = False

    for data in TestValidData:
        if(Student_FindNode(data) == False):
            Error = True
            print("Find Node valid data not found: " + data)
            break
    
    for data in TestInvalidData:
        if(Student_FindNode(data) == True):
            Error = True
            print("Find Node invalid data was found: " + data)
            break
    
    return Error
#YOU DO NOT NEED TO UNDERSTAND THIS FUNCTION FOR THE EXAM
def __RunInsertTests():
    Error = __InsertNodeTest()
    if(Error == True):
        print("Student_InsertNode Test Failed, Trees do not match")
    else:
        print("Student_InsertNode Test Passed")
#YOU DO NOT NEED TO UNDERSTAND THIS FUNCTION FOR THE EXAM
def __RunFindTests():
    Error = __FoundTest()
    if(Error == True):
        print("Student_FindNode Test Failed")
    else:
        print("Student_FindNode Test Passed")

TestValidData = ["F","C","B","E","D","S"]
TestInvalidData = ["Z","G","A","L","K","P"]

def Main():

    for data in TestValidData:
        InsertNode(data)

    __PrintTree(Tree)


    #Test Harness

    #Run test to check your Student_InsertNode function:
    #__RunInsertTests()

    #Run test to check your Student_FindNode function:
    #__RunFindTests()

Main()
