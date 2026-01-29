from chess_2d.Game_Engine import static_variables
from chess_2d.Game_Engine.Game_utils import common_functions
from chess_2d.Game_Engine.Error_handler import set_error

class Board:
    yellow=static_variables.yellow
    green=static_variables.green
    yellow_possible_positions={}
    green_possible_positions={}
    piece_ref=static_variables.piece_ref
    col_ref=static_variables.col_ref
    row_ref=static_variables.row_ref
    current_player='yellow'
    error=set_error.Error()
    running=True
    main_window=None
    canvas =None

    selected_cell=None
    def __init__(self):
        for i in range(8):
           self.yellow['pawn'][i]=common_functions.index_to_cell(2,i)
        self.yellow['king']=['e1']
        self.yellow['queen']=['d1']
        self.yellow['rook']=['a1','h1']
        self.yellow['bishop']=['c1','f1']
        self.yellow['knight']=['b1','g1']
        
        for i in range(8):
            self.green['pawn'][i]=common_functions.index_to_cell(7,i)
        self.green['king']=['e8']
        self.green['queen']=['d8']
        self.green['rook']=['a8','h8']
        self.green['bishop']=['c8','f8']
        self.green['knight']=['b8','g8']
        

def build_board(self):
    return Board()