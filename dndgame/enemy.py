from dndgame.entity import Entity


class Enemy(Entity):
    """Represent an enemy in combat."""

    def __init__(
        self,
        name: str,
        base_hp: int,
        armor_class: int = 10,
        stats: dict[str, int] | None = None,
    ) -> None:
        """Initialize an enemy.

        Args:
            name: The enemy's name.
            base_hp: The enemy's starting hit points.
            armor_class: The enemy's armor class.
            stats: The enemy's ability scores.
        """
        super().__init__(name, base_hp)
        self.armor_class = armor_class
        self.max_hp = base_hp
        self.hp = base_hp
        self.stats = stats or {
            "STR": 10,
            "DEX": 10,
            "CON": 10,
            "INT": 10,
            "WIS": 10,
            "CHA": 10,
        }