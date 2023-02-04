c = 0
num = int(input("Enter a number: "))
d=num % 10
num = num // 10
c = (d*10) + num
print("The reversed number:",c)
