height=float(input("Enter your height(meter) : "))
weight=float(input("Enter your weight(kg) : "))
BMI=(weight/(height*height)) 
print("Your BMI is ",BMI)
if  BMI<18.5: 
    print("You have underweight")

elif BMI<25:
    print("You have healthy weight")

else:
	print("You have overweight")
