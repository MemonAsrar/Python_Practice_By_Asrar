Array = []
sum = 0
for i in range(1,6):
    v = int(input(f"Enter The {i} value : "))
    Array.append(v)

for i in Array:
    sum += i

print(f"The Sum Of Array {sum}")