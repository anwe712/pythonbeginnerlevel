#addition of two numbers using function
def add(a,b): #this is a function in which two numbers are there in the parameter
    return (a+b) # this will return the summation of a and b

c = int(input("Enter a value here:"))
d =int(input("Enter a value here:"))
summation = add(c,d)
print("THe summation of two number using function=",summation)
