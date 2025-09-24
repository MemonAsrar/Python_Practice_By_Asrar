attend = 0
unattend = 0
right_answer = 0
wrong_answer = 0
Total_Marks = 0 
cut_of_marks = 0

que1_ans = input("(Que:1 5x2 =\n(a)8 (b)9 (c)10 (d)skip\nEnter Your Choice : ").lower()

if que1_ans == "a" or que1_ans == "b":
    wrong_answer +=1
    attend +=1

elif que1_ans == "c":
    right_answer += 1
    attend +=1

elif que1_ans == "d":
    unattend += 1

else:
    print("Plze enter aviliable choice")
    exit()



que2_ans = input("(Que:2 5x2-2 =\n(a)8 (b)9 (c)10 (d)skip\nEnter Your Choice : )").lower()

if que2_ans == "b" or que2_ans == "c":
    wrong_answer +=1
    attend +=1

elif que2_ans == "a":
    right_answer += 1
    attend +=1

elif que2_ans == "d":
    unattend += 1
    
else:
    print("Plze enter aviliable choice")
    exit()  

que3_ans = input("(Que:3 75x2 =\n(a)180 (b)150 (c)100 (d)skip\nEnter Your Choice : ").lower()

if que3_ans == "a" or que3_ans == "c":
    wrong_answer +=1
    attend +=1

elif que3_ans == "b":
    right_answer += 1
    attend +=1

elif que3_ans == "d":
    unattend += 1
    
else:
    print("Plze enter aviliable choice")
    exit()


que4_ans = input("(Que:4 55+20 =\n(a)85 (b)90 (c)75 (d)skip)\nEnter Your Choice : ").lower()

if que4_ans == "a" or que4_ans == "b":
    wrong_answer +=1
    attend +=1

elif que4_ans == "c":
    right_answer += 1
    attend +=1

elif que4_ans == "d":
    unattend += 1
    
else:
    print("Plze enter aviliable choice")
    exit()


que5_ans = input("(Que:4 5+2+6+7 =\n(a)20 (b)19 (c)21 (d)skip)\nEnter Your Choice : ").lower()

if que5_ans == "b" or que5_ans == "c":
    wrong_answer +=1
    attend +=1

elif que5_ans == "a":
    right_answer += 1
    attend +=1

elif que5_ans == "d":
    unattend += 1
    
else:
    print("Plze enter aviliable choice")
    exit()    


print(f"Attend Ans = {attend}")
print(f"Unattend Ans = {unattend}")
print(f"Wrong Ans = {wrong_answer}")
print(f"Right Ans = {right_answer}")
print(f"Total Marks = {right_answer*5}")
print(f"Cut of Marks = {(wrong_answer*2)}")
print(f"After cut of marks = {((right_answer*5)-(wrong_answer*2))}")