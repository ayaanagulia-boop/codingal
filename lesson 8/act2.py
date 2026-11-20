print("")
string=input("enter a string: ")
"""
hello
olleh
"""
ans=""
for a in string:
    ans= a+ans
print(string, "reverse: ", ans)