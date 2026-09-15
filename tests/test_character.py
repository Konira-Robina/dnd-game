from dndgame.character import Character


def test_character_creation() -> None:
    """Test that a character is created with the correct attributes."""
    character = Character("Robina", "Elf", 10)

    assert character.name == "Robina"
    assert character.race == "Elf"
    assert character.base_hp == 10
    assert character.level == 1
    assert character.armor_class == 10
    assert character.hp == 0
    assert character.max_hp == 0


def test_get_modifier() -> None:
    """Test ability score modifier calculation."""
    character = Character("Robina", "Human", 10)

    character.stats = {
        "STR": 14,
        "DEX": 9,
    }

    assert character.get_modifier("STR") == 2
    assert character.get_modifier("DEX") == -1


def test_roll_stats() -> None:
    """Test that rolling stats creates all six ability scores."""
    character = Character("Robina", "Human", 10)

    character.roll_stats()

    assert set(character.stats) == {
        "STR",
        "DEX",
        "CON",
        "INT",
        "WIS",
        "CHA",
    }

    assert all(isinstance(value, int) for value in character.stats.values())
    assert character.max_hp > 0
    assert character.hp == character.max_hp


def test_human_racial_bonus() -> None:
    """Test that Humans receive +1 to every ability score."""
    character = Character("Robina", "Human", 10)

    character.stats = {
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHA": 10,
    }

    character.apply_racial_bonuses()

    assert character.stats == {
        "STR": 11,
        "DEX": 11,
        "CON": 11,
        "INT": 11,
        "WIS": 11,
        "CHA": 11,
    }


def test_elf_racial_bonus() -> None:
    """Test that Elves receive +2 DEX."""
    character = Character("Robina", "Elf", 10)

    character.stats = {
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHA": 10,
    }

    character.apply_racial_bonuses()

    assert character.stats["STR"] == 10
    assert character.stats["DEX"] == 12


def test_dwarf_racial_bonus() -> None:
    """Test that Dwarves receive +2 CON."""
    character = Character("Robina", "Dwarf", 10)

    character.stats = {
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHA": 10,
    }

    character.apply_racial_bonuses()

    assert character.stats["CON"] == 12
    assert character.stats["DEX"] == 10


def test_halfling_racial_bonus() -> None:
    """Test that Halflings receive +2 DEX."""
    character = Character("Robina", "Halfling", 10)

    character.stats = {
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHA": 10,
    }

    character.apply_racial_bonuses()

    assert character.stats["STR"] == 10
    assert character.stats["DEX"] == 12