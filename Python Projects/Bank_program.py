#  Bank program Python

def show_balance() :
    print(f"Your current balance is: ${balance:.2f}")


def deposit() :
     amount = float(input("Enter amount to deposit : "))

     if amount <= 0 :
         print("Thats's not a Valid Amount")
         return 0
     else :
         return amount


def withdraw() :
    amount = float(input("Enter amount to Withdraw : "))

    # print(f"You have Withdrawn ${amount}")
    if amount > balance :
         print("In-Sufficient Funds")
         return 0
    elif  amount < 0 :
           print("Amount Must be grater than $0")
    else :
         return amount
    
    

     
balance = 0
is_running = True


while is_running :


    print("Banking Program")
    print("1.Show Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.EXIT")


    choice = input("Enter your Choice (1-4): ")

    if choice == '1' :
        show_balance()

    elif choice == '2' :
         balance += deposit()  

    elif choice == '3' :      
       balance -= withdraw()

    elif choice == '4' :  
        is_running = False

    else :
        print ("That is not a Valid choice ")      



print("Thank You ! Have a Nice Day")


