Day = int(input("Enter Day to find Time: "))


print(f"Year =  {Day//365}")
print(f"Mounth =  {Day%365//30}")
print(f"Days =  {Day%365%30}")
