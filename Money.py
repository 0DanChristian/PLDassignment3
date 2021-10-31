hmmoney = int(input("Please enter the amount of money you have. "))
pplprc = int(input(" ask for the price of the apples. "))

maxppl = int(input("maximum apples that you can buy"))

pplttl = pplprc * maxppl
mleft = hmmoney - pplttl
print(f"You can buy {maxppl} apple and your change is {mleft} pesos.", end ="")
print("Thank you!")