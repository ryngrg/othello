from othello import Board
from agent import AI_Agent
import tkinter as tk


def draw_bg_grid():
    for i in range(9):
        canvas.create_line(30 * i, 0, 30 * i, 240)
        canvas.create_line(0, 30 * i, 240, 30 * i)
    canvas.update()


def disp_coins():
    canvas.delete('all')
    draw_bg_grid()
    for i in range(8):
        for j in range(8):
            if board.board[i][j] == 1:
                canvas.create_oval(3 + 30*i, 3 + 30*j, 27 + 30*i, 27 + 30*j, fill="black")
            elif board.board[i][j] == 2:
                canvas.create_oval(3 + 30*i, 3 + 30*j, 27 + 30*i, 27 + 30*j, fill="white")

            if human[board.player - 1] and (i, j) in board.moves:
                canvas.create_oval(12 + 30*i, 12 + 30*j, 18 + 30*i, 18 + 30*j, fill="yellow")
    canvas.update()


def game_over():
    print("game over")
    print("winner is :", board.winner)


def click_func(event):
    x = event.x
    y = event.y
    if not board.end:
        if human[board.player - 1]:
            i = int(x / 30)
            j = int(y / 30)
            if (i, j) in board.moves:
                idx = board.moves.index((i, j))
                board.make_move(idx)
                disp_coins()
                while not(board.end or human[board.player - 1]):
                    mv = ai[board.player - 1].get_move(board)
                    board.make_move(mv)
                    disp_coins()
                if board.end:
                    game_over()

    else:
        game_over()


if __name__ == "__main__":
    human = [False, False]
    ai = [None, None]
    r = input("Player 1: human (y/n): ")
    if r[0] in ('y', 'Y'):
        human[0] = True
    else:
        ai[0] = AI_Agent(1)
    r = input("Player 2: human (y/n): ")
    if r[0] in ('y', 'Y'):
        human[1] = True
    else:
        ai[1] = AI_Agent(2)
    board = Board()

    root = tk.Tk()
    root.resizable(False, False)
    canvas = tk.Canvas(root, bg='green', width=240, height=240)
    canvas.pack(expand=True, fill=tk.BOTH)

    canvas.bind("<Button-1>", click_func)

    draw_bg_grid()
    disp_coins()
    if not human[0]:
        move = ai[board.player - 1].get_move(board)
        board.make_move(move)
        disp_coins()
    root.mainloop()
