from dndgame.dice import roll
from dndgame.entity import Entity


class Combat:
    """Manage combat between two game entities."""

    def __init__(self, player: Entity, enemy: Entity) -> None:
        """Initialize a combat encounter.

        Args:
            player: The player's entity.
            enemy: The enemy's entity.
        """
        self.player: Entity = player
        self.enemy: Entity = enemy
        self.round: int = 0
        self.initiative_order: list[Entity] = []

    def roll_initiative(self) -> list[Entity]:
        """Roll initiative and determine the combat order.

        Returns:
            Entities ordered from highest to lowest initiative.
        """
        player_init = roll(20, 1) + self.player.get_modifier("DEX")
        enemy_init = roll(20, 1) + self.enemy.get_modifier("DEX")

        if player_init >= enemy_init:
            self.initiative_order = [self.player, self.enemy]
        else:
            self.initiative_order = [self.enemy, self.player]

        return self.initiative_order

    def attack(self, attacker: Entity, defender: Entity) -> int:
        """Perform an attack against a defender.

        Args:
            attacker: The entity making the attack.
            defender: The entity being attacked.

        Returns:
            The damage dealt, or 0 if the attack misses.
        """
        attack_roll = roll(20, 1) + attacker.get_modifier("STR")
        weapon_max_damage = 6

        if attack_roll >= defender.armor_class:
            damage = roll(weapon_max_damage, 1)
            defender.hp = max(0, defender.hp - damage)
            return damage

        return 0

    def is_over(self) -> bool:
        """Check whether either combatant has been defeated.

        Returns:
            True if the player or enemy has 0 HP.
        """
        return self.player.hp <= 0 or self.enemy.hp <= 0