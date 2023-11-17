try:
    x = int( input("Enter a number between 1-10") )
except:
    print("invalid input")


try:
    y = 10/x
except ZeroDivisionError:
    print("Invalid division")



#y = 10/x

#print(y)



