from cardHolder import cardHolder
t_hist=[]
def print_menu():

    print("Please choose the following options ... ")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Transaction History")
    print("5. Transfer Money")
    print("6. Exit")

def deposit(cardHolder):
    try:
        deposit= float(input("How much ₹₹ would you like to Deposit : "))
        cardHolder.set_balance(cardHolder.get_balance()+deposit)
        print("Thank you for your ₹₹. Your new balance is : ",str(cardHolder.get_balance()))
        t_hist.append( f"Deposit : {deposit} ")
    except:
        print("Invalid input")

def withdraw(cardHolder):
    try:
        withdraw = float(input("How much ₹₹ would you like to withdraw : "))
        if(cardHolder.get_balance()<withdraw):
            print("Insufficient balance :(")
        else:
            cardHolder.set_balance(cardHolder.get_balance()-withdraw)
            print("You are good to go! Thank You")
            t_hist.append( f"Withdraw : {withdraw} " )
    except:
        print("Invalid input")

def transfer_money(cardHolder):
    try:
        transfer_money= float(input("How much ₹₹ would you like to Transfer : "))
        print("Transfer money to another account has transaction charges of 0.03%")
        total_debit= transfer_money+transfer_money*.03
        if(cardHolder.get_balance()<transfer_money):
            print("Insufficient balance :(")
        else:
            cardHolder.set_balance(cardHolder.get_balance()-total_debit)
            input("Enter receiver's account no. : ")
            input("Enter receiver's bank name : ")
            input("Enter receiver's name : ")
            print(f"Total amount debited : {total_debit}")
            print("You are good to go! Thank You")
            t_hist.append( f"Transfer Money : {transfer_money}" )
    except:
        print("Invalid input")

def check_balance(cardHolder):
    print("Your current balance is : ",cardHolder.get_balance()) 

def transaction_history(cardHolder):
   for t in t_hist:
       print(t)

if __name__ =="__main__":
    current_user = cardHolder("","","","","") 

    list_of_cardHolders=[]
    list_of_cardHolders.append(cardHolder("9083441167",9083,"Dipayan","Dutta",150.12))
    list_of_cardHolders.append(cardHolder("6290973057",6290,"Aditi","Bag",145.52))
    list_of_cardHolders.append(cardHolder("9382435548",9382,"Mainak","Dutta",185.90))
    list_of_cardHolders.append(cardHolder("8317679248",8317,"Hritwick","Biswas",128.36))
    list_of_cardHolders.append(cardHolder("9082440918",9082,"Pritam","Biswas",150.05))

    debitCardNum = ""
    while True:
        try:
            debitCardNum = input("Please enter your Debit card no. :")
            debitMatch = [holder for holder in list_of_cardHolders if holder.cardNum == debitCardNum]  
            if(len(debitMatch)>0):
                current_user = debitMatch[0]
                break
            else:
                print("Card number not recognized . Please try again")  
        except:
            print("Card number not recognized . Please try again")

    while True:
        try:
            userPin = int(input("Please enter your PIN : ").strip())    
            if(current_user.get_pin() == userPin):
                break
            else:
                print("Incorrect PIN. Please try again.")
        except:
            print("Incorrect PIN. Please try again.")   

    print("Welcome" , current_user.get_firstname(),":)")             
    option = 0
    while(option != 6):
        print_menu()
        try:
            option = int(input())
        except:
            print("Invalid Input. Please try again.")

        if(option == 1):
            deposit(current_user)
        elif(option == 2):
            withdraw(current_user)
        elif(option == 3):
            check_balance(current_user)
        elif(option == 4):
            transaction_history(current_user)
        elif(option == 5):
            transfer_money(current_user)
        elif(option == 6):  
            break
        else:
            option = 0 

    print("Thank you.Have a nice day.  :)")
