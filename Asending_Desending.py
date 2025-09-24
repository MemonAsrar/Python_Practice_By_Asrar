n = int(input("Enter how many numbers: "))

a = []
for i in range(n):
    a.append(int(input("Enter number: ")))

for i in range(n):
    for j in range(n-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

print("Ascending :", a)
print("Second Largest Number : ",a[len(a)-2])


for i in range(n):
    for j in range(n-1):
        if a[j] < a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

print("Decending :", a)
