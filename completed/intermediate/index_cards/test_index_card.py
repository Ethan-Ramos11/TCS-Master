import unittest
from index_card import Index_Card, Index_Card_Set


class TestIndexCard(unittest.TestCase):
    def test_card_creation(self):
        """Test creating a new index card"""
        card = Index_Card("Front", "Back")
        self.assertEqual(card.name, "Front")
        self.assertEqual(card.value, "Back")

    def test_card_update(self):
        """Test updating card name and value"""
        card = Index_Card("Front", "Back")
        self.assertTrue(card.update_name("New Front"))
        self.assertEqual(card.name, "New Front")
        self.assertTrue(card.update_value("New Back"))
        self.assertEqual(card.value, "New Back")

    def test_card_equality(self):
        """Test card equality comparison"""
        card1 = Index_Card("Front", "Back")
        card2 = Index_Card("Front", "Back")
        card3 = Index_Card("Different", "Back")
        self.assertEqual(card1, card2)
        self.assertNotEqual(card1, card3)


class TestIndexCardSet(unittest.TestCase):
    def test_add_card(self):
        """Test adding cards to a set"""
        card_set = Index_Card_Set("Test Set")
        self.assertTrue(card_set.add_card("Card 1", "Value 1"))
        self.assertFalse(card_set.add_card("Card 1", "Value 1"))  # Duplicate

    def test_remove_card(self):
        """Test removing cards from a set"""
        card_set = Index_Card_Set("Test Set")
        card = Index_Card("Card 1", "Value 1")
        card_set.add_card("Card 1", "Value 1")
        self.assertTrue(card_set.remove_card(card))
        self.assertFalse(card_set.remove_card(card))  # Already removed

    def test_save_and_load(self):
        """Test saving and loading card sets"""
        card_set = Index_Card_Set("Test Set")
        card_set.add_card("Card 1", "Value 1")
        card_set.add_card("Card 2", "Value 2")

        # Save to file
        filename = "test_set.json"
        card_set.upload_to_file(filename)

        # Load from file
        loaded_set = Index_Card_Set.load_from_file(filename)
        self.assertEqual(loaded_set.set_name, "Test Set")
        self.assertEqual(len(loaded_set.cards), 2)

        # Clean up
        import os
        os.remove(filename)


if __name__ == '__main__':
    unittest.main()
