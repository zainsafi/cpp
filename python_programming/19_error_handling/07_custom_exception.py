# custom exception class
# We can create our own exceptions by inheriting from Exception class.

# Docstring: is a description/documentation string like comments it doesn't affect the program

# program 1: age_error
class age_error(Exception):
    "Raised when age is less than 18" # docstring
    pass

try: 
    age = int(input("Enter your age: "))
    if(age < 18):
        raise age_error("You are not eligible to vote")
    
except age_error as e:
    print(e)

else:
    print("you can vote")


# program 2: insufficientfunderror
print("\nInsufficient funds custom error")
class InsufficientFundError(Exception):
    def __init__(self,balance,amount):
        self.balance = balance
        self.amount = amount
        super().__init__(
            f"insufficient funds: {balance} available,{amount} requested"
        )

def withdraw(balance,amount):
    if amount > balance:
        raise InsufficientFundError(balance,amount)
    
    return balance - amount

try:
    balance = 250
    amount = int(input("Enter the amount you want to withdraw: "))
    newbalance = withdraw(balance,amount)
except InsufficientFundError as e:
    print(f"Transaction failed: {e}")

else:
    print(f"Your new balance is: {newbalance}")