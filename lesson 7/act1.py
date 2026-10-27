print("Welcome to the exam eligibility check")
m= input("Do you have a medical case? (‘Y’ for yes and ‘N’ for no).")
if m== "y":
    print("you are allowed to take the exam")
else:
    a= float(input("enter your attendnace percent "))
    if a> 75:
        print("you are allowed to give the exam")
    else:
        print("you are not allowed to give the exam")
