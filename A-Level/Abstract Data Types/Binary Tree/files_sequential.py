import pickle

class CarRecord: # declaring a class without other methods
 def __init__(self): # constructor
    self.VehicleID = "id"
    self.Registration = ""
    self.DateOfRegistration = None
    self.EngineSize = 0
    self.PurchasePrice = 0.00


#instantiate 100 car records
Car = [CarRecord() for i in range(100)]

CarFile = open('CarFile.DAT', 'wb') # open file for binary write

pickle.dump(Car, CarFile) # write a whole record to the binary file

CarFile.close() # close file


#read in the binary file
Car = [] # start with empty list
CarFile = open('CarFile.DAT', 'rb') # open file for binary read
Car = pickle.load(CarFile) # append record from file to end of list
CarFile.close()

#print all ids
for c in Car:
    print(c.VehicleID)
