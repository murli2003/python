print("welcome to pizza delivery system")
size= input("what kind of pizza do u want? S or M or L: ")
bill=0
if size=="S":
    bill+=10
elif size=="M":
    bill+=15
else:
    bill+=20
pep=input("want some peperonis? Y or N: ")
if pep=="Y":
    if size=="S":
        bill+=2
    else:
        bill+=3
ext= input("extra cheese? Y or N: ")
if ext=="Y":
    if size=="S":
        bill+=1
    else:
        bill+=2
print(bill)
