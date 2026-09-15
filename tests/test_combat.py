from unittest.mock import patch

from dndgame.character import Character
from dndgame.combat import Combat
from dndgame.enemy import Enemy


def create_player() -> Character:
    """Create a player with predictable stats for testing."""
    player = Character("Robina", "Human", 10)
    player.stats = {
        "STR": 12,
        "DEX": 14,
        "CON": 12,
        "INT": 10,
        "WIS": 10,
        "CHA": 10,
    }
    player.hp = 10
    player.max_hp = 10
    return player


def create_goblin() -> Enemy:
    """Create a goblin with predictable stats for testing."""
    return Enemy(
        "Goblin",
        5,
        10,
        {
            "STR": 10,
            "DEX": 10,
            "CON": 10,
            "INT": 8,
            "WIS": 8,
            "CHA": 8,
        },
    )


def test_enemy_creation() -> None:
    """Test that an enemy is created with the correct values."""
    enemy = create_goblin()

    assert enemy.name == "Goblin"
    assert enemy.base_hp == 5
    assert enemy.hp == 5
    assert enemy.max_hp == 5
    assert enemy.armor_class == 10
    assert enemy.stats["STR"] == 10
    assert enemy.stats["DEX"] == 10


def test_enemy_default_stats() -> None:
    """Test that an enemy receives default ability scores."""
    enemy = Enemy("Goblin", 5)

    assert enemy.stats["STR"] == 10
    assert enemy.stats["DEX"] == 10
    assert enemy.stats["CON"] == 10
    assert enemy.stats["INT"] == 10
    assert enemy.stats["WIS"] == 10
    assert enemy.stats["CHA"] == 10


def test_roll_initiative_player_first() -> None:
    """Test initiative when the player rolls higher."""
    player = create_player()
    enemy = create_goblin()
    combat = Combat(player, enemy)

    with patch("dndgame.combat.roll", side_effect=[15, 10]):
        order = combat.roll_initiative()

    assert order == [player, enemy]


def test_roll_initiative_enemy_first() -> None:
    """Test initiative when the enemy rolls higher."""
    player = create_player()
    enemy = create_goblin()
    combat = Combat(player, enemy)

    with patch("dndgame.combat.roll", side_effect=[10, 15]):
        order = combat.roll_initiative()

    assert order == [enemy, player]


def test_roll_initiative_player_wins_tie() -> None:
    """Test that the player goes first when initiative is tied."""
    player = create_player()
    enemy = create_goblin()
    combat = Combat(player, enemy)

    with patch("dndgame.combat.roll", side_effect=[10, 10]):
        order = combat.roll_initiative()

    assert order == [player, enemy]


def test_attack_hits() -> None:
    """Test that a successful attack deals damage."""
    player = create_player()
    enemy = create_goblin()
    combat = Combat(player, enemy)

    with patch("dndgame.combat.roll", side_effect=[20, 4]):
        damage = combat.attack(player, enemy)

    assert damage == 4
    assert enemy.hp == 1


def test_attack_misses() -> None:
    """Test that a missed attack deals no damage."""
    player = create_player()
    enemy = create_goblin()
    combat = Combat(player, enemy)

    with patch("dndgame.combat.roll", return_value=1):
        damage = combat.attack(player, enemy)

    assert damage == 0
    assert enemy.hp == 5


def test_attack_does_not_reduce_hp_below_zero() -> None:
    """Test that damage cannot reduce HP below zero."""
    player = create_player()
    enemy = create_goblin()
    enemy.hp = 2
    combat = Combat(player, enemy)

    with patch("dndgame.combat.roll", side_effect=[20, 6]):
        damage = combat.attack(player, enemy)

    assert damage == 6
    assert enemy.hp == 0


def test_combat_is_not_over_when_both_are_alive() -> None:
    """Test that combat continues while both entities have HP."""
    player = create_player()
    enemy = create_goblin()
    combat = Combat(player, enemy)

    assert combat.is_over() is False


def test_combat_is_over_when_enemy_dies() -> None:
    """Test that combat ends when the enemy reaches zero HP."""
    player = create_player()
    enemy = create_goblin()
    enemy.hp = 0
    combat = Combat(player, enemy)

    assert combat.is_over() is True


def test_combat_is_over_when_player_dies() -> None:
    """Test that combat ends when the player reaches zero HP."""
    player = create_player()
    player.hp = 0
    enemy = create_goblin()
    combat = Combat(player, enemy)

    assert combat.is_over() is True