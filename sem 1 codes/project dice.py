g='''-----
|   |
| o |
|   |
-----'''

b='''-----
|o  |
|   |
|  o|
-----
'''

c='''-----
|o  |
| o |
|  o|
-----'''

d='''-----
|o o|
|   |
|o o|
-----'''

e='''-----
|o o|
| o |
|o o|
-----'''

f= '''-----
|o o|
|o o|
|o o|
-----'''


import random
min = 1
max = 6

roll_again = "yes"
score=0

while roll_again == "yes" or roll_again == "y":
    user = int(input("Enter your number between 1 and 6: \n"))
    print ("Rolling the dice...")
    a = (random.randint(min, max))
    print ("face value of dice is: ", a)
    if a == 1:
        print (g)
    elif a == 2:
        print (b)
    elif a == 3:
        print (c)
    elif a == 4:
        print (d)
    elif a == 5:
        print (e)
    else:
        print (f)

    
    if a == user:
        print ("user won ")
        score += 1
        print ("score= ",score)
    else:
        print ("user lose")
        score += 0
        print ("score=",score)

    roll_again = input("Roll the dice again?\n")
    if roll_again == "no"or roll_again =="n":
        print (f"Good Game \n Your score is: {score}")
        break




    

