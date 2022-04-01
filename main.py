from othello import Board
from agent import AI_Agent
import tkinter as tk

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
        ai[0] = AI_Agent(1)
    board = Board()

    root = tk.Tk()
    canvas = tk.Canvas(root, bg='light green', width=240, height=240)
    for i in range(9):
        canvas.create_line(30 * i, 0, 30 * i, 240)
        canvas.create_line(0, 30 * i, 240, 30 * i)
    # canvas.create_oval(3, 3, 27, 27, fill="white")
    # canvas.create_oval(33, 33, 57, 57, fill="black")
    canvas.pack(expand=True, fill=tk.BOTH)
    root.mainloop()

