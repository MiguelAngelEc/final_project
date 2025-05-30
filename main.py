"""
Main script for the application
"""

import random 
import time

def main():
    """
    Main function for the application
    """
    print("🧠🎴 Welcome to the Memory Match Challenge! 🎴🧠\n")
    print("""
    🧠 Welcome to the Memory Game!

    🎯 Goal:
    
    Match all the hidden pairs by remembering their positions.

    🕹️ How to Play:
    
    1️⃣ Enter two positions per turn (e.g., A1 and B2).
    2️⃣ If the cards match, they stay revealed.
    3️⃣ If not, they will be hidden again after 2 seconds.
    4️⃣ You can't pick the same card twice in a turn.

    🎮 Board:
    
    - The board is a 4x4 grid.
    - Rows are labeled A to D.
    - Columns are labeled 1 to 4.

    ✅ Valid Inputs: A1, B3, D4, etc.
    ❌ Invalid Inputs: a5, E2, 11, etc.

    💡 Tip:
    Pay attention and remember the card positions to win faster!

    Good luck! 🍀
    """)
    board = create_board()
    hidden_board = generate_hidden_board()
    revealed = set()
    
    while len(revealed) < 16:
        play_turn(board, hidden_board, revealed)
    print_board(board)
    print("\n")
    print("🎉 You found all the pairs! 🎉")

def create_board(size=4):
    board = [['*' for _ in range (size)] for _ in range (size)]
    return board

def print_board(board):
    size = len(board)
    columns = "    " + "   ".join(str(i + 1) for i in range(size))
    print(columns)
    for i in range(size):
        row = chr(65 + i) + "   " + "   ".join(board[i])
        print(row)

def generate_hidden_board(size=4):
    total_pairs = (size * size) // 2
    
    values = [chr(65 + i) for i in range(total_pairs)] * 2
    random.shuffle(values)
    
    board = []
    index = 0
    for i in range(size):
        row = []
        for j in range(size):
            row.append(values[index])
            index += 1
        board.append(row)
    return board

def parse_position(pos):
    row = ord(pos[0].upper()) - 65
    col = int(pos[1]) - 1
    return row, col

def reveal_card(visible_board, hidden_board, row, col):
    visible_board[row][col] = hidden_board[row][col]
    
def play_turn(board, hidden_board, revealed):
    print_board(board)
    print("\n")
    first = input("Enter the first card (e.g., A1): ")
    second = input("Enter the second card (e.g., B2): ")
    print("\n")
    
    valid_positions = [f"{chr(65 + i)}{j+1}" for i in range(4) for j in range(4)]
    
    if first.upper() not in valid_positions or second.upper() not in valid_positions:
        print(f"⚠️ Invalid input: '{first}' or '{second}' is not a valid position. Please enter positions like A1, B2, etc.\n")
        return

    r1, c1 = parse_position(first)
    r2, c2 = parse_position(second)

    if (r1, c1) == (r2, c2):
        print("⚠️ You picked the same card twice! Please choose two different cards. 🔁 \n")

        return

    board[r1][c1] = hidden_board[r1][c1]
    board[r2][c2] = hidden_board[r2][c2]
    print_board(board)

    if hidden_board[r1][c1] == hidden_board[r2][c2]:
        print(f"🎉 It's a match! You found two '{hidden_board[r1][c1]}' cards!")
        print("\n---------------------------\n")
        revealed.add((r1, c1))
        revealed.add((r2, c2))
    else:
        print(f"🙈 Oops! {hidden_board[r1][c1]} doesn't match {hidden_board[r2][c2]}. Keep trying!")
        print("\n---------------------------\n")
        time.sleep(2)
        if (r1, c1) not in revealed:
            board[r1][c1] = "*"
        if (r2, c2) not in revealed:
            board[r2][c2] = "*"
    

if __name__ == "__main__":
    main()
