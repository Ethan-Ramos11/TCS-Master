from typing import List, Dict, Optional
from ..characters.character import Character


class Battle:
    def start_battle(self) -> None:
        pass

    def end_battle(self) -> None:
        pass

    def get_turn_order(self) -> List[Character]:
        pass

    def execute_turn(self, attacker: Character, defender: Character) -> None:
        pass

    def calculate_damage(self, attacker: Character, defender: Character) -> int:
        pass

    def apply_status_effects(self, character: Character) -> None:
        pass

    def check_battle_end(self) -> bool:
        pass

    def handle_character_death(self, character: Character) -> None:
        pass

    def use_skill(self, user: Character, target: Character, skill_name: str) -> bool:
        pass

    def get_available_skills(self, character: Character) -> List[str]:
        pass

    def add_to_battle_log(self, message: str) -> None:
        pass

    def get_battle_log(self) -> List[str]:
        pass

    def get_battle_state(self) -> Dict:
        pass

    def is_valid_target(self, attacker: Character, target: Character) -> bool:
        pass

    def calculate_rewards(self) -> Dict:
        pass

    def handle_flee_attempt(self, character: Character) -> bool:
        pass

    def get_character_position(self, character: Character) -> int:
        pass

    def update_character_position(self, character: Character, new_position: int) -> None:
        pass

    def get_remaining_enemies(self) -> List[Character]:
        pass

    def get_battle_winner(self) -> Optional[Character]:
        pass

    def is_character_turn(self, character: Character) -> bool:
        pass

    def skip_turn(self, character: Character) -> None:
        pass

    def get_character_stats(self, character: Character) -> Dict:
        pass

    def reset_battle(self) -> None:
        pass
