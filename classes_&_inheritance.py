class Monster():
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy
    
    def attack(self, damage):
        self.damage = damage
        self.attack = self.damage
        self.energy -= 10
        print(f'The monster dealt {self.damage} points of damage')
        
class Scorpion(Monster):
    def __init__(self, poison_damage, sco_health, sco_energy):
        self.poison_damage = poison_damage
        super().__init__(sco_health, sco_energy)
        
    def attack(self):
        self.attack = self.poison_damage
        self.energy -= 20
        print(f'The scorpion dealts {self.poison_damage} points of poison damage...')
        print(f'Hero is now poisoned!')

def a():
    print(' ')

monster = Monster(health = 50, energy = 40)
monster.attack(40)

a()

scorpion = Scorpion(poison_damage = 200, sco_health = 90, sco_energy = 30)
print(scorpion.energy)
scorpion.attack()
print(scorpion.energy)

'''
    #* Explanation:

#? In this project I used inheritance in classes.

#! 1. I created two classes, Monster (Father) and Scorpion (Child).
#! 2. Monster() has the parameters health and energy while Scorpion() have poison_damage, health and energy.
#! 3. We tell to python that Scorpion() is child of Monster() using super().__init__(health, energy).    
    #! 3.1. A other way of doing it is calling the class with dunder method __init__ and passing self to it with the wanted attributes, pretty similar to the super(), otherwise we have to pass self, then it would be something like:
        #? Monster.__init__(self, health, energy).

#! 4. Now the health and energy parameters of Scorpion() go like arguments to health and energy of Monster() and then self.health and self.energy refers those args.
#! 5. I wanted to have a different attack method instead of Monster attack method then I just did it again, although I passed the argument on the monster's attack, I decided to leave it as a parameter for the scorpion itself.
#! 6. Finally, we have a inheritence of Monster() to the Scorpion(), health and energy, calling it where we want like it were from Scorpion() itself.

#? Inheritance is really powerful and now I could have a lot of objects sharing methods and customizing them when I need to.

#* OBS: Classes could have a lot of fathers and a father could have a lot of childs, as well.
'''