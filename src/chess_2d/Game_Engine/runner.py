from chess_2d.Game_Engine.Error_handler import set_error
from chess_2d.Game_Engine.Game_Rules import move_validator,game_rules
from chess_2d.Game_Engine.Game_utils import util,common_functions,board_printing
from chess_2d.Game_Engine.Error_handler import error_printer

def runner(board):

    while  not game_rules.is_check_mate(board):
        error=board.error

        if error.flag: # if error found in previous input
            error_printer.Print_message(error)
            if error.type == 'Abort':
                break
            board.error=set_error.Error() # clearing the error

        if game_rules.is_check(board):
            board_printing.print_check_message(board.current_player)
            
        if perform_move(board):
            util.update_current_player(board)
        common_functions.clrscr()


    if game_rules.is_check_mate(board):
        print(f" {util.get_winner(board)} player WON")
        return
    

    exit(0) 



def perform_move(board):
    
    util.print_board(board)
    

    input=util.take_user_input(board)
    if board.error.flag and board.error.type in ['Abort','input_error']: # Error in input
        return False

    source_cell,distination_cell=map(str,input)
    
    if move_validator.is_legal_move(board,source_cell,distination_cell):
        util.update_piece_position(board,source_cell,distination_cell)
        return True
    
    board.error=set_error.Error(True,'illegal_input',f'please provide correct input: previous input - {source_cell},{distination_cell} ')
    return False
    
    