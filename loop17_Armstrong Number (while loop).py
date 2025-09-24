num = int(input("Enter a number: "))
digits = len(str(num))
temp = num
sum_pow = 0

while temp > 0:
    d = temp % 10
    sum_pow += d ** digits
    temp //= 10

if sum_pow == num:
    print(num, "is an Armstrong Number")
else:
    print(num, "is NOT an Armstrong Number")
