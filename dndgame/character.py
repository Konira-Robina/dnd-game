from dndgame.dice import roll
from dndgame.entity import Entity


RACE_BONUSES: dict[str, dict[str, int]] = {
    "Human": {
        "STR": 1,
        "DEX": 1,
        "CON": 1,
        "INT": 1,
        "WIS": 1,
        "CHA": 1,
    },
    "Elf": {
        "DEX": 2,
    },
    "Dwarf": {
        "CON": 2,
    },
    "Halfling": {
        "DEX": 2,
    },
}


class Character(Entity):
    """Represent a player character in the game."""

    def __init__(self, name: str, race: str, base_hp: int) -> None:
        """Initialize a player character.

        Args:
            name: The character's name.
            race: The character's race.
            base_hp: The character's starting hit points.
        """
        super().__init__(name, base_hp)
        self.race: str = race

    def roll_stats(self) -> None:
        """Roll and assign the character's ability scores."""
        print("Rolling stats...\n")
        stats = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]

        for stat in stats:
            print(f"Rolling {stat}...")
            self.stats[stat] = roll(6, 3)

        self.max_hp = self.base_hp + self.get_modifier("CON")
        self.hp = self.max_hp

    def apply_racial_bonuses(self) -> None:
        """Apply the ability bonuses associated with the character's race."""
        bonuses = RACE_BONUSES.get(self.race, {})

        for stat, bonus in bonuses.items():
            self.stats[stat] += bonus