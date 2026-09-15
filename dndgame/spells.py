# type: ignore
class Spell:
    def __init__(self, name: str, level: int, school: str, spell_power: int):
        self.name = name
        self.level = level
        self.school = school
        self.spell_power = spell_power

    def cast(self, caster, target):
        pass


class SpellBook:
    """Manage a collection of spells."""

    def __init__(self) -> None:
        self.spells: list[Spell] = []

    def add_spell(self, spell: Spell) -> None:
        """Add a spell to the spellbook."""
        self.spells.append(spell)

    def get_available_spells(self, spell_level: int) -> list[Spell]:
        """Return spells available at the given spell level."""
        return [spell for spell in self.spells if spell.level <= spell_level]
