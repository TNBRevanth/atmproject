print("WELCOME TO MY BANK HAVE SAFE TRASACTION")
Name="Revanth "
pin=(int(input("Please Enter Your Four Digit pin To access your account: ")))
balance=5000
if pin==1234:
    print("Your Pin has been verified please access your account: ")
    print("1.Balance enquiry: ")
    print("2.Withdraw: ")
    print("3.Deposite: ")
    print("4.Help: ")
    option=int(input("Enter the option: "))
    if option==1:
        print(Name+"your balance is: ",balance,"rs/-")
    elif option==2:
        withdraw_amount=int(input("enter your withdraw amount: "))
        if withdraw_amount<=balance:
            balance=balance-withdraw_amount
            print("your updated balance is: ",Name + "your balance is",balance,"rs/-")
        else:
            print("insufficient balance")
    elif option==3:
        deposite_amount=int(input("enter your deposite amount: "))
        print("your previous balance amount is ",balance)
        balance=balance+deposite_amount
        print("your updated balance is: ",balance)
    elif option==4:
        print("contect help desk(1800-200-44)")
    else:
        print("invlid input")
else:
    print("invalid pin")


