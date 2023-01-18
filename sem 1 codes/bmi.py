a=input("ENTER HEIGHT(m): ")
b=input("enter weight(kg): ")
c=float(a)
d=float(b)
bmi=d/(c**2)
f= int(bmi)
print("your BMI is: ",f)
if f<18.5:
    print("u are underweight")
elif f<25:
    print("normal weight")
elif f<30:
    print("overweight")
elif f<35:
    print("obese")
else:
    print("clinically obese")