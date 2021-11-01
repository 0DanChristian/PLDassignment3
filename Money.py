# Enter how much money you have
# Ask for the price of an apple
# Display the out put
# Format: You can buy ___ apples and your change is ____ pesos.


def hm_money():
    hmMoney = int(input("How much money do you have? "))
    return hmMoney

def prc_ppl():
    prcApple = int(input("How much is an apple? "))
    return prcApple

def ttl_mnt():
    ttlAmmount = amountMoney // priceApple
    return ttlAmmount

def changeP():
    Pchange = amountMoney % priceApple
    return Pchange
   
def display(ttlApple, change):
    print(f"You can buy {ttlApple} apples and your change will be {change} pesos, thank you! ")

# steps
# 1. ask for the amount of money you have then save as variable
amountMoney = hm_money()
# 2. ask for the price of an apple then save as variable
priceApple = prc_ppl()
# 3. solve for the total amount of apples you can buy then save as variable 
ttlApple = ttl_mnt()
# 4. solve for the change then save as variable
change = changeP()
# 5. display the total number of apples and the change
output = display(ttlApple, change)