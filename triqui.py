import random

board = [' ' for _ in range(9)]
player = ''
bot = ''

def draw_board():
    print('-------------')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('-------------')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('-------------')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('-------------')

def choose_player():
    global player, bot
    player = input("¿Quieres jugar con 'X' o 'O'? ").upper()
    while player not in ['X', 'O']:
        player = input("Por favor, elige 'X' o 'O': ").upper()
    if player == 'X':
        bot = 'O'
    else:
        bot = 'X'

def make_move(player, position):
    board[position] = player

def is_winner(board, player):
    return ((board[0] == player and board[1] == player and board[2] == player) or
            (board[3] == player and board[4] == player and board[5] == player) or
            (board[6] == player and board[7] == player and board[8] == player) or
            (board[0] == player and board[3] == player and board[6] == player) or
            (board[1] == player and board[4] == player and board[7] == player) or
            (board[2] == player and board[5] == player and board[8] == player) or
            (board[0] == player and board[4] == player and board[8] == player) or
            (board[2] == player and board[4] == player and board[6] == player))

def is_board_full(board):
    return ' ' not in board

def get_bot_move():
    return random.choice([i for i in range(9) if board[i] == ' '])

def play():
    global board
    choose_player()
    print("Empezaremos a jugar. {} va primero.".format(player))
    draw_board()
    while True:
        if player == 'X':
            position = int(input("Selecciona una casilla (1-9): ")) - 1
            while board[position] != ' ':
                position = int(input("La casilla está ocupada, por favor, elige otra (1-9): ")) - 1
            make_move(player, position)
        else:
            position = get_bot_move()
            make_move(bot, position)
            print(f"El bot ha elegido la casilla {position+1}.")
        draw_board()
        if is_winner(board, player):
            print(f"{player} ha ganado. ¡Felicidades!")
            break
        elif is_winner(board, bot):
            print(f"{bot} ha ganado. ¡Inténtalo de nuevo!")
            break
        elif is_board_full(board):
            print("El juego ha terminado en empate.")
            break
        if player == 'X':
            player = 'O'
        else:
            player = 'X'

play()
