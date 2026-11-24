amt= int(input("Enter the amount: "))
#note1 represents 500 currency
note1= amt//500
#note2 represents 100 rupee currency
note2= (amt%500)//100
note3= ((amt%500)%100)//50
note4= ((amt%500)%100)%50
print(amt, "Rupees is asked. We will have", note1, "500 rupee notes", note2, "100 rupee notes", note3 , "50 rupee notes", note4 ,"and 1 rupee.")