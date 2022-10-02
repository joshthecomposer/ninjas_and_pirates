import random

class Pirate:

    home_base_health = 100

    def __init__( self , name ):
        self.name = name
        self.damage = 13.9
        self.speed = 4
        self.health = 100
        self.armour = 0.52
        self.crit_chance = 5
        self.crit_damage = self.damage * 1.5


    def show_stats( self ):
        print("=========================")
        print(f"Name: {self.name}\nDamage: {self.damage}\nSpeed: {self.speed}\nHealth: {self.health}\nArmour: {self.armour}\nCrit chance: {self.crit_chance}\nFaction Base Health: {Pirate.home_base_health}")
        print("=========================")

    def attack ( self , ninja ):
        if self.health <= 0:
            return self
            
        for i in range(self.speed, 0, -1):
            crit_roll = random.randint(1, 100)
            if crit_roll <= self.crit_chance:
                ninja.health -= ((self.crit_damage) - (self.crit_damage * ninja.armour))
            else:
                ninja.health -= (self.damage - (self.damage * ninja.armour))
            i -= 1  
        return self
    
    @classmethod
    def damage_home_base(cls):
        cls.home_base_health -=1