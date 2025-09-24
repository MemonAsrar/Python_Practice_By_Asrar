num = int(input("Enter a number: "))
temp = num
rev = 0

while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10

if num == rev:
    print(num, "is a Palindrome")
else:
    print(num, "is NOT a Palindrome")
