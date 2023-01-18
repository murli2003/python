
a= str(input("enter everyones name separated by ', '"))
names =a.split(", ")
print(f"names are: ",names)
length = len(names)
import random
random_choice = random.randint(0, length)
random_person = names[random_choice]
print(random_person,"is going to pay for the bill")

#or for simpler code u can use
random_person1= random.choice(names)
print(random_person1, "is going to pay the bill")


