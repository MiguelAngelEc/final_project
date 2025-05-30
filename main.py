"""
Main script for the application
"""

import random 

def main():
    """
    Main function for the application
    """
    board = create_board()
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

if __name__ == "__main__":
    main()
