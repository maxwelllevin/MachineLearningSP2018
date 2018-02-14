from unittest import TestCase
from othello_minimax import *

class TestOthelloMinimax(TestCase):

    def setUp(self):
        # This is automatically run before each test
        self.case1 = diagram_to_state(['########',
                                       '########',
                                       '########',
                                       '#######O',
                                       'OOOOOOOO',
                                       'OOOOOOOO',
                                       'OOOOOOOO',
                                       'OOOOOOOO'])
        self.case2 = diagram_to_state(['O#######',
                                       '########',
                                       '########',
                                       '########',
                                       '..#OOOOO',
                                       'OOOOOOOO',
                                       'OOOOOOOO',
                                       'OOOOOOOO'])
        self.case3 = diagram_to_state(['........',
                                       '........',
                                       '........',
                                       '..OO#...',
                                       '........',
                                       '..OOO#O.',
                                       '........',
                                       '........'])
        self.case4 = diagram_to_state(['........',
                                       'O#O##...',
                                       '........',
                                       '........',
                                       '........',
                                       '........',
                                       '........',
                                       'O#......'])

    def test_evaluate_scores_end_game(self):
        self.assertEqual(-1, evaluate(self.case1))

    def test_evaluate_scores_unifinished_game(self):
        self.assertEqual(0.02, evaluate(self.case2))

    def test_minimax_evaluates_state_at_depth_0(self):
        self.assertEqual(-0.04, minimax(self.case3, '#', 0))

    def test_minimax_evaluates_state_at_depth_1(self):
        self.assertEqual(0.03, minimax(self.case3, '#', 1))

    def test_best_move_works_at_depth_1(self):
        self.assertEqual((5, 1), best_move(self.case3, '#', 1))

    def test_best_move_works_at_depth_2(self):
        self.assertEqual((3, 1), best_move(self.case3, '#', 2))

    def test_best_moves_works_at_depth_1_for_O(self):
        self.assertEqual((1, 5), best_move(self.case4, 'O', 1))

    def test_best_moves_works_at_depth_2_for_O(self):
        self.assertEqual((7, 2), best_move(self.case4, 'O', 2))

    def test_best_moves_works_at_depth_3_for_O(self):
        self.assertEqual((1, 5), best_move(self.case4, 'O', 3))