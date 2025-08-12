import numpy as np

year = 1
accounts = {}
accountsnames = {}

def randomGenerator():
    run = True
    while run:
        accountNumber = 0
        random = [np.random.randint(1000 , 10000) , np.random.randint(1000 , 10000) , np.random.randint(1000 , 10000)]
        random.reverse() #I do this to generate random numbers in a weird way
        for i in random:
            accountNumber = accountNumber*10000 + i 
        if accountNumber not in BankAccounts.AccountNumbers:
            BankAccounts.AccountNumbers.append(accountNumber)
            run = False
            return accountNumber
        
def passwordcheck(user , password):
    try:
        return user.password == password
    except ValueError:
        return False

def amountchecker(amount):
    try:
        if amount > 0:
            return amount
        else:
            return 0
    except ValueError:
        return 0
    
def incorrect():
    print("Incorrect passoword.")

def insufficienct():
    print("Insuffiecient amount")

class BankAccounts:

    UserNumber = 0
    AccountNumbers = []
    objectlist = []
    YearMade = 2024

    def __init__(self , name , gender , age , initial_amount , password , ir = 1.02):

        self.name = name
        self.gender = gender
        self.age = age
        self.amount = amountchecker(initial_amount)
        self.password = password
        self.accountNumber = randomGenerator()
        self.transactionsMade = 0
        self.yearJoined = 2024 + year
        self.ir = ir

        BankAccounts.UserNumber += 1
        BankAccounts.objectlist.append(self)
        
    def GetAccountNumber(self , password):
        Bool = passwordcheck(self , password)
        if Bool:
            print(self.accountNumber)
        else:
            print("Wrong Password")

    def bankDetails(self , password):
        Bool = passwordcheck(self , password)
        if Bool:
            print(self.__dict__)
        else:
            print("Wrong Password")

    def balance(self):
        print(f"Balance amount in bank: {self.amount}")

    def transfer(self , user , amount , password):
        Bool = passwordcheck(self , password)
        amount = amountchecker(amount)
        if self.amount >= amount:
            if Bool:
                self.amount -= amount
                user.amount += amount
                print(f"Amount {amount} transferred successfully to {user.name}")
                self.balance()
            else:
                incorrect()
        else:
            insufficienct()

    def withdraw(self , amount , password):
        Bool = passwordcheck(self , password)
        amount = amountchecker(amount)
        if self.amount >= amount:
            if Bool:
                self.amount -= amount
                print(f"Amount {amount} withdrawn successfully.")
                self.balance()
            else:
                incorrect()
        else:
            insufficienct()

    def deposit (self,amount , password):
        Bool = passwordcheck(self ,password)
        amount = amountchecker(amount)
        if Bool:
            self.amount += amount
            print(f"Amount {amount} deposited successfully.")
            self.balance()
        else:
            incorrect()

    def changepassword(self , password):
        Bool = passwordcheck(self , password)
        if Bool:
            loop = True
            while loop:
                try:
                    password = int(input("Enter 4 digit pin code: "))
                    if password >= 1000 and password<= 9999:
                        self.password = password
                        print(f"Password changed to {password} successfully.")
                        loop = False
                    else:
                        print("Enter valid password.")
                except ValueError:
                    print("Enter a valid number.")
        else:
            incorrect()
            
    @classmethod
    def yearpassed(cls):
        for i in cls.objectlist:
            i.amount = i.amount*i.ir

    @classmethod
    def details(cls):
        print(cls.__dict__)

def objectcreator():
    print("Creating account. \n Enter the following details:")
    name = input("Enter your name: ")
    loop = True
    while loop:
        try:
            age = int(input("Give your age: "))
            if age > 17:
                loop = False
            else:
                print("Enter a valid age.")
        except ValueError:
            print("Enter a valid number.")

    gender = input("Enter your gender.")
    loop = True
    while loop:
        try:
            initial_amount = int(input("Give your initial amount: "))
            if initial_amount > 9999:
                loop = False
            else:
                print("Minimum amount is 10k.")
        except ValueError:
            print("Enter a valid number.")
    loop = True
    while loop:
        try:
            password = int(input("Enter 4 digit pin code: "))
            if password >= 1000 and password <= 9999:
                loop = False
            else:
                print("Enter valid password.")
        except ValueError:
            print("Enter a valid number.")

    globals()[name] = BankAccounts(name , gender , age , initial_amount , password)
    print("Account created successfully!")
    accounts.update({globals()[name].accountNumber:globals()[name]})
    accountsnames.update({globals()[name].accountNumber:globals()[name].name})

def accountviewer():
    print(accountsnames)

def accountaccessor():
    try:
        anum = int(input("Give account number of user you want to access: "))
        if anum == 0:
            print("Going back.")
        elif anum not in accounts:
            print("No such account exists.")
        else:
            print(f"Welcome {accountsnames[anum]}")
            in_account(accounts[anum])

    except ValueError:
        print("Enter appropriate input.")
  
def in_account(user):
    while True:
        print("Press 1 to tranfer amount.")
        print("Press 2 to withdraw amount.")
        print("Press 3 to deposit amount.")
        print("Press 4 to view bank details.")
        print("Press 5 to change password.") 
        try:
            x = int(input())
            if x == 0:
                print("Going back.")
                break
            elif x == 1:
                other = int(input("Enter bank account of user you want to transfer to: "))
                if other not in accounts:
                    print("No such user exists.")
                else:
                    amount = int(input("Give an amount to transfer."))
                    password = int(input("Enter your password: "))
                    user.transfer(accounts[other] , amount , password)
            
            elif x == 2:
                amount = int(input("Give amount you wish to withdraw: "))
                password = int(input("Enter your password: "))
                user.withdraw(amount , password)

            elif x == 3:
                amount = int(input("Enter amount you want to deposit."))
                password = int(input("Enter your password: "))
                user.deposit(amount , password)

            elif x == 4:

                password = int(input("Enter your password: "))
                user.bankDetails(password)

            elif x == 5:

                password = int(input("Enter your current password: "))    
                user.changepassword(password)

            else:
                print("Enter a valid number.")

        except ValueError:
            print("Enter an appropriate input.")     

def main():
    global year
    print("Welcome")
    print(f"Current year is {year + 2024}")
    run = True
    while run:
        print("Press 1 to create bank account.")
        print("Press 2 to view current accounts.")
        print("Press 3 to access an account.")
        print("Press 4 to advance an year.")
        print("Press 5 to view overall details.")
        print("Press 6 to exit simulation.")
        print("0 is treated as back.")
        loop = True
        while loop:
            try:
                user = int(input())
                if user == 1:
                    objectcreator()
                    loop = False
                elif user == 2:
                    print("Displaying current bank accounts.")
                    accountviewer()
                    loop = False
                elif user == 3:
                    accountaccessor()
                    loop = False
                elif user == 4:
                    year += 1
                    print(f"The year is now {year}")
                    BankAccounts.yearpassed()
                    loop = False
                elif user == 5:
                    print(f"Current year is {year}")
                    BankAccounts.details()
                    loop = False
                elif user == 6:
                    print("Ending simulation.")
                    print(f"Current Year is {year}")
                    for i in accounts.values():
                        i.bankDetails(i.password)

                    BankAccounts.details()
                    loop = False
                    run = False

                else:
                    print("Enter a valid number.")
            except ValueError:
                print("Enter a valid number.")

if __name__ == "__main__":
    main()
 