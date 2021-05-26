import unittest
import dice_combos


class TestPair(unittest.TestCase):
    def test_score(self):
        pair_combo = [1, 3, 6, 3, 6] 
        self.assertEqual(dice_combos.pair(pair_combo), 12,
                         'incorrect scoring')
        self.assertEqual(pair_combo, [1, 3, 6, 3, 6],
                         'list of dice values was mutated')

        self.assertEqual(dice_combos.pair([1, 6, 3, 6, 3]), 12,
                         'incorrect scoring')

    def test_missing(self):
        self.assertEqual(dice_combos.pair([1, 2, 3, 4, 5]), 0,
                         'score for missing combo was not 0')

