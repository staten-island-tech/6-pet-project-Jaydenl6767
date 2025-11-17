"""class Calculator():
    def add(x, y):
        print(x + y)
        return x + y

    def add_many(numbers):
        print(sum(numbers))
        return sum(numbers)

    def subtract(numbers):
        return numbers

Calculator.add(5, 6)

class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory

    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # double underscore means "private"

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print(f"{self.owner} has ${self.__balance}")"""\
        
class pet: 
    def __init__(self, happiness, name, health, hunger):
        self.happiness = happiness
        self.name = name     
        self.health = health
        self.hunger = hunger

def play(self, game, value):
    self.happiness += value
    print(f"{self.name} is playing a {game}") 
    print(f"{self.name}'s happiness increased to {self.happiness}")

def eat(self, food, value):
    self.hunger -= value
    self.happiness += value
    print(f"{self.name} is eating {food}")
    print(f"{self.name}'s hunger decreased to {self.hunger} and {self.name}'s happiness increased to {self.value}")

def check(self):
    print(f"{self.name}'s happiness is currently {self.happiness}")
    print(f"{self.name}'s hunger is now  {self.hunger}")

x = input("What is your pet's name?")
x = pet(f"{x}", 0, True, 10)
x.check()

while x.life:
    isitem = False
    while not isitem:
        choice = input("\n What would you like to do with your pet? \n"
        "1: Check your pets stats\n"
        "2: Play with your pet\n "
        "3: Feed your pet\n") 

if choice in ["Check your pets stats", "1", "stats", "check"]:
    x.check()