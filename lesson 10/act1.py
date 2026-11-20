print("Welcome to the charater counting program")
inp=input("enter a string: ")
ch=input("enter the letter to be counted: ")
i=0
c=0
while i<len(inp):
    if ch==inp[i]:
        c=c+1
    i=i+1
print(c)