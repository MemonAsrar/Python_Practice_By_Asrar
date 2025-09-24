cname = input("Enter Customer Name: ")
pname = input("Enter Product Name: ")
price = int(input("Enter Price: "))
qty = int(input("Enter Quantity: "))
gender = input("Enter Gender (M/F): ")

total = price * qty
dis = 0

if total >= 1500:
    dis = total * 15 / 100
elif total >= 1000:
    dis = total * 10 / 100
elif total >= 500:
    dis = total * 5 / 100
else:
    dis = 0

net = total - dis

print("----- Bill Summary -----")
print("Customer Name:", cname)
print("Product Name :", pname)
print("Price        :", price)
print("Quantity     :", qty)
print("Total        :", total)
print("Discount     :", dis)
print("Net Price    :", net)

if gender.lower() == "m":
    print("Thank you for shopping Mr.", cname, "Good Luck!")
else:
    print("Thank you for shopping Ms.", cname, "Good Luck!")
