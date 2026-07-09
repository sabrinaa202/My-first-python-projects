import random
guessing_number =int(input("guess a random number between 1 to 500:  "))
secret_number=random.randint(1, 500)
if guessing_number==secret_number:
    print("Congratulations! You guessed the correct number!")
else :
    print("Incorrect.the correct number is ",secret_number)
