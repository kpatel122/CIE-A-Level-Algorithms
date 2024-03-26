#simple recursion
def rec(n):
    if(n>0):
        print("Enter recursion ", n) #general case
        rec(n-1)
    print("Exit recursion ", n) #base case


#simple recursion
def CountDown(n):
    print(n)#general case
    if(n>0): #Base case
       CountDown(n-1)
    print("end countdown n=" + str(n))

#recursion using return values
def Factorial(n):
    if  n==0 :
      result = 1
    else:
      result = n * Factorial(n-1)
    
    return result

CountDown(3)

#function call sequence
def C():
   print("Enter C")
   print("Exit C")
   
def B():
    print("Enter B")
    C()
    print("Exit B")

def A():
   print("Enter A")
   B()
   print("Exit A")