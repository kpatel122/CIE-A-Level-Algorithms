class A: #class definition 
    def __init__(self): #constructor
        print("Constructor for A")
        self.__a_variable = "Hello " #class attributes
    def get_details(self): #class method
        print("the value of a is " + self.__a_variable)

    def get_a(self): #getter
            return self.__a_variable
    def set_a(self,aValue): #setter
            self.__a_variable = aValue

class B(A): #class B inherits all attributes and methods from class A 
    def __init__(self): #constructor
        super.__init__(self) #call the parent constructor(must always be called)
        print("Constructor for B")
        self.__b_variable = "World" #class variable/attributes
    
    def print_message(self): #class methods
        print(self.get_a() + self.__b_variable) #inherited class has access to base class attributes/methods









class Animal: #base/parent class
    def __init__(self,name): #class constructor
        print("Animal constructor called")
        self.__name=name
        self.__type="mammal"

    def get_type(self):
        return self.__type
    
    def set_type(self, new_type):
        self.__type = new_type

    def get_name(self): #getter
        return self.__name #all class attributes have getters and setters
    
    def set_name(self, name): #setter
        self.__name = name #all class attributes have getters and setters
    
    def make_sound(self): #class method
        print("Animal makes a sound")
        
class Dog(Animal): #sub/child class inherits call class attributes and methods from parent
    def __init__(self,name):
        super().__init__(name) #call the base/parent constructor, must provide all params parent 
                               #constructor expects
    def make_sound(self): #polymorphism override the parent class method
        print("whoof whoof")

    def print_type(self):
        print(super().get_type())
 


d = Dog("spot")


#print(d.get_name())

d.print_type()
#d.make_sound()











class Vehicle: #base/parent class
    def __init__(self):
        self.__numberOfWheels = 0 #class attributes
        self.__numberOfSeats = 0
    
    def Move(self): #class methods
        print("Vehicle is moving")
    
    def get_numberOfWheels(self): #getters
        return self.__numberOfWheels

    def get_numberOfSeats(self): 
        return self.__numberOfSeats
    
    def set_numberOfWheels(self, numberOfWheels):#setters
        self.__numberOfWheels = numberOfWheels
    
    def set_numberOfSeats(self, numberOfSeats):
        self.__numberOfSeats = numberOfSeats
    
class Car(Vehicle): #child class is a specialist version of the parent class
    def __init__(self):
        super().__init__() #call the parent constructor
        self.__model = ""

    def GetDetails(self): #class method
        print("Model " + self.__model)

    def Move(self): #class method
        print("Car is moving ")

#mazda = Car() #instantiation- variable mazda is an instance of the car class

#mazda.Move()
#mazda.set_numberOfSeats(4)
#print("Seats are ", mazda.get_numberOfSeats())
