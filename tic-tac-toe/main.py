board = [' ', ' ', ' ',
         ' ' ,' ', ' ',
         ' ' ,' ', ' '
]


def print_board():
    print(f'{board[0]} | {board[1]} | {board[2]}')
    print('----------')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print('----------')
    print(f'{board[6]} | {board[7]} | {board[8]}')
    

def change_player(player):
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
    return player


def is_move_valid(position):
    if board[position - 1] == ' ':
        return True
    else:
        return False


def check_win():
    if board[0] == board[1] == board[2] != ' ':
        return True
    elif board[3] == board[4] == board[5] != ' ':
        return True
    elif board[6] == board[7] == board[8] != ' ':
        return True
    elif board[0] == board[3] == board[6] != ' ':
        return True
    elif board[1] == board[4] == board[7] != ' ':
        return True
    elif board[2] == board[5] == board[8] != ' ':
        return True
    elif board[0] == board[4] == board[8] != ' ':
        return True
    elif board[2] == board[4] == board[6] != ' ':
        return True
    else:
        return False

    
def main():
    is_game_on = True
    current_player = 'X'
    game_round = 0
    print_board()
    while is_game_on:
        game_round += 1
        print(f"Player '{current_player}' move.")
        choice = int(input("Chose number 1-9: "))
        while not is_move_valid(choice):
            print("Invalid move. Try again.")
            choice = int(input("Chose number 1-9: "))
        board[choice-1] = current_player
        print_board()
        if game_round == 9:
            if check_win():
                print(f"Player '{current_player}' won the game.")
                is_game_on = False
            else:
                print(f"Game ended. Draw.")
                is_game_on = False
        else:
            if check_win():
                print(f"Player '{current_player}' won the game.")
                is_game_on = False
                
        current_player = change_player(current_player)

    
main()