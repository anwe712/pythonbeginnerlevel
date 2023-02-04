import math
b = int (input("Enter the value of b: "))
a = int (input("Enter the value of a: "))
c = int (input("Enter the value of c: "))

solution1 = (-b + (math.pow(b,2)-2*a*c))
solution2 = (-b - (math.pow(b,2)-2*a*c))
final1 = solution1/ (2*a)
final2 = solution2/ (2*a)
print ("The roots of the quadratic equation are:",final1,"and", final2)