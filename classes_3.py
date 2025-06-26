import random

var0 = 10 # type is: integer / int
var1 = "hello" # string / str
var2 = True # boolean / bool
var3 = 0.2 # float
var4 = None # None
var5 = {1, 2, 3} # set[int]
var6 = {0.2, 0.3, 0.4} # set[float]
var7 = {"Mihai", "Marius", "Magdalena"} #set[str]

var8: int = 100

class Account:
    def __repr__(self):
        return "Hello World"

    # def __str__(self):
    #     return "Not here"

ac1 = Account()
ac2 = Account()
# __str__
print(ac1)

accounts = [ac1, ac2]
# __repr__
print(accounts)

print("Bank Account exercise")

class BankAccount:
    def __init__(self, name: str):
        # private attribute
        self.__balance = 0
        self.owner = name

    def deposit(self, amount: int):
        """Allows the bank account owner to deposit x amount into their bank account balance.
        :param amount: the amount to be added to this account's balance
        :return:
        """
        if amount <= 0:
            print("Amount must be a positive number!")
            return

        print("Owner deposits: {} coins.".format(amount))
        self.__balance = self.__balance + amount
        print("Total balance: {}".format(self.__balance))

    def withdraw(self, amount: int):
        """Allows the bank account owner to withdraw x amount from their bank account balance. Balance must be bigger than the amount to be withdrawn
        :param amount: Amount to be withdrawn
        :return: Returns the amount that was withdrawn
        """
        # if the amount is positive and lower than current account's balance
        if amount > 0 and amount <= self.__balance:
            self.__balance = self.__balance - amount
            # returns the amount that was withdrawn from the account
            return amount
        else:
            print("Amount must be a positive number and must not exceed current balance.")
            return None

    def __give_me_a_million(self):
        # private method
        self.__balance = self.__balance + 1000000

    def coin_flip(self):
        # flip a coin. if it lands on heads, we get a million dollars.
        coin_flip_result = random.randint(0, 1)
        if coin_flip_result == 1:
            self.__give_me_a_million()
        print("Current Balance: {}".format(self.__balance))

    def get_balance(self):
        """Returns current account balance.
        :return:
        """
        # a way to access private method value
        return self.__balance

    # not used:
    # def set_balance(self, new_balance):
    #     if new_balance < 10000 and new_balance < 0:
    #         return
    #     else:
    #         self.__balance = new_balance


acc1 = BankAccount("Mihai")
acc1.deposit(500)
acc1.deposit(500)
acc1.deposit(-20)

acc1.withdraw(900)
acc1.coin_flip()

# print(acc1.__balance)
print(acc1.get_balance())

# Not possible:
# acc1.get_balance() = 10000

