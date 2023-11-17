#catch all exceptions from the try block
try:
    x = int( input("Enter a number between 1-10") )
except:
    print("Invalid number!")

print("You enetered ", x)

#only catch divide by zero errors in te try block
try:
    y = 10/x

except ZeroDivisionError:
    print("invalid division")
    