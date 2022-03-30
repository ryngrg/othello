import numpy as np


class Board:
    def __init__(self):
        self.board = np.zeros((8, 8))
        self.player = 1

    def reset(self):
        self.__init__()

    def update_flip(self, x, y):
        opponent = 3 - self.player
        flipped = []
        i = x + 1
        while i < 8 and self.board[i][y] == opponent:
            i += 1
        if i != 8 && self.board[i][y] == self.player():
            for k in range(x + 1, i):
                self.board[k][y] = self.player()
                flipped.append((k, y))
                
        for (a, b) in flipped:
            self.update_flip(a, b)
        
    def check_valid(self, x, y):
        if x not in range(8):
            return False
        if y not in range(8):
            return False
        if self.board[x][y] != 0:
            return False
        return True
        
    def make_move(self, x, y):
        if self.check_valid(x, y):
            self.board[x][y] = self.player
            self.update_flip(x, y)
            self.player = 3 - self.player
            return True
        else:
            print("invalid move requested")
            return False

    def play(self, get_move_func, display = False):
        moves = 0
        while moves < 64:
            x, y = get_move_func()
            if self.make_move(x, y):
                moves += 1
            if display:
                self.display()
        if self.board.sum() == 96:
            if display:
                print("game drawn")
            return 0
        elif self.board.sum() < 96:
            if display:
                print("player 1 wins")
            return 1
        else:
            if display:
                print("player 2 wins")
            return 2

    def display(self):
        print(self.board)


def get_human_move():
    x = int(input("x : "))
    y = int(input("y : "))
    return x, y

if __name__ == "__main__":
    board = Board()
    board.play(get_human_move, display = True)
