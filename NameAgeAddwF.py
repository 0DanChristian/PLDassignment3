
# ask for name then save to variable
# ask for age then save to variable
# ask for address then save to variable
# print in format (Hi my name is _, I am _ years old and I live in _. )

def getName():
    _name = input("Name: ")
    return _name

def getAge():
    _age = input("Age: ")
    return _age

def getAddress():
    _address = input("Address: ")
    return _address

def display(NAME, AGE, ADDRESS):
    print(f"Hi, my name is {NAME}, I am {AGE} years old and I live in {ADDRESS} .")

name = getName()
age = getAge()
address = getAddress()

display(name, age, address)


