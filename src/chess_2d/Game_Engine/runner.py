from chess_2d.Game_Engine.Error_handler import set_error
from chess_2d.Game_Engine.Game_Rules import move_validator,game_rules
from chess_2d.Game_Engine.Game_utils import util,common_functions,board_printing
from chess_2d.Game_Engine.Error_handler import error_printer

def runner(board):
    
    board_printing.print_board(board)
    perform_move(board)
    board.main_window.mainloop()


def perform_move(board):

    input=util.take_user_input(board)
    if input is None:
        print("Game exited")
        return
    if board.error.flag and board.error.type in ['Abort','input_error']: # Error in input
        return False

    source_cell,distination_cell=map(str,input)
    
    if move_validator.is_legal_move(board,source_cell,distination_cell):
        util.update_piece_position(board,source_cell,distination_cell)
        util.update_current_player(board)
        board_printing.redraw_board(board)
        board.main_window.after(0, lambda: perform_move(board))
        
    
    
    