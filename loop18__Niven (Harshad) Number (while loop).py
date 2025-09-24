num = int(input("Enter The Number : "))

temp = num
digi_sum = 0

while temp >0:
    digi_sum = digi_sum + (temp%10)
    temp = temp //10

if num%digi_sum == 0:
    print(f"{num} Is Naivan Number")
else:
    print(f"{num} Is Not Naivan Number")

