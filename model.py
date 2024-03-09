# In this iteration of my chess model I want to try using a Move object instead of Square objects.
# I want to see if this makes the code more readable and easier to understand.
# There will be less objects in the code, but the Move object will have more attributes.
# Therefore, if I still end up having to use deepcopy, there will be fewer objects to copy.
ranks = ['1', '2', '3', '4', '5', '6', '7', '8']
files = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

class Board:
    #contains a list of files which has one index for each rank, essentially just a map of the board
    #contains a list of pieces
    global ranks
    global files
    # squares will be written as board[file][rank] where each starts at 0
    board = [[file + rank for rank in ranks] for file in files]
    
    def __init__(self):
        pass

class Move:
    #contains a start square and an end square
    #contains a piece
    #will contain a flag for captures and checks
    #will contain flags for special moves like castling, en passant, and promotion
    #a piece will have a list of these as legal moves
    pass

class Piece:
    #contains a color
    #contains a type
    #contains a list of legal moves
    #if a move is a capture, check, or attack, it will be passed to the player's list of checks, captures, and attacks
    pass

class Player:
    #contains a color
    #contains a list of pieces
    #contains a list of checks, captures, and attacks
    #boolean for castling rights
    pass

class Game:
    pass

board = Board()
print(board.board)