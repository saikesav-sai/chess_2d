from colorama import Fore,Back,Style
from chess_cli.Board.build import build_board
from chess_cli.Game_Engine.runner import runner
from chess_cli.Game_Engine.Game_utils import common_functions


class chess:
    def __init__(self):
        board=build_board(self)
        common_functions.clrscr()
        print("----------------WELCOME TO CHESS --------------")
        print("Input format (e.g., e2 e4)")
        print("Press q to quit the game anytime")
        print("-----------------------------------------------")
        print("Made by - Sai Kesav")
        runner(board)
        

chess()