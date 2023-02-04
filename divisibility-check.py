num1 = int(input("Enter any number:"))
num2 =int(input("Enter any number:"))
if (num1 % num2 == 0):
    print (num1,"is divisible by", num2)
elif (num2 % num1 == 0):
    print (num2 ,"is divisible by",num1)   
else:
    print("They are not divisible by one another")    