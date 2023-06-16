from copy import deepcopy


class Engine:
    _size_x: int
    _size_y: int
    _board: list[list[int]]
    _n_mines: int

    def __init__(self, x, y=None):
        self._size_x = x
        self._size_y = y or x
        self._board = [[0 for _ in range(self.y)] for _ in range(self.x)]
        self._n_mines = 0

    @property
    def x(self):
        return self._size_x
    
    @property
    def y(self):
        return self._size_y

    def get_board(self):
        return deepcopy(self._board)
    
    def _place_mine(self, x, y):
        assert 0 <= x < self.x
        assert 0 <= y < self.y

        self._board[x][y] = None
        self._n_mines += 1

    def _reset_cell(self, x, y):
        assert 0 <= x < self.x
        assert 0 <= y < self.y

        self._board[x][y] = 0

    def _increase_cell(self, x, y):
        assert 0 <= x < self.x
        assert 0 <= y < self.y

        self._board[x][y] += 1

    def _decrease_cell(self, x, y):
        assert 0 <= x < self.x
        assert 0 <= y < self.y

        self._board[x][y] -= 1
    
    def place_mine(self, x, y):
        assert 0 <= x < self.x
        assert 0 <= y < self.y

        if self.get_cell(x, y) is None:
            return
        
        self._place_mine(x, y)

        for i in (x - 1, x, x + 1):
            if i < 0 or i >= self.x:
                continue
        
            for j in (y - 1, y, y + 1):
                if j < 0 or j >= self.y:
                    continue

                if self.get_cell(i, j) is not None:
                    self._increase_cell(i, j)
    
    def _remove_mine(self, x, y):
        assert 0 <= x < self.x
        assert 0 <= y < self.y

        self._reset_cell(x, y)
        self._n_mines -= 1
    
    def remove_mine(self, x, y):
        assert 0 <= x < self.x
        assert 0 <= y < self.y

        if self.get_cell(x, y) is not None:
            return
        
        self._remove_mine(x, y)

        n_mines = 0
        for i in (x - 1, x, x + 1):
            if i < 0 or i >= self.x:
                continue
        
            for j in (y - 1, y, y + 1):
                if j < 0 or j >= self.y:
                    continue

                if self.get_cell(i, j) is not None:
                    self._decrease_cell(i, j)
                else:
                    n_mines += 1
        
        self._board[x][y] = n_mines
    
    def get_cell(self, x, y):
        assert 0 <= x < self.x
        assert 0 <= y < self.y

        return self._board[x][y]
    
    def mine_count(self):
        return self._n_mines
    
    def __getitem__(self, key):
        assert len(key) == 2

        x, y = key
        return self.get_cell(x, y)
    
    __len__ = mine_count
