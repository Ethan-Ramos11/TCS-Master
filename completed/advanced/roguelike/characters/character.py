import random


class Character:
    def __init__(self, hp: int = 100, mana: int = 10, attack: int = 5,
                 defense: int = 5, speed: int = 5, crit_chance: float = 0.5):
        # Resource stats
        self.max_hp = hp
        self.hp = hp
        self.max_mana = mana
        self.current_mana = mana

        # Combat stats
        self.stats = {
            "attack":  attack,
            "defense": defense,
            "speed": speed,
            "crit_chance": crit_chance
        }

        # Status and progression
        self.lvl = 1
        self.exp = 0
        self.exp_to_next_level = 100
        self.status_effects = {}
        self.is_alive = True

        # Equipment and inventory
        self.inventory = []
        self.equipped_items = {
            'weapon': None,
            'armor': None,
            'accessory': None
        }

    # Combat Functions
    def take_damage(self, amount: int) -> bool:
        """
        Return: True if still alive False otherwise
        """
        if amount < 0:
            return True
        if self.hp - amount <= 0:
            self.hp = 0
            self.is_alive = False
            return False
        else:
            self.hp -= amount
            return True

    def heal(self, amount: int) -> int:
        """TODO: Restore HP up to max_hp, apply healing modifiers"""
        if amount < 0:
            return 0
        if self.hp + amount >= self.max_hp:
            healed_amt = self.max_hp - self.hp
            self.hp = self.max_hp
            return healed_amt
        else:
            self.hp += amount
            return amount

    def attack(self, target: 'Character') -> int:
        """TODO: Calculate damage based on attack stat, handle critical hits"""
        pass

    def use_mana(self, amount: int) -> bool:
        """TODO: Attempt to use mana, return success status"""
        pass

    # Status and Progression
    def gain_exp(self, amount: int) -> bool:
        """TODO: Add experience, handle level ups and stat increases
        Returns True if we level up False otherwise"""
        if amount < 0:
            return False
        if self.lvl >= 100:
            return False
        elif amount + self.exp >= self.exp_to_next_level:
            additional_exp = (amount + self.exp) - self.exp_to_next_level
            self.exp = additional_exp
            self.lvl += 1
            self.exp_to_next_level += 100
            self.update_stats()
            return True
        else:
            self.exp += amount
            return False

    def update_stats(self) -> None:

        self.max_hp += 10
        self.hp += 10
        self.max_mana += 5
        self.current_mana = self.max_mana

        stat_increase = (self.lvl // 2) * 3
        for val in self.stats.values():
            val += stat_increase

    def add_status_effect(self, effect: str) -> None:
        if effect in self.status_effects():
            return
        turns = random.randint(1, 3)
        self.status_effects.append({effect: turns})

    def remove_status_effect(self, effect_name: str) -> None:
        if effect_name in self.status_effects:
            del self.status_effects[effect_name]
    # Equipment Management

    def equip_item(self, item: 'Item') -> bool:
        if self.equipped_items[item.type] != None:
            self.unequip_item(item.type)
        self.equipped_items[item.type] = item

    def unequip_item(self, slot: str) -> 'Item':
        if self.equipped_items == "None":
            return
        self.equipped_items = None

    def add_to_inventory(self, item: 'Item') -> bool:
        if len(self.inventory) == 5:
            return False
        self.inventory.append(item)

    # Utility Functions
    def is_alive(self) -> bool:
        return self.is_alive

    def get_stat(self, stat_name: str) -> int:
        if stat_name not in self.stats:
            return -1
        return self.stats[stat_name]

    def get_equipped_stats(self) -> dict:
        stats = self.stats
        for item in self.equipped_items.values():
            stats[item.type] += item.stat_boost
        return stats

    def save_state(self) -> dict:
        """TODO: Return character's current state for saving"""
        pass

    def load_state(self, state: dict) -> None:
        """TODO: Load character state from saved data"""
        pass

    # Combat Calculations
    def calculate_damage(self, base_damage: int) -> int:
        """TODO: Calculate final damage with modifiers and critical hits"""
        pass

    def calculate_defense(self) -> int:
        """TODO: Return total defense including equipment"""
        pass

    def calculate_speed(self) -> int:
        """TODO: Return total speed including equipment"""
        pass
