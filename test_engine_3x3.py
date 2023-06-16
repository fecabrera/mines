from unittest import TestCase
from engine import Engine


class TestEngine3x3(TestCase):
    def setUp(self):
        self.engine = Engine(3)

    def test_get_cell(self):
        self.engine.place_mine(0, 0)
        self.engine.place_mine(1, 1)
        self.engine.place_mine(0, 2)

        self.assertEqual(self.engine.get_cell(0, 0), self.engine._board[0][0])
        self.assertEqual(self.engine.get_cell(1, 1), self.engine._board[1][1])
        self.assertEqual(self.engine.get_cell(0, 2), self.engine._board[0][2])
        self.assertEqual(self.engine.get_cell(0, 1), self.engine._board[0][1])
        self.assertEqual(self.engine.get_cell(1, 0), self.engine._board[1][0])
        self.assertEqual(self.engine.get_cell(1, 2), self.engine._board[1][2])
        self.assertEqual(self.engine.get_cell(2, 0), self.engine._board[2][0])
        self.assertEqual(self.engine.get_cell(2, 1), self.engine._board[2][1])
        self.assertEqual(self.engine.get_cell(2, 2), self.engine._board[2][2])

    def test_increase_cell(self):
        self.engine._increase_cell(0, 0)
        self.assertEqual(self.engine.get_cell(0, 0), 1)

    def test_decrease_cell(self):
        self.engine._decrease_cell(0, 0)
        self.assertEqual(self.engine.get_cell(0, 0), -1)

    def test_place_mine(self):
        self.engine.place_mine(1, 1)
        self.assertEqual(self.engine.mine_count(), 1)
        self.assertEqual(self.engine.get_board(), [
            [1, 1, 1],
            [1, None, 1],
            [1, 1, 1],
        ])

        self.engine.place_mine(0, 0)
        self.assertEqual(self.engine.mine_count(), 2)
        self.assertEqual(self.engine.get_board(), [
            [None, 2, 1],
            [2, None, 1],
            [1, 1, 1],
        ])

        self.engine.place_mine(2, 0)
        self.assertEqual(self.engine.mine_count(), 3)
        self.assertEqual(self.engine.get_board(), [
            [None, 2, 1],
            [3, None, 1],
            [None, 2, 1],
        ])

    def test_remove_mine(self):
        self.engine.place_mine(0, 0)
        self.engine.place_mine(1, 1)
        self.engine.place_mine(2, 0)

        self.engine.remove_mine(1, 1)
        self.assertEqual(self.engine.mine_count(), 2)
        self.assertEqual(self.engine.get_board(), [
            [None, 1, 0],
            [2, 2, 0],
            [None, 1, 0],
        ])

        self.engine.remove_mine(0, 0)
        self.assertEqual(self.engine.mine_count(), 1)
        self.assertEqual(self.engine.get_board(), [
            [0, 0, 0],
            [1, 1, 0],
            [None, 1, 0],
        ])

        self.engine.remove_mine(2, 0)
        self.assertEqual(self.engine.mine_count(), 0)
        self.assertEqual(self.engine.get_board(), [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ])
