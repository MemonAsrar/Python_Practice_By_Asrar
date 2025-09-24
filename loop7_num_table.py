s_num = int(input("Enter The Strat Value : "))
e_num = int(input("Enter The End Value : "))
for i in range(s_num,e_num+1):
    print(f"\n----- Multiplication Table of {i} -----\n")
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")
