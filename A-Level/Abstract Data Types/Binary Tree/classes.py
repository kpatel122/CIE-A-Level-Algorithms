class Person: #class definition

    def __init__(self): #class constructor
        
 
        self.__Surname = "P" #private attributes are shown with an underscore
        self.__FirstName = "A"
        self.__DateOfBirth = ""
        self.__Job = ""
        print(" Person Constructor ")
    
 
    def GetFirstName(self): #class methods belong to the class
        return self.__FirstName

    def SetFirstName(self, newFirstName): #setter of the private variable
            self.__FirstName = newFirstName

    def GetDetails(self): #methods
        print("First name " + self.__FirstName )
        print("Second name " + self.__Surname )

PersonA = Person() #instantiation
PersonA.__FirstName = "" #PersonA is an instance
PersonA.GetDetails() #call the person method
