import random

print("1. Rock\n2.paper\n3.Scissors")
user=int(input("enter your choice: "))

computer=random.randint(1,4)

choices=["Rock","paper","Scissors"]
print("computer chose:", choices[computer-1])

if user ==computer:
    print("Draw")
elif (user ==1 and computer ==3) or \
    (user ==2 and computer ==1) or \
    (user ==3 and computer ==2):
    print("You win!!")
else:
    print("You Loose")    