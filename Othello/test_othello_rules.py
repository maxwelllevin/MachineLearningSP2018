from unittest import TestCase
from othello_rules import *


class TestOthelloRules(TestCase):

    def setUp(self):
        # This is automatically run before each test
        self.case1 = diagram_to_state(['...#O...',
                                       '...#....',
                                       '....O...',
                                       '..OO#...',
                                       '........',
                                       '..OOO#O.',
                                       '........',
                                       '........'])
        self.case2 = diagram_to_state(['....O...',
                                       '....#...',
                                       '....#...',
                                       '....#...',
                                       '........',
                                       '........',
                                       '........',
                                       '........'])
        self.case3 = diagram_to_state(['########',
                                       '########',
                                       '########',
                                       '########',
                                       'OOOOOOOO',
                                       'OOOOOOOO',
                                       'OOOOOOOO',
                                       'OOOOOOOO'])
        self.case4 = diagram_to_state(['########',
                                       '########',
                                       '########',
                                       '.#######',
                                       '.OOOOOOO',
                                       'OOOOOOOO',
                                       'OOOOOOOO',
                                       'OOOOOOOO'])

    def test_diagram_to_state_converts_correctly(self):
        correct = [['#', '.'], ['.', 'O']]
        self.assertEqual(correct, diagram_to_state(['#.', '.O']))

    def test_count_pieces_counts_case1_correctly(self):
        counts = count_pieces(self.case1)
        self.assertEqual(4, counts['#'])
        self.assertEqual(8, counts['O'])
        self.assertEqual(52, counts['.'])

    def test_prettify_converts_correctly(self):
        correct = ' 01234567\n' + \
                  '0........0\n' + \
                  '1........1\n' + \
                  '2........2\n' + \
                  '3...#O...3\n' + \
                  '4...O#...4\n' + \
                  '5........5\n' + \
                  '6........6\n' + \
                  '7........7\n' + \
                  ' 01234567\n' + \
                  "{'#': 2, 'O': 2, '.': 60}\n"
        self.assertEqual(correct, prettify(INITIAL_STATE))

    def test_opposite_works_both_ways(self):
        self.assertEqual('O', opposite('#'))
        self.assertEqual('#', opposite('O'))

    def test_flips_finds_correct_pieces(self):
        f = flips(self.case1, 3, 1, '#', 0, 1)
        self.assertEqual(2, len(f))
        self.assertIn((3, 2), f)
        self.assertIn((3, 3), f)

    def test_flips_does_not_find_excess_pieces(self):
        f = flips(self.case1, 0, 2, 'O', 1, 1)
        self.assertEqual([(1, 3)], f)

    def test_flips_does_not_modify_state(self):
        before = prettify(self.case1)
        flips(self.case1, 3, 1, '#', 0, 1)
        self.assertEqual(prettify(self.case1), before)

    def test_flips_something_can_return_true(self):
        self.assertTrue(flips_something(self.case1, 3, 1, '#'))

    def test_flips_something_can_return_false(self):
        self.assertFalse(flips_something(self.case1, 3, 1, 'O'))

    def test_legal_moves_finds_all_moves(self):
        moves = legal_moves(self.case1, '#')
        self.assertEqual(6, len(moves))
        self.assertIn((0, 5), moves)
        self.assertIn((1, 4), moves)
        self.assertIn((3, 1), moves)
        self.assertIn((3, 5), moves)
        self.assertIn((5, 1), moves)
        self.assertIn((5, 7), moves)

    def test_legal_move_offers_pass_when_nothing_can_be_flipped(self):
        moves = legal_moves(self.case2, '#')
        self.assertEqual(['pass'], moves)

    def test_successor_produces_correct_successor(self):
        correct = diagram_to_state(['..OOO...',
                                    '...O....',
                                    '....O...',
                                    '..OO#...',
                                    '........',
                                    '..OOO#O.',
                                    '........',
                                    '........'])
        self.assertEqual(correct, successor(self.case1, (0, 2), 'O'))

    def test_successor_does_not_modify_state(self):
        before = prettify(self.case1)
        successor(self.case1, (5, 1), '#')
        self.assertEqual(before, prettify(self.case1))

    def test_score_counts_correctly(self):
        self.assertEqual(-4, score(self.case1))

    def test_game_over_can_return_true(self):
        self.assertTrue(game_over(self.case3))

    def test_game_over_can_return_false(self):
        self.assertFalse(game_over(self.case1))

    def test_game_over_detects_no_legal_moves(self):
        self.assertTrue(game_over(self.case4))
