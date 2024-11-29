import tkinter as tk
from tkinter import messagebox
import math
import time

# Initialize the board and scores
board = [["" for _ in range(3)] for _ in range(3)]
player_score = 0
ai_score = 0

# Evaluate the board's state
def evaluate():
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0]:
            return (1 if board[i][0] == "X" else -1), [(i, 0), (i, 1), (i, 2)]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i]:
            return (1 if board[0][i] == "X" else -1), [(0, i), (1, i), (2, i)]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0]:
        return (1 if board[0][0] == "X" else -1), [(0, 0), (1, 1), (2, 2)]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2]:
        return (1 if board[0][2] == "X" else -1), [(0, 2), (1, 1), (2, 0)]

    # Check for a draw
    if all(board[i][j] for i in range(3) for j in range(3)):
        return 0, []

    # Game is ongoing
    return None, []

# Minimax algorithm with Alpha-Beta Pruning
def minimax(is_maximizing, alpha, beta):
    score, _ = evaluate()
    if score is not None:
        return score

    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if not board[i][j]:
                    board[i][j] = "X"
                    eval = minimax(False, alpha, beta)
                    board[i][j] = ""
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if not board[i][j]:
                    board[i][j] = "O"
                    eval = minimax(True, alpha, beta)
                    board[i][j] = ""
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Get the best move for the AI
def best_move():
    best_value = -math.inf
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if not board[i][j]:
                board[i][j] = "X"
                move_value = minimax(False, -math.inf, math.inf)
                board[i][j] = ""
                if move_value > best_value:
                    best_value = move_value
                    move = (i, j)
    return move

# Flash the winning buttons to celebrate
def celebrate(winning_cells):
    for _ in range(5):  # Flash 5 times
        for (r, c) in winning_cells:
            buttons[r][c].config(bg="yellow")
        root.update()
        time.sleep(0.2)
        for (r, c) in winning_cells:
            buttons[r][c].config(bg="SystemButtonFace")
        root.update()
        time.sleep(0.2)

# Update the board and check the game state
def make_move(row, col, player):
    global player_score, ai_score

    if board[row][col] or evaluate()[0] is not None:
        return

    # Update board and button
    board[row][col] = player
    buttons[row][col].config(text=player)

    # Check game state
    result, winning_cells = evaluate()
    if result is not None:
        if result == 1:
            ai_score += 1
            score_label.config(text=f"Player: {player_score} | AI: {ai_score}")
            celebrate(winning_cells)
            messagebox.showinfo("Game Over", "AI wins!")
        elif result == -1:
            player_score += 1
            score_label.config(text=f"Player: {player_score} | AI: {ai_score}")
            celebrate(winning_cells)
            messagebox.showinfo("Game Over", "You win!")
        else:
            messagebox.showinfo("Game Over", "It's a draw!")
        reset_game()
        return

    # If it's AI's turn, make its move
    if player == "O":
        ai_move = best_move()
        make_move(ai_move[0], ai_move[1], "X")

# Reset the game
def reset_game():
    global board
    board = [["" for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", bg="SystemButtonFace")

# Initialize the GUI
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Create a 3x3 grid of buttons
buttons = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", font=("Arial", 24), height=2, width=5,
                                  command=lambda row=i, col=j: make_move(row, col, "O"))
        buttons[i][j].grid(row=i, column=j)

# Display the score
score_label = tk.Label(root, text="Player: 0 | AI: 0", font=("Arial", 14))
score_label.grid(row=3, column=0, columnspan=3)

# Reset button
reset_button = tk.Button(root, text="Reset", font=("Arial", 14), command=reset_game)
reset_button.grid(row=4, column=0, columnspan=3)

# Run the GUI event loop
root.mainloop()
