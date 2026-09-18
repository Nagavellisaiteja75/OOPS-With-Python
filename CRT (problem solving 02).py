class account:
    holdername="Saiteja"
    accnumber="2334"
    balance=500

    def deposit(self,money):
     print(money)
     
    def withdrawl(self,cash):
     print(cash)
     
    def display(self,balance):
     print(self.balance)
     
s=account()
s.deposit(600)
s.withdrawl(100)
s.display(500)