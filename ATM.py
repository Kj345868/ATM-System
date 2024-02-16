class ATM:
    user_name=[]
    user_bal=[]
    def __init__(self):
        file = open("C:/Python/ATM SYSTEM/names.txt","r")
        dictionary = file.read().split('\n')
        for x in dictionary:
            self.user_name.append(x)
        file.close()
        file2 = open("C:/Python/ATM SYSTEM/balance.txt","r")
        dictionary2 = file2.read().split('\n')
        for x in dictionary2:
            self.user_bal.append(x)
        file2.close()
        print("--!!--* Welcome to ATM SYSTEM *--!!--")
        for i in range(0,2):
            print()
        print("1.Register")
        print("2.Login")
        print("3.Exit")
        print()
        ch = int(input("Enter your choice:"))
        if ch == 1:
            self.Register()
        elif ch == 2:
            self.Login()
        elif ch == 3:
            self.Save()
            pass
        else:
            print("Invalid Choice")
    def Register(self):
        username=input("Enter a Username:")
        password=int(input("Enter 4 digit pass:"))
        repassword=int(input("Re-Enter a password:"))
        passtostr=str(password)
        filetoread = open("C:/Python/ATM SYSTEM/ATM.txt","r")
        verifyuser = filetoread.read()
        filetoread.close()
        if password != repassword:
            print("Password are not same")
            self.__init__()
        elif passtostr.__len__()  != 4:
            print("Please Enter 4 digit password:")
            self.__init__()
        elif username in verifyuser:
            print("Username is already exits.")
            self.__init__()
        else:
            file = open("C:/Python/ATM SYSTEM/ATM.txt","a")
            file.write(username+" "+str(password)+"\n")
            self.user_name.append(username)
            self.user_bal.append(str(1000))
            print("Registration Successful")
            file.close()
            self.__init__()        
    def Login(self):
        username=input("Enter a Username:")
        password=int(input("Enter a Password:"))
        file = open("C:/Python/ATM SYSTEM/ATM.txt","r")
        tosearch=file.read()
        if username+" "+str(password) in tosearch:
           print("Login Successful.")
           self.Index(username,password)
        else:
            print("Login Unsuccessful.")
            self.__init__()
        file.close()
    def Index(self,username,password):
         print("--!!--* ATM SERVICES *--!!--")
         print()
         print("1.Withdraw Money")
         print("2.Add Money")
         print("3.Check Balance")
         print("4.Logout")
         ch = int(input("Enter Your choice:"))
         if ch == 1:
             self.withdraw(username,password)
         elif ch==2:
             self.add(username,password)
         elif ch == 3:
             self.checkbalance(username,password)
         elif ch == 4:
             self.__init__()
         else:
             print("Invalid Choice")
             self.Index(username,password)
    def withdraw(self,username,password):
        amount = int(input("Enter amount to withdraw:"))
        useramount = 0
        index = 0
        for x in range(len(self.user_name)):
            if username == self.user_name[x]:
                useramount = int(self.user_bal[x])
                index = x
                break
        if int(useramount) < int(amount):
            print("Insufficient balance in your bank account")
            self.Index(username,password)
        else:
            print("Money has withdrawn:",amount)
            self.user_bal[index] = useramount-amount
            self.Index(username,password)
    def add(self,username,password):
        amount=int(input("Enter a amount to add:"))
        if amount < 0:
            print("Invalid amount")
            self.Index(username,password)
        else:
           useramount = 0
           index = 0
           for x in range(len(self.user_name)):
               if username == self.user_name[x]:
                useramount = int(self.user_bal[x])
                index = x
                break
           self.user_bal[index]=str(useramount+amount)
           print("Money is Added to Your account")
           self.Index(username,password)
    def checkbalance(self,username,password):
        useramount = 0
        index = 0
        for x in range(len(self.user_name)):
            if username == self.user_name[x]:
                useramount = int(self.user_bal[x])
                index = x
                break
        print("You're Current Balance is:",useramount)
        self.Index(username,password)
    def Save(self):
        file = open("C:/Python/ATM SYSTEM/balance.txt","w")
        balance=""
        for x in self.user_bal:
            balance+=str(x)+"\n"
        file.write(str(balance))
        file.close()
        file2 = open("C:/Python/ATM SYSTEM/names.txt","w")
        names=""
        for x in self.user_name:
            names+=x+"\n"
        file2.write(str(names))
        file2.close()
atm = ATM()



