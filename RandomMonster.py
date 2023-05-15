import random
import time

monsters = [
    "Goliath",
    "Kraken",
    "Wraith",
    "Behemoth",
    "Gorgon",
    "Elder Kraken",
    "Meteor Goliath",
    "Glacial Behemoth",
]

perks = [
    [
        "Brawler",
        "Enhanced Senses",
        "Fast Climber",
        "Haste",
        "Heavy Armor",
        "Hunger",
        "Leg Breaker",
        "Savage Nature",
        "Unstoppable",
    ],
    [
        "Aggravated Wounds",
        "Crippling Attack",
        "Endurance",
        "Feral Instincts",
        "Fly Swatter",
        "Heavy Hitter",
        "Insatiable Hunger",
        "Mutated Claw",
        "Mutated Haste",
        "Mutated Recovery",
        "Mutated Senses",
        "Scale Armor",
        "Speed Climber",
    ],
    [
        "Brute Force",
        "Deadly Brawler",
        "Evolved Claw",
        "Evolved Haste",
        "Evolved Recovery",
        "Ferocious Bloodlust",
        "Grounder",
        "Infectious Wounds",
        "Paralyzing Attack",
        "Plated Armor",
        "Unending Endurance",
        "Unkillable",
    ],
]

# Choose monster at random
def choose_monster():
    return random.choice(monsters)


# Generate perks at random
def generate_perks():
    return (random.choice(perk) for perk in perks)


def build_class():
    steps = (choose_monster, generate_perks)
    return generate_output(*[step() for step in steps])


def generate_output(monster, perks):
    output = (
        f"You will play as the {monster.upper()}",
        " with the following perks:",
        f"  🔶 {monster}",
    )
    output += tuple((f" ▫️{perk}") for perk in perks)
    return output


def main():
    print(
        'Make this randomizer yourself by clicking the card on the top right!\nCheck out "ML Mindset with Jason Hertzog" on YouTube!\nStarting in:'
    )
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)

    output = build_class()
    print("\n".join(output))


if __name__ == "__main__":
    main()
