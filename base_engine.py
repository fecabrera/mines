from copy import deepcopy


class BaseEngine(object):
    """Base engine class for mine placement and board management.
    
    This class provides the foundation for mine placement games, handling
    board state, mine counting, and basic operations.
    
    Attributes:
        _size_x (int): Width of the board.
        _size_y (int): Height of the board.
        _board (list[list[int]]): 2D board representation.
        _n_mines (int): Current number of mines on the board.
    """
    _size_x: int
    _size_y: int
    _board: list[list[int]]
    _n_mines: int

    @property
    def x(self):
        """Get the width of the board.
        
        Returns:
            int: The width of the board.
        """
        return self._size_x

    @property
    def y(self):
        """Get the height of the board.
        
        Returns:
            int: The height of the board.
        """
        return self._size_y

    @property
    def mine_count(self):
        """Get the current number of mines on the board.
        
        Returns:
            int: The number of mines currently placed.
        """
        return self._n_mines

    def __init__(self, x: int, y: int = None):
        """Initialize the base engine.
        
        Args:
            x (int): Width of the board.
            y (int, optional): Height of the board. If None, defaults to x.
        """
        self._size_x = x
        self._size_y = y or x
        self.reset_board()

    def reset_board(self):
        """Reset the board to an empty state.
        
        Clears all mines and resets all cells to 0.
        """
        self._board = [[0 for _ in range(self.y)] for _ in range(self.x)]
        self._n_mines = 0

    def place_mine(self, x: int, y: int):
        """Place a mine on the board.
        
        Args:
            x (int): X coordinate of the mine.
            y (int): Y coordinate of the mine.
            
        Raises:
            NotImplementedError: This method must be implemented by subclasses.
        """
        raise NotImplementedError

    def remove_mine(self, x: int, y: int):
        """Remove a mine from the board.
        
        Args:
            x (int): X coordinate of the mine.
            y (int): Y coordinate of the mine.
            
        Raises:
            NotImplementedError: This method must be implemented by subclasses.
        """
        raise NotImplementedError

    def place_mines(self, *mines: tuple[int, int]):
        """Place multiple mines on the board.
        
        Args:
            *mines (tuple[int, int]): Variable number of (x, y) coordinate tuples.
        """
        for x, y in mines:
            self.place_mine(x, y)

    def remove_mines(self, *mines: tuple[int, int]):
        """Remove multiple mines from the board.
        
        Args:
            *mines (tuple[int, int]): Variable number of (x, y) coordinate tuples.
        """
        for x, y in mines:
            self.remove_mine(x, y)

    def get_cell(self, x: int, y: int):
        """Get the value of a cell.
        
        Args:
            x (int): X coordinate of the cell.
            y (int): Y coordinate of the cell.
            
        Returns:
            int or None: The value of the cell (0 for empty, None for mine).
            
        Raises:
            AssertionError: If coordinates are out of bounds.
        """
        assert 0 <= x < self.x
        assert 0 <= y < self.y

        return self._board[x][y]

    def _cell_is_mine(self, x: int, y: int):
        """Check if the cell is a mine.
        
        Args:
            x (int): X coordinate of the cell.
            y (int): Y coordinate of the cell.
            
        Returns:
            bool: True if the cell contains a mine, False otherwise.
        """
        return self.get_cell(x, y) is None

    def _make_mine(self, x: int, y: int):
        """Mark a cell as containing a mine.
        
        Args:
            x (int): X coordinate of the cell.
            y (int): Y coordinate of the cell.
        """
        self._board[x][y] = None

    def _reset_cell(self, x: int, y: int):
        """Reset a cell to empty state.
        
        Args:
            x (int): X coordinate of the cell.
            y (int): Y coordinate of the cell.
        """
        self._board[x][y] = 0

    def _place_mine(self, x: int, y: int):
        """Internal method to place a mine and update count.
        
        Args:
            x (int): X coordinate of the mine.
            y (int): Y coordinate of the mine.
        """
        self._make_mine(x, y)
        self._n_mines += 1

    def _remove_mine(self, x: int, y: int):
        """Internal method to remove a mine and update count.
        
        Args:
            x (int): X coordinate of the mine.
            y (int): Y coordinate of the mine.
        """
        self._reset_cell(x, y)
        self._n_mines -= 1

    def get_board(self):
        """Get the current state of the board.
        
        Returns:
            list[list[int]]: A deep copy of the current board state.
        """
        return deepcopy(self._board)

    def __len__(self):
        """Get the number of mines on the board.
        
        Returns:
            int: The number of mines currently placed.
        """
        return self.mine_count

    def __getitem__(self, key: tuple[int, int]):
        """Get the value of a cell using tuple indexing.
        
        Args:
            key (tuple[int, int]): A tuple containing (x, y) coordinates.
            
        Returns:
            int or None: The value of the cell.
            
        Raises:
            AssertionError: If the key tuple doesn't have exactly 2 elements.
        """
        assert len(key) == 2

        x, y = key
        return self.get_cell(x, y)
