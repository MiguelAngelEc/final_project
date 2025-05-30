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
    
    print("Tablero de juego (cartas ocultas):")
    print_board(board)
    
    print("\nTablero con las cartas (solo para pruebas):")
    print_board(hidden_board)

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
    

if __name__ == "__main__":
    main()
