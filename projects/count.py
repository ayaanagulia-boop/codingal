print("Welcome to the digit counter")
number=int(input("Please enter a number: "))
n=number
ans=0
while n>0:
    n=n//10
    ans=ans+1
print("Number of digits is", ans)
    