#ATM FORMAT
import random


class atm:
    def __init__(self,name,account_no,balance=0):
        self.name=name
        self.account_no=account_no
        self.balance=balance

    def AccountDetail(self):
        print("""\n----------ACCOUNT DETAIL----------""")
        print(f"""Account Holder:{self.name}""")
        print(f"""Account Number:{self.account_no}""")
        print(f"""Available balance:{self.balance}\n""")
        
    def CheckBalance(self):
        print("""Available balance:""",self.balance)
        
    def Deposit(self,amount):
        self.amount=amount
        self.balance=self.balance+self.amount
        print(f"""Available balance:{self.balance}\n""")
        
    def withdraw(self,amount):
        self.amount=amount
        if self.amount>self.balance:
            print("""Insufficient fund!""")
            print(f"""Your balance is{self.balance} only.""")
            print("""Try with lesser amount than balance.""")
        else:
            self.balance = self.balance - self.amount
            print(f"""{amount} withdrawal successful!""")
            print("""Current account balance:""", self.balance)
            
    def transaction(self):
        print("""
            TRANSACTION 
        *********************
            Menu:
            1. Account Detail
            2. Check Balance
            3. Deposit
            4. Withdraw
            5. Exit
        *********************
        """)
        
        while True:
            try:
                option = int(input("Enter 1, 2, 3, 4 or 5:"))
            except:
                print("Error: Enter 1, 2, 3, 4, or 5 only!\n")
                continue
            else:
                if option == 1:
                    atm.AccountDetail()
                elif option == 2:
                    atm.CheckBalance()
                elif option == 3:
                    amount = int(input("How much you want to deposit:"))
                    atm.Deposit(amount)
                elif option == 4:
                    amount = int(input("How much you want to withdraw:"))
                    atm.withdraw(amount)
                elif option == 5:
                    print(f"""
                printing receipt..............
          ******************************************
              Transaction is now complete.                         
              Transaction number: {random.randint(10000, 1000000)} 
              Account holder: {self.name.upper()}                  
              Account number: {self.account_no}                
              Available balance:{self.balance}                    
 
             -------------------------------------
            | Thanks for choosing us as your bank |
            |       Visit us again!               |
             -------------------------------------                  
          ******************************************
          """)
                    break
                
print("""*************************WELCOME TO BANK OF DELHI*************************""")
print("_______________________________________________________________________________\n")
print("-------------------------------ACCOUNT CREATION------------------------------")
name = str(input("""                 Enter your name: """))
account_no= int(input("""   Enter your account number: """))
print("""           Congratulations! Account created successfully......\n""")
 
atm = atm(name, account_no)
atm.transaction()
