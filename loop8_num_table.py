num = int(input("Enter The Number : "))
sum = 0
for i in range(1,num):
    if num%i ==0:
        sum = sum+i

if num == sum:
    print(f"The {num} Number is Perfact Number")
else:
    print(f"The {num} Number is Not Perfact Number")