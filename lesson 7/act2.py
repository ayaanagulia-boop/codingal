e= float(input("Enter the units consumed: "))
if e<50:
    print("per unit cost is 2.60", "tax: 25", "bill: ", (e* 2.60)+25.0 )
elif e>= 50 and e<100:
    print("per unit cost is 3.25 ", "tax:35", "bill: ", (e* 3.25)+35.0 )
elif e>=100 and e<200:
    print("per unit cost is 5.26", "tax: 45", "bill: ", (e* 5.26)+45.0)
else:
    print("per unit cost is 8.45", "tax: 75", "bill: ", (e* 8.45)+75.0)
