start=int(input("Enter the starting point: "))
end=int(input("Enter the ending point of the range: "))
print("The prime numbers in  the range", start, end, "are: ")

#outer loop just atkes care of the range of numbers
for i in range(start, end+1):
    mark=0
    if i>1:
        for j in range(2,i):
            if i%j==0:
                mark=mark+1
                break
            else:
                mark=0
        if mark==0:
                print(i)
    
        
                


