from dndgame.character import Character
from dndgame.dice import roll


def get_choice(prompt: str, valid_choices: list[str]) -> str:
    """Get a valid choice from the user.

    Args:
        prompt: The message displayed to the user.
        valid_choices: The choices accepted as valid input.

    Returns:
        A valid choice entered by the user.
    """
    while True:
        choice = input(prompt).strip()

        if choice in valid_choices:
            return choice

        print(
            f"Invalid choice. Please enter one of: "
            f"{', '.join(valid_choices)}."
        )


def create_character() -> Character:
    """Create a character by collecting the player's choices.

    Returns:
        A newly created and initialized character.
    """
    print("Welcome to D&D Adventure!")
    name = input("Enter your character's name: ").strip()

    print("\nChoose your race:")
    print("1. Human (+1 to all stats)")
    print("2. Elf (+2 DEX)")
    print("3. Dwarf (+2 CON)")
    print("4. Halfling (+2 DEX)")

    race_choice = get_choice(
        "Enter choice (1-4): ",
        ["1", "2", "3", "4"],
    )

    print("\n")

    races = ["Human", "Elf", "Dwarf", "Halfling"]
    race = races[int(race_choice) - 1]

    character = Character(name, race, 10)
    character.roll_stats()
    character.apply_racial_bonuses()

    return character


def display_character(character: Character) -> None:
    """Display the character's information.

    Args:
        character: The character whose information will be displayed.
    """
    print(f"\n{character.name} the {character.race}")
    print("\nStats:")

    for stat, value in character.stats.items():
        modifier = character.get_modifier(stat)
        print(f"{stat}: {value} ({'+' if modifier >= 0 else ''}{modifier})")

    print(f"\nHP: {character.hp}")


def simple_combat(player: Character) -> bool:
    """Run a simple combat encounter against a goblin.

    Args:
        player: The player's character.

    Returns:
        True if the player defeats the goblin, otherwise False.
    """
    print("\nA goblin appears!")
    goblin_hp = 5

    while goblin_hp > 0:
        print(f"\nGoblin HP: {goblin_hp}")
        print("\nYour turn!")
        print("1. Attack")
        print("2. Run away")
        print()

        choice = get_choice(
            "What do you do? ",
            ["1", "2"],
        )

        if choice == "1":
            attack = roll(20, 1)

            if attack >= 10:
                damage = roll(4, 1)
                goblin_hp -= damage
                print(f"You hit for {damage} damage!")
            else:
                print("You missed!")

        elif choice == "2":
            return False

    return True


def main() -> None:
    """Run the D&D game."""
    player = create_character()

    while True:
        print("\nWhat would you like to do?")
        print("1. Fight a goblin")
        print("2. View character")
        print("3. Quit")

        choice = get_choice(
            "Enter choice (1-3): ",
            ["1", "2", "3"],
        )

        if choice == "1":
            victory = simple_combat(player)

            if victory:
                print("You defeated the goblin!")
            elif player.hp <= 0:
                print("Game over!")
            else:
                print("You ran away!")

        elif choice == "2":
            display_character(player)

        elif choice == "3":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()