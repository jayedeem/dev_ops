import time
# Construct a base class


class BaseClass:
    #Constructor hp, attackpower, name
    def __init__(self, hp, attkpwr, name):
        self.hp = int(hp)
        self.attkpwr = int(attkpwr)
        self.name = str(name)

    def class_type(self):
        return self.name

    def totalHP(self):
        return self.hp

    def damage(self):
        return self.attkpwr

# Select Menu


def character_select():
    character = ""
    while character != "1" and character != "2" and character != "3" and character.lower() != 'wizard' and character.lower() != 'elf' and character.lower() != 'human':
      if character != "1" or character != "2" or character != "3":
            print("* Invalid Hero Selection *")
      character = input(
          "Choose your Hero:\n 1) Wizard\n 2) Elf\n 3) Human\n")
        
    return character

# Char Creation


def construct_hero(character_selected):
    if character_selected == "1" or character_selected.lower() == 'wizard':
        hero = BaseClass(70, 150, "Wizard")

    if character_selected == "2" or character_selected.lower() == 'elf':
        hero = BaseClass(100, 100, "Elf")
  
    if character_selected == "3" or character_selected.lower() == 'human':
        hero = BaseClass(150, 20, "Human")

    print(f"You've selected: {hero.class_type()}\nHealth: {hero.totalHP()}\nDamage: {hero.damage()}\n")
    return hero


# Spawn enemy
enemy = BaseClass(300, 50, "Dragon")

# Spawn Champion
champion = construct_hero(character_select())

# Capture HP
enemy_hp = enemy.totalHP()
champion_hp = champion.totalHP()

while True:
    # Hero Attack
    enemy_hp -= champion.damage()
    print(f"{champion.class_type()} damages the {enemy.class_type()}!")
    print(f"The {enemy.class_type()}'s hitpoints are now: {enemy_hp}\n")

    time.sleep(2)

    if enemy_hp <= 0:
        print(f"{enemy.class_type()} has been slained!\n")
        print(
            f"The {champion.class_type()} decapitates {enemy.class_type()} as a trophy!")
        break

    # enemy attack
    champion_hp -= enemy.damage()
    print(f"The {enemy.class_type()} strikes back at {champion.class_type()}", )
    print(f"{champion.class_type()}'s hitpoints are now: {champion_hp}\n")

    time.sleep(2)

    if champion_hp <= 0:
        print(f"{champion.class_type()} has lost the battle!")
        print(f"The {enemy.class_type()} devours the {champion.class_type()}\n")
        break
