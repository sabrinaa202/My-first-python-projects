import random
guessing=input("rock,paper or scissors? ")
secret=random.randint(1,3)
if secret==1:
    secret="rock"
elif secret==2:
    secret="paper"
else:
    secret="scissors"
print("Computer chose ",secret)
if secret==guessing:
	print("Draw.Try again.")
elif secret=="rock" and guessing=="paper" or secret=="paper" and guessing=="scissors" or secret=="scissors" and guessing=="rock":
    print("You wonn!!")
else:
	print("You lost")
