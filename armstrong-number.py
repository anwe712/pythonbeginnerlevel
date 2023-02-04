import math
num = int(input("Please enter any number:"))
copy = num #saved a copy of the number so that it does not get destroyed
sum = 0
while (copy > 0):
    d = copy % 10
    sum = sum + (math.pow(d,3))
    copy = copy // 10
if (sum == num):
    print("This number is Armstrong Number")
else :
    print ("This number is not an Armstrong Number")   



