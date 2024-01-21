# ATM System
print("Welcome to A.Bank, How Can We help you?")

# Functionality
Trails=3

while Trails != 0:
    Username=str(input("Enter Your Name here: "))
    Date_of_Birth=input("Enter Date of Birth: ")
    Create_Pin=int(input("Creates a 4-Digit Code: "))
    Balance=int(input("Enter Your Bank Balance: "))
    Pin=int(input("Please enter the 4-Digit PIN Code: "))
    if Pin != Create_Pin:
        Trails -= 1
        print("Wrong Pin Number, You Have", Trails, "Trails Left")
    else:
        Userchoise = input("d: Deposit or w: Withdraw: ")        
        if Userchoise == "d":
            UserDesposit =  int(input("Enter Amount You Would like to deposit : "))
            print(UserDesposit, "PKR have been Deposited into your Account")
        if Userchoise == "w":
            Userwithdraw =  int(input("Enter Amount You Would like to WithDraw : "))
            if Userwithdraw > Balance:
                print("Insufficient balance.")
                
            else:
                Userwithdraw == Balance or Userwithdraw < Balance
            print(Userwithdraw, "PKR have been WithDrawn from your account")
            
    UserExit = input("Would you like to continue? Y/N: ")       
    if UserExit == "N":  
        print("Thank you For Using A.Bank ")
        break
    else:
        continue