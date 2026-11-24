print("Welcome to the mid digits calculator")
inp=str(input("Enter any number: "))
sum=0
for i in range(1, len(inp)-1):
    sum=sum+ int(inp[i])
print("The sum of numbers is:", sum)
