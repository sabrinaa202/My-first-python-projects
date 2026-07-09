import random
guessing_number=int(input("Guess a number between 1 to 600: "))
secret_number=random.randint(1,600)
while guessing_number !=secret_number:
     input("Wrong❌.Guess again ")
guessing=int(input("Guess the number again: "))
print(" Congratulations! The secret number is ", secret_number)
