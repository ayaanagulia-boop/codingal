print("Welcome to Ride Selection\n\n\n")
print("Choose vehicle preference-\n 1) Bike\n 2)car")
c=int(input("choose either 1 or 2: \n"))
if c==1:
    print("you selected a bike")
    print("choose-\n 1)scooty\n2) sports bike")
    b= int(input("choose 1 or 2: "))
    if b==1:
        print("you selected scooty")
    elif b==2:
        print("you selected sports bike")
    else:
        print("invalid choice")

else:
    if c==2:
        print("You selected a car\n")
        print("choose- \n 1) Sedan\n 2) SUV")
        a= int(input("Choose either 1 or 2: "))
        if a==1:
            print("you selected a sedan")
        elif a==2:
            print("you selected an SUV")
        else:
            print("invalid choice")