s_num = int(input("Enter The Start_Num : "))
e_num = int(input("Enter The End_Num : "))

for i in range(s_num,e_num):
    sum = 0

    for j in range(1,i):
        if i%j==0:
            sum = sum+j
    if sum == i:
        print(i)