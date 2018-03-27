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
        self.withdrawals_list = []


    # allowed papers: 100, 50, 10, 5, and rest of request
    def withdraw(self, request):

        print(f"Welcome to {self.bank_name}")
        print(f"Your current balance = {self.balance}")
        print('='*10)

        remaining_balance = self.balance

        if request > self.balance:
            print("Insufficient Fund ")

        elif request <= 0: print("The reqested amount must be positive")

        else:

            self.withdrawals_list.append(request)
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

        print('='*10)

        self.balance = remaining_balance
        return remaining_balance

    def show_withdrawals(self):

        print(f"The following amounts has been withdrawed from {self.bank_name}: ")
        for withdrawal in self.withdrawals_list:
            print(withdrawal)

        print(f"Current balance = {self.balance}")

balance1 = 1500
balance2 = 3000

atm1 = ATM(balance1, "Smart Bank")
atm2 = ATM(balance2, "Baraka Bank")

atm1.withdraw(277)
atm1.withdraw(100)
atm1.withdraw(654)
atm1.withdraw(55)
atm1.withdraw(13)
atm1.withdraw(174)

atm2.withdraw(100)
atm2.withdraw(1000)
atm2.withdraw(65)
atm2.withdraw(36)
atm2.withdraw(87)
atm2.withdraw(96)
atm2.withdraw(125)
atm2.withdraw(1255)

atm1.show_withdrawals()
atm2.show_withdrawals()