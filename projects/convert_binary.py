print("Welcome to the binary converter: ")
inp=int(input("Enter a number: "))

z=""

while inp>0:
    r=inp%2
    z=str(r)+z
    inp=inp//2
    
print(z)

