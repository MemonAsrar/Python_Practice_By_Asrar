num = int(input("Enter The Number: "))
harmonic = 0
value = 0

for i in range(1,num+1):
    harmonic += 1/i 

print(f"Harmonic number H{num} = {harmonic:.4f}")