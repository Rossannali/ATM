from click import prompt


desired_pin = '1234'
max_tries = 3


def verify_pin(the_pin):
    return the_pin == desired_pin

def main():
    tries = 0

    while tries < max_tries:
        pin = input('please enter your pin code: ')
        if verify_pin(pin):
            print('Correct')
            break
        else:
            print('Incorrect. Please enter again: ')
        tries += 1
        
    else:  
        print(" wrong, account locked!")
if __name__ == '__main__':
    main()

def withdraw(amount):
   print(str(amount) + " withdrawn!")

try:
   a = int(input())
   withdraw(a)

except (ValueError, TypeError):
   print("Please enter a number you wish to withdraw")


def display(self):
        print("\n Available Balance= 100 ",self.balance)
balance = 100

def withdraw():  # asks for withdrawal amount, withdraws amount from balance, returns the balance amount
    while True:
        withdraw = int(input("Enter amount to be withdrawn: "))
        if withdraw > balance:
            print("Error Amount not available in card.")
        else: 
            new_balance = balance - withdraw
            print("Amount left in your account: GBP" + str(new_balance))
            return (new_balance)

balance = withdraw()