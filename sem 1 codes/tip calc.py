print("welcome to tip calculator")
a=float(input("total bill: "))
b=int(input("percentage you would like to give? 10 or 12 or 15 percent: "))
c=int(input("how many people to split bill into: "))
#d is the tip
d= a*(b/100)
#e is the total amount after adding tip and splitting into peoples  
e=(a+d)/c
f=("{:.2f}".format(e))
print("each person should pay: ",f)
