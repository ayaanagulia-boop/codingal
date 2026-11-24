n=int(input("Enter a number: "))
number=1

for i in range(1, n+1):
    for p in range(1, i+1):
        print(number, end=" ")
        number=number +1
    print()