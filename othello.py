import numpy as np


class Board:
    def __init__(self):
        self.board = np.zeros((8, 8))
        self.board[3][3] = 2
        self.board[4][4] = 2
        self.board[4][3] = 1
        self.board[3][4] = 1
        self.player = 1
        self.possible_moves(self.player)
        self.end = False
        self.winner = 0

    def possible_moves(self, player):
        opp = 3 - player  # opponent
        moves = []
        flip_list = []
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == 0:
                    added = False
                    f = []

                    # South
                    x = i + 1
                    while x < 8 and self.board[x][j] == opp:
                        x += 1
                    if (x < 8) and (x-i > 1) and (self.board[x][j] == player):
                        added = True
                        moves.append((i, j))
                        for k in range(i + 1, x):
                            f.append((k, j))
                    
                    # North
                    x = i - 1
                    while x >= 0 and self.board[x][j] == opp:
                        x -= 1
                    if (x >= 0) and (i-x > 1) and (self.board[x][j] == player):
                        if not added:
                            added = True
                            moves.append((i, j))
                        for k in range(x + 1, i):
                            f.append((k, j))
                    
                    # East
                    y = j + 1
                    while y < 8 and self.board[i][y] == opp:
                        y += 1
                    if (y < 8) and (y-j > 1) and (self.board[i][y] == player):
                        if not added:
                            added = True
                            moves.append((i, j))
                        for k in range(j + 1, y):
                            f.append((i, k))
                    
                    # West
                    y = j - 1
                    while y >= 0 and self.board[i][y] == opp:
                        y -= 1
                    if (y >= 0) and (j-y > 1) and (self.board[i][y] == player):
                        if not added:
                            added = True
                            moves.append((i, j))
                        for k in range(y + 1, j):
                            f.append((i, k))
                    
                    # North - West
                    x = i - 1
                    y = j - 1
                    while (y >= 0) and (x >= 0) and self.board[x][y] == opp:
                        y -= 1
                        x -= 1
                    if (y >= 0) and (x >= 0) and (j-y > 1) and (self.board[x][y] == player):
                        if not added:
                            added = True
                            moves.append((i, j))
                        for k in range(1, j - y):
                            f.append((i - k, j - k))
                    
                    # North - East
                    x = i - 1
                    y = j + 1
                    while (y < 8) and (x >= 0) and self.board[x][y] == opp:
                        y += 1
                        x -= 1
                    if (y < 8) and (x >= 0) and (y-j > 1) and (self.board[x][y] == player):
                        if not added:
                            added = True
                            moves.append((i, j))
                        for k in range(1, y - j):
                            f.append((i - k, j + k))
                    
                    # South - West
                    x = i + 1
                    y = j - 1
                    while (y >= 0) and (x < 8) and self.board[x][y] == opp:
                        y -= 1
                        x += 1
                    if (y >= 0) and (x < 8) and (j-y > 1) and (self.board[x][y] == player):
                        if not added:
                            added = True
                            moves.append((i, j))
                        for k in range(1, j - y):
                            f.append((i + k, j - k))
                    
                    # South - East
                    x = i + 1
                    y = j + 1
                    while (y < 8) and (x < 8) and self.board[x][y] == opp:
                        y += 1
                        x += 1
                    if (y < 8) and (x < 8) and (y-j > 1) and (self.board[x][y] == player):
                        if not added:
                            added = True
                            moves.append((i, j))
                        for k in range(1, y - j):
                            f.append((i + k, j + k))

                    if added:
                        flip_list.append(f)

        n_moves = len(moves)
        if n_moves == 0:
            return False
        self.n_moves = n_moves
        self.moves = moves
        self.flip_list = flip_list
        return True

    def reset(self):
        self.__init__()

    def get_curr_info(self):
        return self.board, self.player, self.n_moves, self.moves

    def make_move(self, i):
        if self.end:
            return False
        x, y = self.moves[i]
        self.board[x][y] = self.player
        for (x, y) in self.flip_list[i]:
            self.board[x][y] = self.player

        if self.possible_moves(3 - self.player):
            self.player = 3 - self.player
        elif not(self.possible_moves(self.player)):
            self.end = True
            self.player = 0
            num1 = self.count(1)
            num2 = self.count(2)
            if num1 == num2:
                self.winner = 0
            elif num1 > num2:
                self.winner = 1
            else:
                self.winner = 2
        return not self.end

    def count(self, p):
        num = 0
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == p:
                    num += 1
        return num
