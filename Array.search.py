string_array = []
stringss = False

ent = int(input("Enter The Number : "))
for i in range(1,ent+1):
    string = input(f"Enter The {i} String : ")
    string_array.append(string)

find = input("Enter The String To Search : ")

for i in string_array:
    if i == find:
        stringss = True
    
if stringss:
    print(f"{i} is Avaliable")
else:
    print(f"{i} is not Avalible")
