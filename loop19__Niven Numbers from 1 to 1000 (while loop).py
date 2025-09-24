num = 1
print("Niven numbers from 1 to 1000 are:")

while num <= 1000:
    temp = num
    digi_sum = 0

    while temp >0:
        digi_sum = digi_sum + (temp%10)
        temp = temp //10

    if num%digi_sum == 0:
        print(num , end=" ")
    
    num +=1

