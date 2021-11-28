class Atm():
    print("welcome , please dont give your personal details its just a app give a random one.")
    cardNumber = input("Enter Your Card Number :- ")
    pinNumber  = input("Enter your pin code of your card :- ")
    deposit = input("Enter your money to deposit :- ")
    cashWithdraw = input("Enter your amount to withdraw :- ")

    balance  = deposit

    if(cashWithdraw > balance):
        print("Sorry!!,Your balance is lesser than the amount you wanted to withdraw, This is your balance ",balance)
    if(cashWithdraw <= balance):
        print("Your have withdrawed ",cashWithdraw," rupees from your account from card, Thank Your")


atmOutput = Atm()