'''
@Author: Houssam Sawan
ATM Mimic program
Input: the requested amount of money
Output: dollar bills count
'''

class ATM:
    '''ATM  software for withdrawing money'''
    def __init__(self, balance, bank_name):
        self.balance = balance
        self.bank_name =bank_name


    # allowed papers: 100, 50, 10, 5, and rest of request
    def withdraw(self, request):

        print(f"Welcom to {self.bank_name}")
        print(f"Your current balance = {self.balance}")
        print("===========================================")

        remaining_balance = self.balance

        if request > self.balance:
            print("Insufficient Fund ")

        elif request <= 0: print("The reqested amount must be positive")

        else:

            remaining_balance = self.balance - request

            while request > 0:

                if request // 100 > 0:
                    print("Give 100")
                    request -= 100

                elif request // 50 > 0:
                    print("Give 50")
                    request -= 50

                elif request // 10 > 0:
                    print("Give 10")
                    request -= 10

                elif request // 5 > 0:
                    print("Give 5")
                    request -= 5

                elif request > 0:
                    print(f"Give {request}")
                    request = 0

        print("===========================================")
        
        self.balance = remaining_balance
        return remaining_balance

balance1 = 500
balance2 = 1000

atm1 = ATM(balance1, "Smart Bank")
atm2 = ATM(balance2, "Baraka Bank")

atm1.withdraw(277)
atm1.withdraw(800)

atm2.withdraw(100)
atm2.withdraw(2000)