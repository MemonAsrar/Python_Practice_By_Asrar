R = int(input("Enter The Rows : "))
C = int(input("Enter The Column : "))

print("Step2")

matrix = []

if R != C:
    print(f"The Matrix Is Nither Simatrical nor Square It Shoud Have {R} == {C}")
else:
    for i in range(R):
        a=[]
        for j in range(C):
            a.append(int(input("Enter The Value : ")))
        matrix.append(a)

    print("Formed array")

    simitrical = True

    for i in range(R):
        for j in range(C):
            if matrix[i][j] != matrix[j][i]:
                simitrical = False
                break
        if not simitrical:
            break

    if simitrical:
        for i in range(R):
            for j in range(C):
                print(matrix[i][j], end=" ")
            print()
        print("Above matrix is simatrical")
    else:
        for i in range(R):
            for j in range(C):
                print(matrix[i][j], end=" ")
            print()
        print("Above matrix is Not simatrical")