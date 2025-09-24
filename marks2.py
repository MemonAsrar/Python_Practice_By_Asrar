Name = input("Enter the Name : ")
M1 = int(input("Enter marks of subject 1: "))
if M1 < 0 or M1 > 100:
    print(f"{M1} is invalid Pleaze enter Valid Value")
    exit()
M2 = int(input("Enter marks of subject 2: "))
if M2 < 0 or M2 > 100:
    print(f"{M2} is invalid Pleaze enter Valid Value")
    exit()
M3 = int(input("Enter marks of subject 3: "))
if M3 < 0 or M3 > 100:
    print(f"{M3} is invalid Pleaze enter Valid Value")
    exit()
M4 = int(input("Enter marks of subject 4: "))
if M4 < 0 or M4 > 100:
    print(f"{M4} is invalid Pleaze enter Valid Value")
    exit()
M5 = int(input("Enter marks of subject 5: "))
if M5 < 0 or M5 > 100:
    print(f"{M5} is invalid Pleaze enter Valid Value")
    exit()

Total = M1+M2+M3+M4+M5
Percentage = Total/5

if Percentage >= 70:
    Grade = "A"
elif Percentage >= 60:
    Grade = "B"
elif Percentage >= 50:
    Grade = "C"
elif Percentage >= 35:
    Grade = "D"
elif Percentage < 35:
    Grade = "E"




print(f"Total = {Total}")
print(f"Percentage = {Percentage}%")

subjects = [M1, M2, M3, M4, M5]
grace_needed = 0   

for mark in subjects:
    if mark < 35:
        diff = 35 - mark
        grace_needed += diff


if grace_needed == 0:
    print(" Result: Passed")
elif grace_needed <= 8:
    print(f" Result: Passed using {grace_needed} grace marks")
else:
    print(" Result: Failed")

