
import time
# Construct a base class


class ConstructHero:

    def __init__(self, hitpoints, attack_power, name):
        self.hitpoints = int(hitpoints)
        self.attack_power = int(attack_power)
        self.name = str(name)

    def get_name(self):
        return self.name

    def total_HP(self):
        return self.hitpoints

    def damage(self):
        return self.attack_power

# Select Menu


def character_select():

    character = ""
    while character != "1" and character != "2" and character != "3" and character.lower() != 'wizard' and character.lower() != 'elf' and character.lower() != 'human':
        character = input(
            "Choose your Hero:\n 1) Wizard\n 2) Elf\n 3) Human\n").lower()
    return character

# Char Creation


def construct_hero(character_selected):
    hero = ""
    if character_selected == "1" or character_selected.lower() == 'wizard':
        hero = ConstructHero(70, 150, "Wizard")

    if character_selected == "2" or character_selected.lower() == 'elf':
        hero = ConstructHero(100, 100, "Elf")

    if character_selected == "3" or character_selected.lower() == 'human':
        hero = ConstructHero(150, 20, "Human")

    print(
        f"You've selected: {hero.get_name()}\nHealth: {hero.total_HP()}\nDamage: {hero.damage()}\n")
    return hero


# Spawn ENEMY
ENEMY = ConstructHero(300, 50, "Dragon")

# Spawn CHAMPION
CHAMPION = construct_hero(character_select())

# Capture HP
ENEMY_HP = ENEMY.total_HP()
CHAMPION_HP = CHAMPION.total_HP()

while True:
    # Hero Attack
    ENEMY_HP -= CHAMPION.damage()
    print(f"{CHAMPION.get_name()} damages the {ENEMY.get_name()}!")
    print(f"The {ENEMY.get_name()}'s hitpoints are now: {ENEMY_HP}\n")

    time.sleep(1)

    if ENEMY_HP <= 0:
        print(f"{ENEMY.get_name()} has been slained!\n")
        break

    # ENEMY attack
    CHAMPION_HP -= ENEMY.damage()
    print(f"The {ENEMY.get_name()} strikes back at {CHAMPION.get_name()}")
    print(f"{CHAMPION.get_name()}'s hitpoints are now: {CHAMPION_HP}\n")

    time.sleep(1)

    if CHAMPION_HP <= 0:
        print(f"{CHAMPION.get_name()} has lost the battle!")
        break
