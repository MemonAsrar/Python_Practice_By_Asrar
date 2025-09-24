Name = input("Enter The Name: ")

marks = []

for i in range(1, 6):
    mark = int(input(f"Enter Marks of Subject {i}: "))

    while mark < 0 or mark > 100:  # validation
        print("Invalid Marks! Please re-enter.")
        mark = int(input(f"Enter Marks of Subject {i}: "))

    marks.append(mark)

Total = sum(marks)
percentage = Total / 5

if any(m < 35 for m in marks):
    Grade = "F"
elif percentage >= 70:
    Grade = "A"
elif percentage >= 60:
    Grade = "B"
elif percentage >= 50:
    Grade = "C"
elif percentage >= 35:
    Grade = "D"
else:
    Grade = "F"

print(f"Name: {Name}")
print(f"Total = {Total}")
print(f"Percentage = {percentage:.2f}%")
print(f"Grade = {Grade}")
