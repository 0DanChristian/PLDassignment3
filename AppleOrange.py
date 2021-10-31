# ask how many for apple
# ask how many for orange
# display total

def bApple():
    _pplmmnt = int(input("How many apple do you want to buy? "))
    return _pplmmnt

def bOrange():
    _rngmmnt = int(input("How many orange do you want to buy? "))
    return _rngmmnt

def ppl_prc():
    _pplprc = 20
    print(f"Our apple costs {_pplprc} pesos each. ")
    return _pplprc

def rng_prc():
    _rngprc = 25
    print(f"Our orange costs {_rngprc} pesos each. ")
    return _rngprc

def totalprc():
    ppl_ttl = apple*ppl_prc()
    rng_ttl = orange*rng_prc()
    _total = ppl_ttl + rng_ttl
    return _total

# intro
apple = bApple()
orange = bOrange()

# total
total = totalprc()

print(f"The total amount for your purchase is {total} pesos. Thank you!")
