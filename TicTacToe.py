from IPython.display import clear_output

def display_the_board(board_list=['0','1','2','3','4','5','6','7','8']):
    
    print([el[0] for el in board_list[0:3]])
    
    print([el[0] for el in board_list[3:6]])
    
    print([el[0] for el in board_list[6:9]])

def users_token():
    #list of all possible tokens in game 
    list_of_tokens = ['X','O']
    
    #current token for the game
    token = ''
    
    #logic to ensure anly valid token in the game 
    while token not in list_of_tokens:
        
        users_token = input('Please choose between: X and O and press ENTER')
        
        if token not in list_of_tokens:
        
            clear_output()

        token = users_token.upper()
        
    return token

def choose_idx_display_board(idx='',list_of_vals=['0','1','2','3','4','5','6','7','8']):
    
    idx = idx
    
    list_of_vals = list_of_vals
    
    while idx not in list_of_vals:
        
        board_list = list(board.values())
    
        display_the_board(board_list)
        
        users_input = input('Please provide number to place token and press ENTER: ')
        
        if idx not in list_of_vals:
            clear_output()
        
        idx = users_input
    
    return idx

import itertools
def result_check(x_mark_rslt=[],o_mark_rslt=[]):
    
    x_mark_rslt = x_mark_rslt
    
    o_mark_rslt = o_mark_rslt
    
    X = 'X win'
    
    O = 'O win'
    
    for x in list(itertools.combinations(x_mark_rslt,3)):
        
        if len(x) == 3 and sum(x) == 15:
            return X
        
    for o in list(itertools.combinations(o_mark_rslt,3)):
        
        if len(o) == 3 and sum(o) == 15:
            return O


def place_the_token(
    user_token = 'X',
    idx = '0',
    board = {'0':['',2],'1':['',7],'2':['',6],'3':['',9],'4':['',5],'5':['',1],'6':['',4],'7':['',3],'8':['',8]}
):    
    
    token = user_token
    
    idx = idx
    
    board = board
    
    val = board[idx][1]
    
    board[idx][0] = token
    
    return val

def restart_the_game():
    
    x_mark_rslt = []
    
    o_mark_rslt = []
    
    board = {'0':['0',2],'1':['1',7],'2':['2',6],'3':['3',9],'4':['4',5],'5':['5',1],'6':['6',4],'7':['7',3],'8':['8',8]}
    
    list_removed = []
    
    list_of_vals = ['0','1','2','3','4','5','6','7','8']
    
    reset = ''
    
    idx = ''
    
    return x_mark_rslt, o_mark_rslt, board, list_of_vals, list_removed, reset, idx

print('Wellcome to Tic Tac Toe')

game_on = True

#values from magic square - if sum == 15 then user won
x_mark_rslt = []

o_mark_rslt = []

#to reset the game
reset = ''

#index of the token
idx = ''

#game_board
board = {'0':['0',2],'1':['1',7],'2':['2',6],'3':['3',9],'4':['4',5],'5':['5',1],'6':['6',4],'7':['7',3],'8':['8',8]}

#lists of possible player's choices
list_of_vals = ['0','1','2','3','4','5','6','7','8']

#list of used user's choices 
list_removed = []

# starting token
user_token = users_token()

while game_on == True: 
    
    board_list = list(board.values())
    
    idx = choose_idx_display_board(idx,list_of_vals)
    
    v = place_the_token(user_token,idx,board)
    
    
    if user_token == 'X':
        
        x_mark_rslt.append(v)
    
    else:
        
        o_mark_rslt.append(v)
        
        M
    if idx in list_of_vals:
        
        list_of_vals.remove(idx)
    
    if idx not in list_removed:
    
        list_removed.append(idx)
    
    
    res = result_check(x_mark_rslt,o_mark_rslt)
    
    
    if user_token == 'X':
        
        user_token = 'O'
    
    else:
        
        user_token = 'X'
    
    
    if res == 'X win':
        
        display_the_board(board_list)
        
        reset = input('Congrats X Player Won! Do you want to play again? Y / N: ')
        
    elif res == 'O win':
        
        display_the_board(board_list)
        
        reset = input('Congrats O Player Won! Do you want to play again? Y / N: ')
    
    elif len(list_of_vals) == 0:
        
        reset = input('It is a draw. Do you want to play again? Y/N: ')
    
    
    if reset.upper() == 'Y':
        
        #unpack starting variables to reset the game
        x,o,b,lv,lr,r,i = restart_the_game() 
        
        x_mark_rslt = x 
        o_mark_rslt = o 
        board = b
        list_of_vals = lv
        list_removed = lr
        reset = r
        idx=i
        
        clear_output()     
        
    elif reset.upper() == 'N':
        game_on = False