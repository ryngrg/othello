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

    def possible_moves(self, player):
        opp = 3 - player # opponent
        moves = []
        flip_list = []
        n_moves = 0
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == 0:
                    # South
                    x = i + 1
                    while x < 8 and self.board[x][j] == opp:
                        x += 1
                    if (x < 8) and (x-i > 1) and (self.board[x][j] == player):
                        moves.append((i, j))
                        n_moves += 1
                        f = []
                        for k in range(i + 1, x):
                            f.append((k, j))
                        flip_list.append(f)
                    
                    # North
                    x = i - 1
                    while x >= 0 and self.board[x][j] == opp:
                        x -= 1
                    if (x >= 0) and (i-x > 1) and (self.board[x][j] == player):
                        moves.append((i, j))
                        n_moves += 1
                        f = []
                        for k in range(x + 1, i):
                            f.append((k, j))
                        flip_list.append(f)
                    
                    # East
                    y = j + 1
                    while y < 8 and self.board[i][y] == opp:
                        y += 1
                    if (y < 8) and (y-j > 1) and (self.board[i][y] == player):
                        moves.append((i, j))
                        n_moves += 1
                        f = []
                        for k in range(j + 1, y):
                            f.append((i, k))
                        flip_list.append(f)
                    
                    # West
                    y = j - 1
                    while y >= 0 and self.board[i][y] == opp:
                        y -= 1
                    if (y >= 0) and (j-y > 1) and (self.board[i][y] == player):
                        moves.append((i, j))
                        n_moves += 1
                        f = []
                        for k in range(y + 1, j):
                            f.append((i, k))
                        flip_list.append(f)
                    
                    # North - West
                    x = i - 1
                    y = j - 1
                    
                    # North - East
                    x = i - 1
                    y = j + 1
                    
                    # South - West
                    x = i + 1
                    y = j - 1
                    
                    # South - East
                    x = i + 1
                    y = j + 1
                    
        if n_moves == 0:
            return False
        self.n_moves = n_moves
        self.moves = moves
        self.flip_list = flip_list
        return True

    def reset(self):
        self.__init__()
        
    def make_move(self, i):
        x, y = self.moves[i]
        self.board[x][y] = self.player
        for (x, y) in self.flip_list[i]:
            self.board[x][y] = self.player

        if self.possible_moves(3 - self.player):
            self.player = 3 - self.player
        elif not(self.possible_moves(self.player)):
            self.end = True

    def play(self, get_move_func, display = False):
        while not(self.end):
            print(self.moves)
            move = get_move_func(self.n_moves)
            self.make_move(move)
            if display:
                self.display()
        num1 = self.count(1)
        num2 = self.count(2)
        if num1 == num2:
            if display:
                print("game drawn")
            return 0
        elif num1 > num2:
            if display:
                print("player 1 wins")
            return 1
        else:
            if display:
                print("player 2 wins")
            return 2

    def display(self):
        print(self.board)


def get_human_move(num_moves):
    i = int(input(str(num_moves) + " possible moves: "))
    return i

if __name__ == "__main__":
    board = Board()
    board.play(get_human_move, display = True)
