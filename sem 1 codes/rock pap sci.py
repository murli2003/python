rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
game_images= [rock, paper, scissors]
person= int(input("enter rock as 0 paper as 1 and scissor as 2 \n"))
print(game_images[person])

import random

computer= random.randint(0,2)
print(f"computer choose {computer}")
print(game_images[computer])

if person == computer:
    print(f"draw")
elif computer==2 and person == 0:
    print("user wins")
elif computer==0 and person == 2:
    print("computer wins")
elif computer > person:
    print("computer wins")
else:
    print("user won")

