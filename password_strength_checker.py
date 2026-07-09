password=input("Enter your password: ")
(len(password))

if len(password)<8:
	print("Too short❌")
	
elif len(password)<11:
	print("Medium password")

else:
    print("Strong password")
