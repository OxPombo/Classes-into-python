class Monster():
    
    # attributes - variables
    health = 100
    energy = 80

    def attack(self, dam):
        print(f'{dam} was applied to the player!!!')
        if dam > 30 and dam < 100:
            print("That's just low damge")
        
        elif dam >= 100 and dam < 300:
            print("That's a medium damage")

        elif dam > 300 and dam < 1000:
            print("OMG, you just died :(")
        
        else:
            print("You didn't get hurted at all")

    def move(self, spd):
        print(f'The monster has a speed of {spd}...')

monster_0 = Monster()
monster_1 = Monster()
monster_2 = Monster()

monster_0.attack(40)
monster_0.move(50)
print(' ')
monster_1.attack(100)
monster_1.move(80)
print(' ')
monster_2.attack(500)
monster_2.move(400)