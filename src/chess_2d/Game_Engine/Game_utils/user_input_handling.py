from chess_cli.Game_Engine.Error_handler import set_error

def take_user_input(board:complex):
    print("Enter Move",end=" ")
    user_input=input()
    
    if user_input=='q': # if the user inputed 'q' then raise a Abort error
        board.error=set_error.Error(True,'Abort','User Aborted :(')
        return input
    
    if not user_input: # if user entered no input raise input_error
        board.error=set_error.Error(True,'input_error','Please Enter a Input')
        return input

    user_input_list=user_input.split(" ")
    if  not (len(user_input_list) == 2):# lenght other then 2 raise input_error
        board.error=set_error.Error(True,'input_error','Please Enter a Input')
        return input
    
    if not board.error.flag: # no error raised
        source,distination=map(str,user_input_list)
        return str.lower(source),str.lower(distination)