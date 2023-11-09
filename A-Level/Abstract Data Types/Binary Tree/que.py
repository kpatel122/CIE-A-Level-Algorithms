EMPTYSTRING = ""
NullPointer = -1
MaxQueSize = 8

FrontOfQuePointer=0
EndOfQuePointer=0
NumberInQue=0
Que = ["","","","","","","",""]

def InitialiseQue():
    global Que, FrontOfQuePointer, EndOfQuePointer,NumberInQue
    #Errata from the book
    #FrontOfQuePointer = NullPointer
    FrontOfQuePointer = 0 
    EndOfQuePointer = NullPointer
    NumberInQue = 0

def AddToQue(NewItem):
    global NumberInQue, EndOfQuePointer
    if NumberInQue < MaxQueSize:
        EndOfQuePointer = EndOfQuePointer + 1
        if EndOfQuePointer > MaxQueSize-1:
            EndOfQuePointer = 0
        
        Que[EndOfQuePointer] = NewItem
        NumberInQue = NumberInQue + 1

def RemoveFromQue():
    Item = EMPTYSTRING
    global NumberInQue, FrontOfQuePointer
    if( NumberInQue > 0):
        Item = Que[FrontOfQuePointer]
        NumberInQue = NumberInQue - 1

        if(NumberInQue == 0):
            InitialiseQue()
        else:
            FrontOfQuePointer = FrontOfQuePointer + 1
            FrontOfQuePointer > MaxQueSize - 1
            if(FrontOfQuePointer > MaxQueSize-1):
                FrontOfQuePointer = 0
        
    return Item

def __PrintQue(QueToPrint = Que):
    #YOU DO NOT NEED TO UNDERSTAND THIS CODE FOR THE EXAM
    data = []
    for x in range(0, len(QueToPrint)):
        data.append([x, QueToPrint[x]])
     
    h=['Index','Data']
    print( '{:<6s} {:<5s}'.format(*h) )

    for list_ in data:
        print( '{:<6d} {:<6s}'.format(*list_) )
    
    print("FrontOfQuePointer: " + str(FrontOfQuePointer))
    print("EndOfQuePointer: " + str(EndOfQuePointer))

def Main():
    InitialiseQue()
    AddToQue("K")
    AddToQue("J")
    AddToQue("T")
    AddToQue("A")
    AddToQue("A")
    AddToQue("K")
    AddToQue("N")
    AddToQue("C")

    x = RemoveFromQue()
    print("X is " + x)

    y = RemoveFromQue()
    print("y is " + y)

    z = RemoveFromQue()
    print("z is " + z)

    AddToQue("Testerson")
    AddToQue("Testerson1")
    AddToQue("Testerson2")

    __PrintQue()


Main()
