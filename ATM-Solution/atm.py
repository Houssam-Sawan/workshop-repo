'''
@Author: Houssam Sawan
ATM Mimic program
Input: the requested amount of money
Output: dollar bills count
'''

# allowed papers: 100, 50, 10, 5, and rest of request
def withdraw(balance, request):

    print(f"Your current balance is: {balance}")

    remaining_balance = balance
    if request > balance:
        print("Insufficient Fund ")

    elif request <= 0: print("The reqested amount must be positive")

    else:

        remaining_balance = balance - request

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

    return remaining_balance

balance = 500

balance = withdraw(balance, 277)
balance = withdraw(balance, 30)
balance = withdraw(balance, 5)
balance = withdraw(balance, 500)