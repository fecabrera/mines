from copy import deepcopy


class BaseEngine(object):
    _size_x: int
    _size_y: int
    _board: list[list[int]]
    _n_mines: int

    @property
    def x(self):
        return self._size_x

    @property
    def y(self):
        return self._size_y

    @property
    def mine_count(self):
        return self._n_mines

    def __init__(self, x: int, y: int = None):
        self._size_x = x
        self._size_y = y or x
        self.reset_board()

    def reset_board(self):
        """
        Reset the board to an empty state
        """
        self._board = [[0 for _ in range(self.y)] for _ in range(self.x)]
        self._n_mines = 0

    def place_mine(self, x: int, y: int):
        """
        Place a mine on the board

        :param x:
        :param y:
        """
        raise NotImplementedError

    def remove_mine(self, x: int, y: int):
        """
        Remove a mine from the board

        :param x:
        :param y:
        """
        raise NotImplementedError

    def place_mines(self, *mines: tuple[int, int]):
        """
        Place multiple mines on the board

        :param mines:
        """
        for x, y in mines:
            self.place_mine(x, y)

    def remove_mines(self, *mines: tuple[int, int]):
        """
        Remove multiple mines from the board

        :param mines:
        """
        for x, y in mines:
            self.remove_mine(x, y)

    def get_cell(self, x: int, y: int):
        """
        Get the value of a cell

        :param x:
        :param y:
        :return:
        """
        assert 0 <= x < self.x
        assert 0 <= y < self.y

        return self._board[x][y]

    def _cell_is_mine(self, x: int, y: int):
        """
        Check if the cell is a mine

        :param x:
        :param y:
        :return:
        """
        return self.get_cell(x, y) is None

    def _make_mine(self, x: int, y: int):
        self._board[x][y] = None

    def _reset_cell(self, x: int, y: int):
        self._board[x][y] = 0

    def _place_mine(self, x: int, y: int):
        self._make_mine(x, y)
        self._n_mines += 1

    def _remove_mine(self, x: int, y: int):
        self._reset_cell(x, y)
        self._n_mines -= 1

    def get_board(self):
        """
        Get the current state of the board

        :return:
        """
        return deepcopy(self._board)

    def __len__(self):
        """
        Get the number of mines on the board

        :return:
        """
        return self.mine_count

    def __getitem__(self, key: tuple[int, int]):
        """
        Get the value of a cell

        :param key:
        :return:
        """
        assert len(key) == 2

        x, y = key
        return self.get_cell(x, y)
