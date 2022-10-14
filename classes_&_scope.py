class Hero:
    def __init__(self, persona, damage, monster):
        self.persona = persona
        self.damage = damage
        self.monster = monster

    def attack (self):
        monster.get_damage(hero.damage)

    def change (self):
        if self.persona == 'Physalis':
            self.persona = 'Pipi'

        elif self.persona == 'Pipi':
            self.persona = 'Physalis'

class Monster:
    def __init__(self, health):
        self.health = health

    def get_damage(self, amount):
        self.health -= amount

monster = Monster(health = 100)

hero = Hero(persona = 'Physalis',damage = 50, monster = monster)

print(monster.health)

hero.attack()

print(monster.health)

print(hero.persona)
hero.change()
print(hero.persona)
hero.change()
print(hero.persona)
hero.change()
print(hero.persona)