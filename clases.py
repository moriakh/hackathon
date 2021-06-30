class Card:
    def __init__(self, name, cost, img):
        self.name = name
        self.cost = cost
        self.img = img
        # self.rarity = rarity
        # self.list = []

    def play(self):
        pass

class Unit(Card):
    def __init__(self, name, cost, img, power, resilience):
        super().__init__(name, cost, img)
        self.power = power
        self.resilience = resilience
        
    def attack(self, unit):
        unit.resilience -= self.power
        self.resilience -= unit.power
            # si resistencia <= 0 sale del tablero
        return self

class Spell(Card):
    def __init__(self, name, cost, img, text, stat, magnitude):
        super().__init__(name, cost, img)
        self.text = text
        self.stat = stat
        self.magnitude = magnitude
        if magnitude >= 0:
            text = "Increase"
        else:
            text = "Decrease"
        self.description = f'{text} the targets {stat} by {abs(magnitude)}'

    def effect(self, unit):
        if self.stat == 'power':
            unit.power += self.magnitude
            # si (unit.power + self.magnitude)<= 0, unit.power = 0
        else:
            unit.resilience += self.magnitude
            # si (unit.resilience + self.magnitude)<= 0, muere
        if self.magnitude >= 0:
            self.icon = "UP"
        else:
            self.icon = "DOWN"
        return self

# class User:
#     def __init__(self, name):
#         self.name = name
#         self.life = 10
#         self.gold = 1

#     def lifes(self):
#         pass
    
    
# import pdb; pdb.set_trace()