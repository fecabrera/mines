from unittest import TestCase
from engine import AutoUpdateEngine


class TestAutoUpdateEngine3x3(TestCase):
    def setUp(self):
        self.engine = AutoUpdateEngine(3)

    def test_place_mine_out_of_bounds(self):
        with self.assertRaises(AssertionError):
            self.engine.place_mine(3, 3)

    def test_remove_mine_out_of_bounds(self):
        with self.assertRaises(AssertionError):
            self.engine.remove_mine(3, 3)

    def test_place_and_remove_mine(self):
        self.engine.place_mine(0, 0)
        self.assertEqual(self.engine._board, [[None, 1, 0], [1, 1, 0], [0, 0, 0]])
        self.assertEqual(self.engine.mine_count, 1)

        self.engine.remove_mine(0, 0)
        self.assertEqual(self.engine._board, [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        self.assertEqual(self.engine.mine_count, 0)

    def test_place_mines(self):
        self.engine.place_mines((0, 0), (1, 1), (2, 2))
        self.assertEqual(self.engine._board, [[None, 2, 1], [2, None, 2], [1, 2, None]])
        self.assertEqual(self.engine.mine_count, 3)

    def test_get_cell(self):
        self.engine.place_mines((0, 0), (1, 1), (2, 2))

        for x in range(self.engine.x):
            for y in range(self.engine.y):
                self.assertEqual(self.engine.get_cell(x, y), self.engine._board[x][y])

    def test_getitem(self):
        self.engine.place_mines((0, 0), (1, 1), (2, 2))

        for x in range(self.engine.x):
            for y in range(self.engine.y):
                self.assertEqual(self.engine[x, y], self.engine._board[x][y])

    def test_get_board(self):
        self.engine.place_mines((0, 0), (1, 1), (2, 2))
        self.assertEqual(self.engine.get_board(), self.engine._board)

    def test_len(self):
        self.assertEqual(len(self.engine), 0)
        self.engine.place_mines((0, 0), (1, 1), (2, 2))
        self.assertEqual(len(self.engine), 3)
