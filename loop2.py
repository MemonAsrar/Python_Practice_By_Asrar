oddsum = 0
evensum = 0

print("Odd Value")
for i in range(1 , 11, 2):
    print(i)
    oddsum += i

print(f"the Sum Of Odd Value {oddsum}")

print("Even Values")
for i in range(2, 11, 2):
    print(i)
    evensum += i

print(f"The Sum Of Even Value {evensum}")

