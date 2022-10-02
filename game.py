from classes.ninja import Ninja
from classes.pirate import Pirate

ninja = Ninja("Joshua")
pirate = Pirate("Brian")

while Ninja.home_base_health > 0 and Pirate.home_base_health > 0:
    if ninja.health <= 0:
        print(f"{pirate.name} Won! Now {pirate.name} is killing {ninja.name}'s base!")
        Ninja.damage_home_base()
        ninja.health = 100

    elif pirate.health <= 0:
        print(f"{ninja.name} Won! Now {ninja.name} is killing {pirate.name}'s base!")
        Pirate.damage_home_base()
        pirate.health = 100

    else:        
        Ninja.start_combat(ninja, pirate)

print(f"In the end, the ninja base has {Ninja.home_base_health} health")
print(f"In the end, the pirate base has {Pirate.home_base_health} health")