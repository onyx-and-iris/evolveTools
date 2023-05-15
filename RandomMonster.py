import random
import time
from typing import Iterable

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

perk_lists = [
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
def choose_monster() -> str:
    return random.choice(monsters)


# Generate perks at random
def generate_perks() -> Iterable:
    return (random.choice(perk_list) for perk_list in perk_lists)


def run_build() -> tuple:
    steps = (choose_monster, generate_perks)
    return generate_output(*[step() for step in steps])


def generate_output(monster: str, perks: list) -> tuple:
    output = (
        f"You will play as the {monster.upper()}",
        " with the following perks:",
        f"  🔶 {monster}",
    )
    output += tuple((f" ▫️{perk}") for perk in perks)
    return output


def main():
    print(
        'Generating random monster and perks...'
    )
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)

    output = run_build()
    print("\n".join(output))


if __name__ == "__main__":
    main()
