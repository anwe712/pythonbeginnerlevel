num = int(input("Enter any number for which you want to get the factorial: "))
fact = 1

for i in range(1,num+1,1):
    fact = fact * i
print("THe factorial of the number=",fact)    