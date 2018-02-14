'''
@Author: Houssam Sawan
ATM Mimic program
Input: the requested amount of money
Output: dollar bills count
'''

# allowed papers: 100, 50, 10, 5, and rest of request

money = 500

request = 277

if request > money:
    print("Insufficient Fund ")
    print(f"Your current balance is {money}")
else:
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



print("Done")
