
## 🎮 Board Layout# 🧠 Memory Match Game

## 🎓 Stanford Code in Place 2025 — Final Project

**Memory Match Game** is a simple, fun, and challenging memory card matching game you can play right in the terminal. Built entirely in Python, this console-based game helps you train your memory and logical thinking by revealing and matching hidden cards on a grid.

---

## 🕹️ How to Play

💡 **Objective**: Match all 8 pairs of hidden cards on the board.

### 🎮 Game Rules

- The board is a 4x4 grid with positions labeled like `A1`, `B3`, etc.
- Each cell hides a symbol. There are 8 unique symbols, each repeated twice.
- On your turn, choose **two different cards** (e.g., `A1`, `C3`).
- If both cards have the same symbol, they stay revealed ✅.
- If they’re different, they are hidden again ❌.
- The game continues until all 16 cards are revealed 🎉.

### ✅ Valid Inputs

- Use row letter (A-D) + column number (1-4), like: `A2`, `D4`, `B3`, etc.

### 🚫 Invalid Inputs

- Typing a position outside the grid (e.g., `E5`, `Z9`)
- Repeating the same card (e.g., `B2`, `B2`)
- Selecting a card that's already been revealed

📢 The game will notify you with clear messages and emojis when you make a mistake.

---

## 💻 How to Run the Game

### ▶️ Run in Terminal

Make sure you have Python 3.6+ installed. Then run:

```bash
python3 memory_game.py
No extra libraries or setup required! 🔥

🧾 Example Gameplay
mathematica
Copiar
Editar
    1   2   3   4
A   *   *   *   *
B   *   *   *   *
C   *   *   *   *
D   *   *   *   *

🎯 Enter the first card (e.g., A1): A2
🎯 Enter the second card (e.g., B4): B4

🟢 It's a match! A2 = B4 = 🐍

...

🎉🎉🎉 CONGRATULATIONS! 🎉🎉🎉
You found all the pairs!
🧠 What I Learned
Structuring code using functions

Handling user input and validation

Using sets and lists effectively

Applying control flow with if/else

Printing formatted boards dynamically

📂 Project Files

bash
Copiar
Editar
final_project/
├── main.py      # Main Python file with all logic
└── README.md           # Game instructions and documentation



🙌 Acknowledgments
This game was created as my final project for the incredible Code in Place 2025 course, taught by Prof. Maryam and supported by a global community of educators and learners.

Thank you to the whole C.I.P. team! 🌟
- 4x4 grid (16 cards total, 8 pairs)
- Rows are labeled A to D
- Columns are labeled 1 to 4

### Valid Input Examples
✅ A1, B3, D4, C2

### Invalid Input Examples
❌ a5, E2, 11, X9

## 💡 Tips
- Pay attention to the card positions
- Try to remember where you saw specific cards
- Plan your moves ahead
- Stay focused and have fun!

## 🚀 Getting Started
1. Make sure you have Python installed
2. Run the game using: `python main.py`
3. Follow the on-screen instructions

## 📝 Author
👤 **Miguel Angel Castillo Enriquez**  
📧 Email: [migue_angelsk8@hotmail.com](mailto:migue_angelsk8@hotmail.com)  
💻 GitHub: [MigueEC](https://github.com/MiguelAngelEc)

Good luck and have fun playing! 🍀
