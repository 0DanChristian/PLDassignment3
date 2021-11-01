# Enter how much money you have
# Ask for the price of an apple
# Display the out put
# Format: You can buy ___ apples and your change is ____ pesos.


def hm_money():
    _money = int(input("How much money do you have? "))
    return _money

def prc_ppl():
    _pA = int(input("How much is an apple? "))
    return _pA

# steps
# 1. ask for the amount of money you have then save as variable
amountMoney = hm_money()
# 2. ask for the price of an apple then save as variable
priceApple = prc_ppl()
# 3. solve for the total amount of apples you can buy then save as variable 
# 4. solve for the change then save as variable
# 5. display the total number of apples and the change
