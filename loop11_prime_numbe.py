num = int(input("Enter The Number : "))

if num<=0:
    print("Pleaze Enter Positive number Grether tHan 1")
elif num == 1:
    print("1 is neither prime nor composite")
elif num==2:
    print("2 is a Prime Number")
else:
    is_prime = True

    for i in range(2,num):
        if num%i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"The {num} Is is prime")
    else:
        print(f"The Number iS not Prime")
