Num1 = int(input("Enter First Number : "))
Num2 = int(input("Enter Second Number : "))

if Num1>Num2:
    print(f"{Num1} is Maximum")
elif Num1<Num2:
    print(f"{Num2} is Maximum")
elif(Num1 == Num2):
    print(f"{Num1} and {Num2} are Same")
else:
    print("Enter The correct Number")

if Num1%2 == 0:
    print("The Number is Even")
else:
    print("The Number is odd")

if Num1 >= 0:
    print(f"The {Num1} Is Positive")
else:
    print(f"The {Num1} is Negative")
