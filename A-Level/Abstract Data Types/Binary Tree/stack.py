EMPTYSTRING = ""
NullPointer = -1
MaxStackSize = 8
BaseOfStackPointer = 0
TopOfStackPointer = 0
Stack = ["","","","","","","",""]

def InitStack():
    global BaseOfStackPointer, TopOfStackPointer
    BaseOfStackPointer = 0
    TopOfStackPointer = NullPointer

def Push(NewItem):
    global TopOfStackPointer, Stack
    if(TopOfStackPointer < MaxStackSize-1):
        TopOfStackPointer = TopOfStackPointer + 1
        Stack[TopOfStackPointer] = NewItem

def Pop():
    global TopOfStackPointer
    Item = ""
    if( TopOfStackPointer > NullPointer):
        Item = Stack[TopOfStackPointer]
        TopOfStackPointer = TopOfStackPointer - 1
    return Item

def __PrintStack():

    #YOU DO NOT NEED TO UNDERSTAND THIS CODE FOR THE EXAM
    data = []
    for x in range(0, TopOfStackPointer+1): #len(Stack)):
        data.append([x, Stack[x]])
     

    h=['Index','Data']
    print( '{:<6s} {:<5s}'.format(*h) )

    for list_ in data:
        print( '{:<6d} {:<6s}'.format(*list_) )
    
    print("Top of Stack: " + str(TopOfStackPointer))

def Main():
    
    InitStack()

    Push("10")
    Push("20")
    Pop()
    Push("30")

    __PrintStack()

Main()
