import pickle # this library is required to create binary files

class CarRecord: # declaring a class without other methods
 def __init__(self): # constructor
    self.VehicleID = "0"
    self.Registration = ""
    self.DateOfRegistration = None
    self.EngineSize = 0
    self.PurchasePrice = 0.00


ThisCar = CarRecord()
ThisCar.VehicleID= "452"
ThisCar.Registration="HDE 4F5"

 

CarFile = open('CarFile.DAT','r+b') # open file for binary read and write
Address =abs(hash(ThisCar.VehicleID))
print(Address)
CarFile.seek(Address)
pickle.dump(ThisCar, CarFile) # write a whole record to the binary file
#CarFile.close() # close file

#CarFile = open('CarFile.DAT','rb') # open file for binary read
Address = abs(hash(ThisCar.VehicleID))
print("address 2 ", Address)

#print("Address ", Address)
#CarFile.seek(Address)
#SearchCar =  pickle.load(CarFile) # load record from file
#CarFile.close()

#print(SearchCar.Registration)