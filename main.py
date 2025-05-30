"""
Main script for the application
"""

import random 

def main():
    """
    Main function for the application
    """
    board = create_board()
    hidden_board = generate_hidden_board()
    
    # Simula que el usuario ingresa "C2"
    user_input = "C2"
    row, col = parse_position(user_input)
    reveal_card(board, hidden_board, row, col)

    print("\nVisible board AFTER revealing C2:")
    print_board(board)

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
    

if __name__ == "__main__":
    main()
