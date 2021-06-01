import unittest
import dice_combos


class TestNumber(unittest.TestCase):
    pass


class TestPair(unittest.TestCase):
    def test_score(self):
        self.assertEqual(dice_combos.pair([1, 3, 6, 3, 6]), 12,
                         'incorrect scoring')
        self.assertEqual(dice_combos.pair([1, 6, 3, 6, 3]), 12,
                         'incorrect scoring')
        self.assertEqual(dice_combos.pair([1, 1, 1, 1, 1]), 2,
                         'incorrect scoring')

    def test_immutable(self):
        throw = [1, 3, 6, 3, 6]
        dice_combos.pair(throw)
        self.assertEqual(throw, [1, 3, 6, 3, 6],
                         'list of dice values was mutated')

    def test_missing(self):
        self.assertEqual(dice_combos.pair([1, 2, 3, 4, 5]), 0,
                         'score for missing combo was not 0')


class TestTwoPair(unittest.TestCase):
    def test_score(self):
        self.assertEqual(dice_combos.two_pair([1, 1, 2, 2, 3]), 6,
                         'incorrect scoring')
        self.assertEqual(dice_combos.two_pair([6, 1, 3, 6, 1]), 14,
                         'incorrect scoring')

    def test_immutable(self):
        throw = [2, 3, 6, 2, 3]
        dice_combos.two_pair(throw)
        self.assertEqual(throw, [2, 3, 6, 2, 3],
                         'list of dice values was mutated')

    def test_missing(self):
        self.assertEqual(dice_combos.two_pair([1, 1, 1, 1, 1]), 0,
                         'score for missing combo was not 0 (four of a kind is not a two pair)')
        self.assertEqual(dice_combos.two_pair([1, 2, 3, 4, 5]), 0,
                         'score for missing combo was not 0')


class TestThreeOfAKind(unittest.TestCase):
    def test_score(self):
        self.assertEqual(dice_combos.three_of_a_kind([1, 3, 6, 3, 3]), 9,
                         'incorrect scoring')
        self.assertEqual(dice_combos.three_of_a_kind([1, 1, 1, 1, 1]), 3,
                         'incorrect scoring')

    def test_immutable(self):
        throw = [1, 3, 6, 3, 3]
        dice_combos.three_of_a_kind(throw)
        self.assertEqual(throw, [1, 3, 6, 3, 3],
                         'list of dice values was mutated')

    def test_missing(self):
        self.assertEqual(dice_combos.three_of_a_kind([1, 2, 3, 4, 5]), 0,
                         'score for missing combo was not 0')


class TestFourOfAKind(unittest.TestCase):
    def test_score(self):
        self.assertEqual(dice_combos.four_of_a_kind([1, 3, 6, 3, 3]), 9,
                         'incorrect scoring')
        self.assertEqual(dice_combos.four_of_a_kind([1, 6, 3, 6, 3]), 12,
                         'incorrect scoring')

    def test_immutable(self):
        throw = [3, 3, 6, 3, 3]
        dice_combos.four_of_a_kind(throw)
        self.assertEqual(throw, [3, 3, 6, 3, 3],
                         'list of dice values was mutated')

    def test_missing(self):
        self.assertEqual(dice_combos.four_of_a_kind([1, 2, 3, 4, 5]), 0,
                         'score for missing combo was not 0')


class TestSmallStraight(unittest.TestCase):
    def test_score(self):
        self.assertEqual(dice_combos.small_straight([1, 3, 2, 5, 4]), 15,
                         'incorrect scoring')
        self.assertEqual(dice_combos.small_straight([5, 4, 3, 2, 1]), 15,
                         'incorrect scoring')

    def test_immutable(self):
        throw = [4, 2, 3, 1, 5]
        dice_combos.small_straight(throw)
        self.assertEqual(throw, [4, 2, 3, 1, 5],
                         'list of dice values was mutated')

    def test_missing(self):
        self.assertEqual(dice_combos.small_straight([6, 2, 3, 4, 5]), 0,
                         'score for missing combo was not 0')


class TestLargeStraight(unittest.TestCase):
    def test_score(self):
        self.assertEqual(dice_combos.large_straight([6, 3, 2, 5, 4]), 20,
                         'incorrect scoring')
        self.assertEqual(dice_combos.large_straight([6, 5, 4, 3, 2]), 20,
                         'incorrect scoring')

    def test_immutable(self):
        throw = [4, 2, 3, 6, 5]
        dice_combos.large_straight(throw)
        self.assertEqual(throw, [4, 2, 3, 6, 5],
                         'list of dice values was mutated')

    def test_missing(self):
        self.assertEqual(dice_combos.large_straight([1, 2, 3, 4, 5]), 0,
                         'score for missing combo was not 0')


class TestFullHouse(unittest.TestCase):
    pass


class TestChance(unittest.TestCase):
    pass


class TestYatzy(unittest.TestCase):
    pass
