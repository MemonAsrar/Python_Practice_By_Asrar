Currancy = int(input("Enter The Amount : "))
Choice = int(input("Enter The Choice\n1 : Dollar to Rs \n2: Rs to Dollar \n3: Cm to Foot \n4: Km to Foot \n5: Pound to Kg \n6: F to C \n   Enter The Choice "))

if Choice == 1:
    print(Currancy/83,"Dollar")
elif Choice == 2:
    print(Currancy*83,"Ruppes")
elif Choice == 3:
    print(Currancy / 0.0328084, "Foot")
elif Choice == 4:
    print(Currancy * 3280.84, "Foot")
elif Choice == 5:
    print(Currancy * 0.453592, "Kilogram")
elif Choice == 6:
    print(Currancy*30.48, "Centimeter")
else:
    print("Problem!")
