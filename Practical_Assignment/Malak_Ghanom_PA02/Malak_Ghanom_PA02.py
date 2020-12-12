# Tic-Tac-Toe
# Global variables
#
# Define your global variables here
player_turn = 1                                     #initialize the player turn to player 1
board = ['#','#','#','#','#','#','#','#','#']       #initialize the board to the empty value

# Game loop
is_running = False                                  #initialize the game loop to false
# Players (x,O)
players = ()                                        #initialize the player tuple

# Game board
def initalize_game():
    global board,player_turn, is_running,players        #Define the global variable to edit them
    board = ['#','#','#','#','#','#','#','#','#']       #Initialize game board. Hint: All spaces should have '#' 
    players = player_input()                            #Assign players by calling your player_input() function
    player_turn = 1                                     #Initialize player turn to player 1
    is_running = True                                   #Remember to the game loop flag to True.

def display_board(board):                                               #Print the game board
    print("\n")
    print(f"\t{board[6]}\t|\t{board[7]}\t|\t{board[8]}\t6 | 7 | 8")     # -->    #   |   #   |   #      6 | 7 | 8
    print(f"\t{board[3]}\t|\t{board[4]}\t|\t{board[5]}\t3 | 4 | 5")     # -->    #   |   #   |   #      3 | 4 | 5
    print(f"\t{board[0]}\t|\t{board[1]}\t|\t{board[2]}\t0 | 1 | 2")     # -->    #   |   #   |   #      0 | 1 | 2
    print("\n")

def place_marker(board, player, position):        #Place the player marker on the board at position and return the board
    board[position] = player                      #assign the mark to the position
    return board                                  #return board after assignement

def check_space(board, position):                 #Check if position on the board is empty return true else return false
    if board[position] == '#':                    #if the position is empty
        return True                               #return true
    else:                                         #otherwise
        return False                              #return false

def player_choice(player, board):                 #Ask the player to choose a space on the board,
    choice = input(f"{player}'s turn. Please select an empty space between 0 and 8: ")
    if choice != '':                              #if the choice not empty
        choice = int (choice)                     #convert to intejer
        for i in range(0,9):                      #Check if the player choice is valid (between 0-8)
            if choice == i:                       #if valid
                if check_space(board, choice):    #Check if the player choice is available
                    return choice                 #if valid and available return choice
        print("invalid (out of range)")           #out of range
    else:                                         #if empty choice
        print("invalid (out of range)")           #alert the player
    return player_choice(player, board)

def player_input():                                                         #ask the player to pick 'X' or 'O' (function)
    player1 = str(input("\nPlease pick a marker 'X' or 'O': ")).upper()     #ask the player to pick 'X' or 'O' (input) 
    if player1 == 'X' or player1 == 'O':                                    #allow user to choose only 'X' or 'O'
        if player1 == 'X':                                                  #if player choose 'X'
            print("You've choosen X. player 2 will be O")                   #print his choice
            return (player1,'O')                                            #return players content
        else:                                                               #else if player choose 'O'
            print("You've choosen O. player 2 will be X")                   #print his choice
            return (player1,'X')                                            #return players content
    else:                                                                   #if the player choose another thing
        print( 'invalid marker')                                            #alert him
        player_input()                                                      #ask him to reselect


def check_board_full(board):            #Check if the board is full by counting the number of spaces left.
    count = 0                           #initiate the hash (#) counter to zero
    for i in board:                     #loop for counting the no. of # in the board
        if i == '#':
            count +=1

    if count == 0:                      #if the board doesn't has # --> (full)
        return True                     #return true
    else:                               #otherwise
        return False                    #retun false

def check_win(board, mark):
    #Check rows for a win
    if board[0]==board[1]==board[2]==mark or board[3]==board[4]==board[5]==mark or board[6]==board[7]==board[8]==mark:
        return True
    #Check coloumns for a win
    elif board[0]==board[3]==board[6]==mark or board[1]==board[4]==board[7]==mark or board[2]==board[5]==board[8]==mark:
        return True
    #Check diagonals for a win
    elif board[2]==board[4]==board[6]==mark or board[0]==board[4]==board[8]==mark:
        return True
    else:               #if there is no winner
        return False                

def replay():                                                             #Ask if the player wishes to start a new game
    replay_game = str(input("Do you want to play again (y/n)? ")).lower()
    if replay_game == 'y':
        return True
    else:
        return False

# DO NOT CHANGE THE LINE BELOW

if __name__ == "__main__":
    print('\nWelcome to Tic-Tac-Toe!')
    
    initalize_game()                                   #Call the initialize_game() function
    display_board(board)                               #display the board on screen
    while is_running:                                  #while the players play and want to play another game this condition will be true
        
        while not check_board_full(board):             #While the board is not full keep playing until the board get full or somebody win the game 
                
            if player_turn % 2 == 1:                   #Check if the player_turn value is odd or even
                player = players[0]                    #if the no. is odd player turn for player 1
            else:
                player = players[1]                    #if the no. is even player turn for player 2
                
            position=player_choice(player, board)      #Call your player_choice() function to ask the user for a position to put his mark on it
            place_marker(board, player, position)      #Call your place_marker() function to place the marker on the board
            display_board(board)                       #Display the board after each selection
            player_turn += 1                           #Increment the player turn counter

            winner = check_win(board,player)           #Check if there is a winner on the board
            if winner:                                 #Check if there is a winner on the board
                print(f"{player} won!")                #print the winner mark
                break                                  #and leave the current game if somebody won

        if winner==False:
            print("Sorry! niether X nor O won the game")
        if replay():                                   #ask the player if he wishes to play again
            initalize_game()                           #initialize the game again
            display_board(board)                       #display the board again
        else:
            is_running = False                         #if the player don't want to replay this will stop the while loop