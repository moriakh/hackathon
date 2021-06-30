from cards import Unit, Spell, User

red_belt_ninja = Unit('Red Belt Ninja', 3, 3, 4)
black_belt_ninja = Unit('Black Belt Ninja', 4, 5, 4)

hard_algorithm = Spell('Hard Algorithm', 2, "Increase target's resilience by 3 points", 'resilience', 3)
unhandled_promise = Spell('Unhandled Promise', 2, "Decrease target's resilience by 2 points",'resilience', -2)
pair_programming = Spell('Pair Programming', 3, "Increase target's power by 2", 'power', 2)

BeaverWarrior = Unit('Beaver Warrior', 2, 2, 3)
DarkMagician = Unit('Dark Magician', 4, 5, 3)

def tablero():
    side_a = []
    side_b = []
    # un diccionario para 
    pass

def status():
    pass

def main():
    name_user_a = input('Insert your nickname: ')
    name_user_b = input("Insert your opponent's nickname: ")
    user_a = User(name_user_a)
    user_b = User(name_user_b)
    game = True
    while True:
        if game:
            return
        else:
            break


# __Increase / Decrease__ " the target's "  __resilience / power__ " by " __number__

# feature adicional, crear clase de jugadores
# feature adicional, crear tablero y cartas que entran y salen del tablero

# turno 1
print('Turno 1')
print(f'{red_belt_ninja.name} resilience: {red_belt_ninja.resilience}')
hard_algorithm.effect(red_belt_ninja)
print(f'{red_belt_ninja.name} resilience: {red_belt_ninja.resilience}')

# turno 2
print('\nTurno 2')
print(f'{black_belt_ninja.name} resilience: {black_belt_ninja.resilience}')
unhandled_promise.effect(black_belt_ninja)
print(f'{black_belt_ninja.name} resilience: {black_belt_ninja.resilience}')

# turno 3
print('\nTurno 3')
print(f'{red_belt_ninja.name} power: {red_belt_ninja.power}')
pair_programming.effect(red_belt_ninja)
print(f'{red_belt_ninja.name} power: {red_belt_ninja.power}')

red_belt_ninja.attack(black_belt_ninja)



import pdb; pdb.set_trace()