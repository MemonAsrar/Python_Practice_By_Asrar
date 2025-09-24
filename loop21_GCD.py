a = int(input("Enter The First Number : "))
b = int(input("Enter The Second Number : "))

while b != 0:
    a,b = b , a%b


print("GCD =", a)

