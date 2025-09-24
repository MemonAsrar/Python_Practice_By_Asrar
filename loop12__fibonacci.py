num = int(input("Enter number of terms: "))

a, b = 0, 1
print("Fibonacci Series:", a, b, end=" ")
for i in range(2, num):
    c = a + b
    print(c, end=" ")
    a, b = b, c
