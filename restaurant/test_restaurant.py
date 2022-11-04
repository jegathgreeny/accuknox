import unittest

from restaurant import find_top_foods, unique_orders


class OrdersTestCase(unittest.TestCase):
    """Tests for the "restaurant.py"."""

    def test_duplicate_values(self):
        """Do repetitive food orders exist."""
        the_log = {
            1: [["a", "b", "c"]],
            2: [["d", "e", "f"]],
            3: [["a", "c", "g"], ["a", "c", "g"]],
            4: [["h", "j", "k"], ["r", "s", "v"]],
            5: [["l", "m", "n"]],
            6: [["l", "j", "q"]],
        }

        answer = unique_orders(the_log)
        self.assertEqual(answer, "error")

    def test_return_only_three_values(self):
        """check if correct answers are returned"""

        the_log = {
            1: [["a", "b", "c"]],
            2: [["d", "e", "f"]],
            3: [["a", "c", "g"]],
            4: [["a", "c", "g"]],
            5: [["h", "j", "k"]],
            6: [["l", "m", "n"]],
        }

        answer = len(find_top_foods(the_log))
        self.assertEqual(answer, 3)

    def test_empty_orders(self):
        """run no matter even if there are empty orders"""
        the_log = {
            1: [["a", "b", "c"]],
            2: [["d", "e", "f"]],
            3: [[]],
            4: [["a"]],
            5: [["h", "j", "k"]],
            6: [["l", "m", "n"]],
        }

        answer = find_top_foods(the_log)
        self.assertIn("a", answer)

    def test_correct_food(self):
        """check if a expected answer is in the dictionary"""

        the_log = {
            1: [["a", "b", "c"]],
            2: [["d", "e", "f"]],
            3: [["a", "c", "g"]],
            4: [["a", "c", "g"]],
            5: [["h", "j", "k"]],
            6: [["l", "m", "n"]],
        }

        answer = find_top_foods(the_log)
        self.assertIn("a", answer)


if __name__ == "__main__":
    unittest.main()
