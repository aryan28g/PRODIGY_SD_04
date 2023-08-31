import tkinter as tk
from tkinter import messagebox

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def solve_sudoku(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True
    row, col = empty_cell

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False

def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

class SudokuSolverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")

        self.board = [[tk.StringVar() for _ in range(9)] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                entry = tk.Entry(root, textvariable=self.board[i][j], width=3)
                entry.grid(row=i, column=j)
                entry.insert(0, "0")

        solve_button = tk.Button(root, text="Solve", command=self.solve)
        solve_button.grid(row=9, columnspan=9)

    def solve(self):
        input_board = [[int(self.board[i][j].get()) for j in range(9)] for i in range(9)]

        if solve_sudoku(input_board):
            for i in range(9):
                for j in range(9):
                    self.board[i][j].set(input_board[i][j])
        else:
            messagebox.showinfo("No Solution", "No solution exists.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuSolverApp(root)
    root.mainloop()
