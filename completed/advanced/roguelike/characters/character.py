class Character:
    def __init__(self):
        self.hp = 100
        self.max_hp = 100
        self.lvl = 1
        self.current_mana = 10
        self.max_mana = 10

        self.attack = 5
        self.defense = 5
        self.speed = 5

        self.crit_chance = .5
        self.status_effects = []
        self.is_alive = True

        self.inventory = []
        self.equipped_items = {
            'weapon': None,
            'armor': None,
            'accessory': None
        }

        self.exp = 0
        self.exp_to_next_level = 100

    
