class Entity:
    """Represent a general game entity."""

    def __init__(self, name: str, base_hp: int) -> None:
        """Initialize an entity.

        Args:
            name: The entity's name.
            base_hp: The entity's starting hit points.
        """
        self.name: str = name
        self.stats: dict[str, int] = {}
        self.base_hp: int = base_hp
        self.hp: int = 0
        self.max_hp: int = 0
        self.level: int = 1
        self.armor_class: int = 10

    def get_modifier(self, stat: str) -> int:
        """Calculate an ability modifier.

        Args:
            stat: The ability score to calculate the modifier for.

        Returns:
            The calculated ability modifier.
        """
        return (self.stats[stat] - 10) // 2