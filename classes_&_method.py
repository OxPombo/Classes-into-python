class Monster:
    def __init__(self, func, name, damage):
        self.func = func
        self.damage = damage
        self.name = name

class Skill:

    def bite(self, name):
        print(f'{name} used bite!')

    def strike(self, name):
        print(f'{name} used strike!')

    def slash(self, name):
        print(f'{name} used slash!')

    def kick(self, name):
        print(f'{name} used strike!')

def a():
    a = print(' ')

monster_bee = Monster(func = Skill().bite, name = 'Bee', damage = 20) #? Skill() could be writed just like skill but you should pass it before, like: skill = Skill()
monster_bee.func(monster_bee.name)
print(f'{monster_bee.name} dealt {monster_bee.damage} damage')

a()
monster_bear = Monster(func = Skill().slash, name = 'Bear', damage = 40)
monster_bear.func(monster_bear.name)
print(f'{monster_bear.name} {monster_bear.damage} damage')

a()
monster_monkey = Monster(func = Skill().slash, name = 'Monkey', damage = 60)
monster_monkey.func(monster_monkey.name)
print(f'{monster_monkey.name} dealt {monster_monkey.damage} damage')

#? Each attribute is assigned by declaring a variable with args for the parameters of the def __init__ method.