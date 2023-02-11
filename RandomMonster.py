import random

# List of all monsters
monsters = ["Goliath", "Kraken", "Wraith", "Behemoth", "Gorgon", "Elder Kraken", "Meteor Goliath", "Glacial Behemoth"]
# The weak perks
perk1 = ["Brawler", "Enhanced Senses", "Fast Climber", "Haste", "Heavy Armor", "Hunger", "Leg Breaker", "Savage Nature",
         "Unstoppable"]
# The mid perks
perk2 = ["Aggravated Wounds", "Crippling Attack", "Endurance", "Feral Instincts", "Fly Swatter", "Heavy Hitter",
         "Insatiable Hunger", "Mutated Claw", "Mutated Haste", "Mutated Recovery", "Mutated Senses", "Scale Armor",
         "Speed Climber"]
# The strong perks
perk3 = ["Brute Force", "Deadly Brawler", "Evolved Claw", "Evolved Haste", "Evolved Recovery", "Ferocious Bloodlust",
         "Grounder", "Infectious Wounds", "Paralyzing Attack", "Plated Armor", "Unending Endurance", "Unkillable"]


# Choose monster at random
def choose_monster():
    return random.choice(monsters)


# Choose all perks at random, I kind of want to make this something I can choose though
def choose_perks(num_perks):
    if num_perks < 1 or num_perks > 3:
        print("Error: Invalid number of perks. Please choose a number between 1 and 3.")
        return []
    chosen_perks = []
    for i in range(num_perks):
        if i == 0:
            chosen_perks.append(random.choice(perk1))
        elif i == 1:
            chosen_perks.append(random.choice(perk2))
        else:
            chosen_perks.append(random.choice(perk3))
    return chosen_perks


# print it out baby
def print_picks(monster, perks):
    print("You will play as the " + monster.upper() + " with the following perks:\n 🔶" + monster);
    for perk in perks:
        print(" ▫️" + perk)


# do stuff
if __name__ == "__main__":
    monster = choose_monster()
    perks = choose_perks(3)
    print_picks(monster, perks)
