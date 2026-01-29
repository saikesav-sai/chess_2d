import tkinter as tk
from chess_2d.Game_Engine.Game_utils import common_functions


cell_size=80
width,height=cell_size * 8 ,cell_size * 8  


def print_board(board:complex):
    

    main_window=tk.Tk()

    main_window.title("Chess 2D - Sai Kesav")
    main_window=create_board(main_window)
    put_pieces_on_board(main_window,board.yellow,board.green)
    main_window.mainloop()

    return

def put_pieces_on_board(main_window,yellow,green):
    
    main_window.images=[]    

    for player_name,player_data in (['green',green],['yellow',yellow]):
        put_one_player_pieces(main_window,player_name,player_data)
    return 
    

def put_one_player_pieces(main_window,player_name,player_data):

    file_name= "white_" if player_name == 'yellow' else "black_"
    folder_path="chess_2d\\img\\"+file_name

    for type,pieces in player_data.items():
        for pos in pieces:
            file_path=folder_path+(type+'.png')
            row,col=common_functions.cell_to_index(pos)

            img=tk.PhotoImage(file=file_path)
            main_window.images.append(img)  
            main_window.create_image(col*cell_size, row*cell_size, image=img, anchor="nw")

    return

def create_board(main_window):
    cell_size=80
    width,height=cell_size * 8 ,cell_size * 8
    board=tk.Canvas(main_window, width=width, height=height)

    colors = ["#f0d9b5", "#b58863"]

    for r in range(8):
        for c in range(8):
            color = colors[(r+c)%2]
            board.create_rectangle(
                c*cell_size, r*cell_size,
                (c+1)*cell_size, (r+1)*cell_size,
                fill=color, outline=""
            )
    board.pack()
    return board


