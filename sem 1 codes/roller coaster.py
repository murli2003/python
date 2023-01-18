print("Welcome to the Rollercoaster")
height=int(input("enter ur height in cm's: "))
if height>=120:
    print("you can ride the rollercoaster")
    age=int(input("enter age: "))
    if age<12:
        print("please pay $5.")
        a= str(input("want photos (y/n)"))
        if a=="y":
            print("your total is:$8")
        else:
            print("total:$5")
    elif age>=12 and age<18:
        print("please pay $7.")
        a= str(input("want photos (y/n)"))
        if a== "y":
            print("your total is:%10")
        else:
            print("total:$7")
    else:
        print("please pay $10.")
        a= str(input("want photos (y/n)"))
        if a=="y":
            print("your total is:$13")
        else:
            print("total:$10")
        

else:
    print("get ur damn ass outta here")