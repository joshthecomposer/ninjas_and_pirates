import random

class Ninja:

    home_base_health = 100

    def __init__( self , name ):
        self.name = name
        self.damage = 6.6
        self.speed = 10
        self.health = 100
        self.armour = 0.35
        self.crit_chance = 27
        self.crit_damage = self.damage * 1.2


    def show_stats( self ):
        print("=========================")
        print(f"Name: {self.name}\nDamage: {self.damage}\nSpeed: {self.speed}\nHealth: {self.health}\nArmour: {self.armour}\nCrit Chance: {self.crit_chance}\nFaction Base Health: {Ninja.home_base_health}")
        print("=========================")

    def attack(self , pirate):

        if (self.health <= 0):
            pirate.win()
            return self

        for i in range(self.speed, 0, -1):
            crit_roll = random.randint(1, 100)
            if crit_roll <= self.crit_chance:
                pirate.health -= ((self.crit_damage) - (self.crit_damage * pirate.armour))
            else:
                pirate.health -= (self.damage - (self.damage * pirate.armour))
            i -= 1
        return self

    @staticmethod
    def start_combat(ninja, pirate):
        while ninja.health >= 0 and pirate.health > 0:
            ninja.attack(pirate)
            pirate.attack(ninja)

    @classmethod
    def damage_home_base(cls):
        cls.home_base_health -=1