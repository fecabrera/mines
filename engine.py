from base_engine import BaseEngine


class Engine(BaseEngine):
    """Engine class to handle the game logic.
    
    This engine provides basic mine placement and removal functionality
    with manual board updates.
    """
    
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

        self._remove_mine(x, y)

    def update_cell(self, x: int, y: int):
        """Update the cell with the number of mines around it.
        
        Args:
            x (int): X coordinate of the cell.
            y (int): Y coordinate of the cell.
            
        Raises:
            AssertionError: If coordinates are out of bounds.
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
        """Update the board with the number of mines around each cell.
        
        Iterates through all cells and updates their values to reflect
        the number of adjacent mines.
        """
        for x in range(self.x):
            for y in range(self.y):
                self.update_cell(x, y)
