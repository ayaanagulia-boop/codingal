print("welcome to the program that checks if a number is an armstrong number or not")
m=int(input("enter a number: "))
n=m
a=0
while n>0:
    r= n%10
    a= a+(r**3)
    n=n//10
if a==m:
    print("it is an armstrong number")
else:
    print("it is not an armstrog number")