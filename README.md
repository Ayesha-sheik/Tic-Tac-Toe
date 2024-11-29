# Tic-Tac-Toe
Creating a graphical user interface (GUI) for the Tic-Tac-Toe game makes the experience more interactive and visually appealing. Below is a Python implementation using the **Tkinter** library for the GUI.

---
# Algorithm Overview
Game Representation: Use a 3x3 grid to represent the board. Each cell can have one of three values: 'X' for the AI, 'O' for the human, or '' for empty.

1.Minimax Algorithm:

Objective: Maximize the AI's score while minimizing the opponent's score.
Base Case: Evaluate the board's state to determine if the AI has won, lost, or if it's a draw.
Recursive Case: Simulate all possible moves for the AI and the human, recursively choosing the best move.
Alpha-Beta Pruning:

Optimize Minimax by cutting off branches in the search tree that don't affect the final decision.
2.Human Interaction:

Allow the human player to choose a move via input.

### **Features**
1. **Interactive Interface**:
   - A grid of buttons represents the Tic-Tac-Toe board.
   - Players can click buttons to make their moves.

2. **AI Integration**:
   - The AI uses the Minimax algorithm to make optimal moves.
   - Ensures the AI is unbeatable.

3. **Reset Functionality**:
   - A "Reset" button clears the board to start a new game.

4. **Game Notifications**:
   - A pop-up message announces the winner or a draw.

---

### **How It Works**
1. Players take turns by clicking buttons on the grid.
2. The AI plays immediately after the human player's move.
3. The game ends with a notification of the result: AI win, player win, or draw.

---

### **Requirements**
- Python 3.x
- Tkinter (built-in with Python)

This GUI version of Tic-Tac-Toe provides an engaging and user-friendly experience while showcasing the unbeatable AI logic.
Here's an updated version of the **Tic-Tac-Toe** program that counts the score and shows a simple celebration animation when a player wins. The score is displayed on the interface, and the winner's buttons flash to celebrate the win.

---

### **Tic-Tac-Toe with Score Tracking and Celebration**
### **New Features**
1. **Score Tracking**:
   - Tracks and displays the scores for the player and AI.
   - Updates after each game.

2. **Celebration Animation**:
   - Winning cells flash in yellow for a celebratory effect.
   - Visual feedback enhances the game experience.

3. **Interactive Reset**:
   - Resets the board while preserving scores.

---

### **How It Works**
1. Players take turns by clicking the buttons.
2. The AI plays optimally using the Minimax algorithm.
3. Scores update after each game.
4. Winning cells flash in celebration of a victory.

This version makes the game fun, competitive, and visually appealing!
