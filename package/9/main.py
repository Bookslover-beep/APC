#9.Develop a package banking containing: 
#a)account.py – account creation and balance  
#b)transaction.py – deposit and withdrawal  
#c)loan.py – loan calculation  
#Create a main program to use the package. 

from banking import account, transaction, loan

acc = account.create_account("Alice", 1000)
transaction.deposit(acc, 500)
print("Balance:", acc["balance"])
print("Loan Amount:", loan.calculate_loan(5000))