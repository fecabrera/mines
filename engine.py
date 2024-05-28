from copy import deepcopy


class Engine:
    """
    Engine class to handle the game logic
    """
    _size_x: int
    _size_y: int
    _board: list[list[int]]
    _n_mines: int

    def __init__(self, x: int, y: int = None):
        self._size_x = x
        self._size_y = y or x
        self.reset_board()

    @property
    def x(self):
        return self._size_x
    
    @property
    def y(self):
        return self._size_y

    @property
    def mine_count(self):
        return self._n_mines

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
        assert 0 <= x < self.x
        assert 0 <= y < self.y

        if self._board[x][y] is None:
            return

        self._board[x][y] = None
        self._n_mines += 1

    def place_mines(self, *mines: tuple[int, int]):
        """
        Place multiple mines on the board

        :param mines:
        """
        for x, y in mines:
            self.place_mine(x, y)

    def remove_mine(self, x: int, y: int):
        """
        Remove a mine from the board

        :param x:
        :param y:
        """
        assert 0 <= x < self.x
        assert 0 <= y < self.y

        if self._board[x][y] is not None:
            return

        self._board[x][y] = 0
        self._n_mines -= 1

    def update_cell(self, x: int, y: int):
        """
        Update the cell with the number of mines around it

        :param x:
        :param y:
        """
        assert 0 <= x < self.x
        assert 0 <= y < self.y

        if self._board[x][y] is None:
            return

        self._board[x][y] = 0

        for i in range(x - 1, x + 2):
            if i < 0 or i >= self.x:
                continue

            for j in range(y - 1, y + 2):
                if j < 0 or j >= self.y:
                    continue

                if self._board[i][j] is None:
                    self._board[x][y] += 1

    def update_board(self):
        """
        Update the board with the number of mines around each cell
        """
        for x in range(self.x):
            for y in range(self.y):
                self.update_cell(x, y)

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
