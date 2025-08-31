from base_engine import BaseEngine


class AutoUpdateEngine(BaseEngine):
    """Implements an engine that updates the board automatically.
    
    This engine automatically updates the board whenever a mine is
    placed or removed, maintaining accurate mine counts around each cell.
    """
    
    def _increase_around(self, x: int, y: int):
        """Increase the number of mines around a cell.
        
        Args:
            x (int): X coordinate of the cell.
            y (int): Y coordinate of the cell.
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
        """Decrease the number of mines around a cell.
        
        Args:
            x (int): X coordinate of the cell.
            y (int): Y coordinate of the cell.
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
        """Place a mine on the board.
        
        Args:
            x (int): X coordinate of the mine.
            y (int): Y coordinate of the mine.
            
        Raises:
            AssertionError: If coordinates are out of bounds.
        """
        assert 0 <= x < self.x
        assert 0 <= y < self.y

        if self._cell_is_mine(x, y):
            return

        self._place_mine(x, y)
        self._increase_around(x, y)

    def remove_mine(self, x: int, y: int):
        """Remove a mine from the board.
        
        Args:
            x (int): X coordinate of the mine.
            y (int): Y coordinate of the mine.
            
        Raises:
            AssertionError: If coordinates are out of bounds.
        """
        assert 0 <= x < self.x
        assert 0 <= y < self.y

        if not self._cell_is_mine(x, y):
            return

        self._decrease_around(x, y)
        self._remove_mine(x, y)
