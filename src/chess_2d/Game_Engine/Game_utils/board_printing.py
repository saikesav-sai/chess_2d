from chess_cli.Game_Engine.static_variables import piece_ref
from chess_cli.Game_Engine.Game_utils.common_functions import cell_to_index

def print_board(board:complex):
    cells=put_pieces_on_board(board.yellow,board.green)
    print("   "+"   ".join(board.col_ref))
    print()
    for i in range(8):
        print(board.row_ref[i]+"  "+"   ".join(cells[i]))
        print()
    
def put_pieces_on_board(yellow,green):
    cells=[['-' for _ in range(8)]for _ in range(8)] # creating viewable Board

    # putting white pieces into the board
    for piece,cords in yellow.items():
        for text in cords:
            row,col=cell_to_index(text)
            cells[row][col]=f"\033[93m{piece_ref[piece]}\033[00m"

    # putting black pieces into the board
    for piece,cords in green.items():
        for text in cords:
            row,col=cell_to_index(text)
            cells[row][col]=f"\033[92m{piece_ref[piece]}\033[00m"

    return cells

def print_check_message(player:str):
    print(f"\033[91mCheck for {player} player!\033[00m")

