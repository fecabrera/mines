from base_engine import BaseEngine


class Engine(BaseEngine):
    """
    Engine class to handle the game logic
    """
    def place_mine(self, x: int, y: int):
        """
        Place a mine on the board

        :param x:
        :param y:
        """
        assert 0 <= x < self.x
        assert 0 <= y < self.y

        if self._cell_is_mine(x, y):
            return

        self._place_mine(x, y)

    def remove_mine(self, x: int, y: int):
        """
        Remove a mine from the board

        :param x:
        :param y:
        """
        assert 0 <= x < self.x
        assert 0 <= y < self.y

        if not self._cell_is_mine(x, y):
            return

        self._remove_mine(x, y)

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


class AutoUpdateEngine(BaseEngine):
    """
    Implements an engine that updates the board automatically every time a mine is placed or removed
    """
    def _increase_around(self, x: int, y: int):
        """
        Increase the number of mines around a cell

        :param x:
        :param y:
        """
        for i in range(x - 1, x + 2):
            if i < 0 or i >= self.x:
                continue

            for j in range(y - 1, y + 2):
                if j < 0 or j >= self.y:
                    continue

                if not self._cell_is_mine(i, j):
                    self._board[i][j] += 1

    def _decrease_around(self, x: int, y: int):
        """
        Decrease the number of mines around a cell

        :param x:
        :param y:
        """
        for i in range(x - 1, x + 2):
            if i < 0 or i >= self.x:
                continue

            for j in range(y - 1, y + 2):
                if j < 0 or j >= self.y:
                    continue

                if not self._cell_is_mine(i, j):
                    self._board[i][j] -= 1

    def place_mine(self, x: int, y: int):
        """
        Place a mine on the board

        :param x:
        :param y:
        """
        assert 0 <= x < self.x
        assert 0 <= y < self.y

        if self._cell_is_mine(x, y):
            return

        self._place_mine(x, y)
        self._increase_around(x, y)

    def remove_mine(self, x: int, y: int):
        """
        Remove a mine from the board

        :param x:
        :param y:
        """
        assert 0 <= x < self.x
        assert 0 <= y < self.y

        if not self._cell_is_mine(x, y):
            return

        self._decrease_around(x, y)
        self._remove_mine(x, y)
