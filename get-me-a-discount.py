price = int(input("Enter the price of the item:"))
discount = int(input("Enter the discount percentage:"))
final_price = price - (discount* 0.01 * price)
print("The price of the item after the discount=",final_price)