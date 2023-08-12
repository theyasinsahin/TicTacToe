import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Tic Tac Toe Game")

title_label = tk.Label(text="Tic Tac Toe", font=("Arial", 20))
title_label.grid(row=0, column=1)

player = "X"
player_label = tk.Label(text=f"{player}'s turn",font=("Arial", 15), fg="red")
player_label.grid(row=1,column=1)
# Create board
def create_board():
    for i in range(2,5):
        for j in range(3):
            button = tk.Button(text="", font=("Arial", 50), height=2, width=6, bg="lightblue", command=lambda row=i, col=j: handle_click(row, col))
            button.grid(row=i, column=j, sticky="nsew")

create_board()

# Initialize variables
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
current_player = 1

# Handle button clicks
def handle_click(row, col):
    global current_player
    global player
    global player_label
    global board

    if board[row-2][col] == 0:
        if current_player == 1:
            board[row-2][col] = "X"
            player= "O"
            player_label.config(text=f"{player}'s turn", fg="blue")
            current_player = 2
        else:
            board[row-2][col] = "O"
            player= "X"
            player_label.config(text=f"{player}'s turn", fg="red")
            current_player = 1

        button = window.grid_slaves(row=row, column=col)[0]
        button.config(text=board[row-2][col])
        check_for_winner(board)

def check_for_winner(board):
    winner = None
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != 0:
            winner = row[0]
            break

    # Check columns
    for col in range(len(board)):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != 0:
            winner = board[0][col]
            break

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        winner = board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
        winner = board[0][2]

    if all([all(row) for row in board]) and winner is None:
        winner = "tie"

    if winner:
        declare_winner(winner)

def declare_winner(winner):
    if winner == "tie":
        message = "It's a tie!"
    else:
        message = f"Player {winner} wins!"


    answer = messagebox.askyesno("Game Over", message + " Do you want to restart the game?")

    if answer:
        global board
        board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(2,5):
            for j in range(3):
                button = window.grid_slaves(row=i, column=j)[0]
                button.config(text="")

        global current_player
        current_player = 1

        global player
        player = "X"
        player_label.config(text=f"{player}'s turn", fg="red")
    else:
        window.quit()

window.mainloop()
