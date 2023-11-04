class Node:
    def __init__(self,data="",pointer=-1):
        self.Pointer= pointer
        self.Data=str(data)

List = [Node("B",1),Node("D",2),Node("L",-1),Node("",4),Node("",5),Node("",-1)]
FreeListPtr = 3
NullPointer = -1
StartPointer = 0

def InsertNode(NewItem):
    global List, FreeListPtr, StartPointer 

    NewNodePtr = NullPointer
    ThisNodePointer = NullPointer
    
    PrevNodePointer = NullPointer

    if (FreeListPtr != NullPointer):
        NewNodePtr = FreeListPtr
        List[NewNodePtr].Data = NewItem
        FreeListPtr = List[FreeListPtr].Pointer

        ThisNodePointer = StartPointer
        #book errata
        #PrevNodePointer = StartPointer is not correct

        PrevNodePointer = NullPointer
        
        
        while((ThisNodePointer != NullPointer) and
                (List[ThisNodePointer].Data  < NewItem)):
                    
                    #remember this node
                    PrevNodePointer = ThisNodePointer

                    #follow the pointer to the next node
                    ThisNodePointer = List[ThisNodePointer].Pointer
        
        #book erata 
        #if (PrevNodePointer == StartPointer):
        if (PrevNodePointer == NullPointer):
                 #insert the node at the start of the list
                List[NewNodePtr].Pointer = StartPointer
                StartPointer = NewNodePtr
                 
        else:

            if(PrevNodePointer != NullPointer):
                List[NewNodePtr].Pointer = List[PrevNodePointer].Pointer
                List[PrevNodePointer].Pointer = NewNodePtr


def Student_InsertNode(NewItem):
    global List, FreeListPtr, StartPointer 

    NewNodePtr = NullPointer
    ThisNodePointer = NullPointer
    PrevNodePointer = NullPointer

    #your implementation
   

def DeleteNode(DataItem):
    global List, FreeListPtr, StartPointer 
    ThisNodePtr = StartPointer
    PreviousNodePtr = NullPointer

    while (ThisNodePtr != NullPointer and
            List[ThisNodePtr].Data != DataItem):
        
        PreviousNodePtr = ThisNodePtr
        ThisNodePtr = List[ThisNodePtr].Pointer
    
    if (ThisNodePtr != NullPointer):
        if(ThisNodePtr == StartPointer):
            StartPointer=List[StartPointer].Pointer
        else:
            List[PreviousNodePtr].Pointer = List[ThisNodePtr].Pointer
    
    List[ThisNodePtr].Pointer = FreeListPtr
    FreeListPtr = ThisNodePtr


def __PrintLinkedList(ListToPrint):
    #YOU DO NOT NEED TO UNDERSTAND THIS CODE FOR THE EXAM
    data = []
    for x in range(len(ListToPrint)):
        data.append([x, ListToPrint[x].Data,ListToPrint[x].Pointer])
     
    h=['Index','Data', 'Next']
    print( '{:<6s} {:<5s} {:<5s}'.format(*h) )

    for list_ in data:
        print( '{:<6d} {:<6s} {:<5d}'.format(*list_) )
    
    print("Start Pointer: " + str(StartPointer))
    print("FreeListPtr: " + str(FreeListPtr)+"\n")

__DefaultData = ["B","D","L"]

def __ResetList():
    global List,FreeListPtr, StartPointer 
    for x in range( len(__DefaultData)):
        List[x].Data = __DefaultData[x]
        List[x].Pointer = x + 1

    List[x].Pointer = NullPointer
    
    x = x + 1
    while x < len(List):
        List[x].Data = ""
        List[x].Pointer = x + 1
        x = x + 1

    List[len(List)-1].Pointer = -1
    FreeListPtr = len(__DefaultData)
    StartPointer = 0
def __CompareLinkedLists(List1, List2):
    Error=False

    for x in range(len(List1)):
        node1 = List1[x]
        node2 = List2[x]

        a = len(node1.Data)

        x  = bool((len(node1.Data) != 1) or (len(node2.Data)!=1))
        y = bool(node1.Data != node2.Data)
        z = bool((int(node1.Pointer) != int(node2.Pointer)))

        if((node1.Data != node2.Data) or
          (int(node1.Pointer) != int(node2.Pointer))):
            Error = True
            break
    return Error

ValidTestData = ["A","K"]

def __InsertNodeTest():
    global List

    __ResetList()


    for d in ValidTestData:
        InsertNode(d)

    print("\n****Testing Original List**** ")
    __PrintLinkedList(List)

    import copy
    ListCopy = copy.deepcopy(List)
    CopyStartPointer = StartPointer

    __ResetList()

    print("\n****Testing Student Tree**** ")
    for d in ValidTestData:
        Student_InsertNode(d)

    __PrintLinkedList(List)

    Error = False

    Error =  __CompareLinkedLists(ListCopy, List)

    if(CopyStartPointer != StartPointer):
        print("Error: Start Pointers Don't Match")
        Error = True

    __ResetList()

    if(Error == True):
        print("Student_InsertNode Test Failed, Lists do not match")
    else:
        print("Student_InsertNode Test Passed")

def __DeleteNodesTest():
    __ResetList()
    DeleteNode("L")
    __PrintLinkedList(List)


def Main():

    #for item in TestDataValid:
    #    InsertNode(item)

    #__InsertNodeTest()

    __DeleteNodesTest()

    #InsertNode("A")

    #print("original ")
    #__PrintLinkedList(List)

    #__ResetList()

    #print("Reset ")
    #__PrintLinkedList(List)

Main()
        
 