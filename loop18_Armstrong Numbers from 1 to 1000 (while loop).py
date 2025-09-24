num = 1
print("Armstrong numbers from 1 to 1000 are:")

while num <= 1000:
    digits = len(str(num))
    temp = num
    sum_pow = 0

    while temp > 0:
        d = temp % 10
        sum_pow += d ** digits
        temp //= 10

    if sum_pow == num:
        print(num, end=" ")
    num += 1
