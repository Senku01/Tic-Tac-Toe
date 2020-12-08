#Global Variable


#Game Board
board=["-","-","-",
            "-","-","-",
            "-","-","-",]
#if game is still going
game_is_still_going= True

#Who Won
winner=None
#whose Turn Is it?
current_player="X"

#Display Board
def display_board():
    print(board[0]+" | "+board[1]+" | "+board[2])
    print(board[3]+" | "+board[4]+" | "+board[5])
    print(board[6]+" | "+board[7]+" | "+board[8])

#play a game of tic tac toe
def play_game():
    #display Intial Board
    display_board()
    #while the game is still going
    while game_is_still_going:  
         #handle a single turn to a arbitary player    
        handle_turn(current_player)
        #check if game is over
        check_if_game_over()
        #Flip to other player
        flip_player()

#the game has ended
    if winner=="X" or winner=="0":
        print(winner+" won.")
    elif winner==None:
        print("Tie")

def handle_turn(player):

    print(player +"'s turn. ")
    position= input("Choose A Position From 1-9:")
    
    valid =False
    while not valid:


        while position not in ["1","2","3","4","5","6","7","8","9"]:
         position=input("Invalid input.Choose From 1-9")

        position=int(position) -1

        if board[position] =="-":
            valid=True
        else:
            print("You cant Go there ")

    board[position]=player

    display_board()

def check_if_game_over():
    check_if_tie()
    check_if_win()

def check_if_win():
    #setup global variable  
    global winner
    #check row
    row_winner=check_row
    #check column
    column_winner= check_column
    #check diagonals
    diagonal_winner=check_diagonals 
    if row_winner:
        #There is a Row Winner
        winner= row_winner()
    elif column_winner:
        #There is a Column winner
        winner = column_winner()
    elif diagonal_winner:
        #There is a diagonal winner
        winner=diagonal_winner()
    else:
        #There is no win   
        winner=None
    return

def check_row():
    #setup global variable
    global game_is_still_going
    #check if any of the row have all the same value(and is not empty)
    row_1 =board[0]==board[1]==board[2] !="-"
    row_2 =board[3]==board[4]==board[5] !="-"
    row_3 =board[6]==board[7]==board[8] !="-"
    if row_1 or row_2 or row_3:
        game_is_still_going=False
    #return the winner
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return
def check_column():
    #setup global variable
    global game_is_still_going
    #check if any of the row have all the same value(and is not empty)
    column_1 =board[0]==board[3]==board[6] !="-"
    column_2 =board[1]==board[4]==board[7] !="-"
    column_3 =board[2]==board[5]==board[8] !="-"
    if column_1 or column_2 or column_3:
        game_is_still_going=False
    #return the winner
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diagonals():
    #setup global variable
    global game_is_still_going
    #check if any of the row have all the same value(and is not empty)
    diagonal_1 =board[0]==board[4]==board[8] !="-"
    diagonal_2 =board[6]==board[4]==board[2] !="-"
    if diagonal_1 or diagonal_2:
        game_is_still_going=False
    #return the winner
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    return

def check_if_tie():
    global game_is_still_going
    if"-"not in board:
        game_is_still_going= False
    return


def flip_player():
    #Global variable we need
    global current_player
     #if current player is X flip to 0
    if current_player == "X":
        current_player= "0"
    #if current player is 0 flip to X   
    elif current_player =="0":
        current_player="X"
    return

play_game()