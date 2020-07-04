class CoffeeMachine:
    
    def __init__(self, water=400, milk=540, coffee_beans=120, disposable_cups=9, money=550):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.disposable_cups = disposable_cups
        self.money = money
    
    def update_stock(self, coffee_type):
        for supply in coffee_type:
          setattr(self, supply, getattr(self, supply) - coffee_type[supply])
            
    def can_make_coffee(self, kind):
        answers = []
        
        for supply in kind:
          answers.append(getattr(self, supply) - kind[supply] < 0)
    
        return (not True in answers)
        
    def missing_supply(self, coffee_type):
        missing = []

        for supply in coffee_type:
            if getattr(self, supply) - coffee_type[supply] < 0:
                missing.append(supply)

        return ','.join(missing)
    
    def buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        selection = input()
        
        if selection == "back":
            self.run()
        
        espresso = {
            "water": 250,
            "coffee_beans": 16,
            "disposable_cups": 1,
            "money": -4
        }
        
        latte = {
            "water": 350,
            "milk": 75,
            "coffee_beans": 20,
            "disposable_cups": 1,
            "money": -7
        }
        
        cappuccino = {
            "water": 200,
            "milk": 100,
            "coffee_beans": 12,
            "disposable_cups": 1,
            "money": -6
        }
        
        coffees = {
            "1": espresso,
            "2": latte,
            "3": cappuccino
        }
        
        if self.can_make_coffee(coffees[selection]):
            print("I have enough resources, making you a coffee!")
            self.update_stock(coffees[selection])
        else:
            print(f"Sorry, not enough {self.missing_supply(coffees[selection])}!")

    def fill(self):
        print("Write how many ml of water do you want to add:")
        water = int(input())
        print("Write how many ml of milk do you want to add:")
        milk = int(input())
        print("Write how many grams of coffee beans do you want to add:")
        coffee_beans = int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        disposable_cups = int(input())
        
        supplies = {
            "water": water,
            "milk": milk,
            "coffee_beans": coffee_beans,
            "disposable_cups": disposable_cups,
        }
        
        for supply, qty in supplies.items():
            setattr(self, supply, getattr(self, supply) + qty)
        
    def take(self):
        print("I gave you $", self.money)
        self.money = 0
        
    def remaining(self):
        print("The coffee machine has:")
        print(self.water, "of water")
        print(self.milk, "of milk")
        print(self.coffee_beans,"of coffee beans")
        print(self.disposable_cups, "of disposable cups")
        print(self.money, "of money")

    def run(self):
        run_action = {
            "buy": self.buy,
            "fill": self.fill,
            "take": self.take,
            "remaining": self.remaining,
            "exit": quit
        }
        
        print("Write action (buy, fill, take, remaining, exit):")
        selection = input()
        
        run_action[selection]()
        self.run()
    
coffe_machine = CoffeeMachine()
coffe_machine.run()
    
