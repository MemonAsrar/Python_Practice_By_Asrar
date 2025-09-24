R = int(input("Enter The Rows : "))
C = int(input("Enter The Column : "))

print("Step2")

matrix = []

for i in range(R):
    a=[]
    for j in range(C):
        a.append(int(input("Enter The Value : ")))
    matrix.append(a)

print("Formed array")

for i in range(R):
    for j in range(C):
        print(matrix[i][j], end=" ")
    print()

print()
print()
print()

for i in range(R):
    for j in range(C):
        print(matrix[j][i], end=" ")
    print()

