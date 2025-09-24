oddsum = 0
evensum = 0
for i in range(1,11):
    if i%2 != 0:
        print(f"{i}\t", end="" )
        oddsum += i

    elif i%2 == 0:
        print(f"{i}")
        evensum += i

print(f"the Sum Of Odd Value {oddsum}")
print(f"The Sum Of Even Value {evensum}")
    
