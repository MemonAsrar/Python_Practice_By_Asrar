num = int(input("Enter a number: "))
i = 1
sum_div = 0

while i < num:
    if num % i == 0:
        sum_div += i
    i += 1

if sum_div == num:
    print(num, "is a Perfect Number")
else:
    print(num, "is NOT a Perfect Number")
