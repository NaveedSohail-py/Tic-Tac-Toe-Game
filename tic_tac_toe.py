import os
import game_art
import game_data

def show_game_board(matrix):
    hr = "----------------"
    for i, row in enumerate(matrix):
        print(hr)
        line = ""
        for j, x in enumerate(row):
            if x == " ":
                pos = game_data.game_positions[i][j]
                line += f"  {pos}  |"
            else:
                line += f"  {x}  |"
        print(line[:-1])
    print(hr)

def update_game_board(flag, pos):
    if flag:
        marker = "O"
    else:
        marker = "X"

    global current_game_board
    matrix_pos = game_data.game_board_position[pos]

    if current_game_board[matrix_pos] != " ":
        return False

    current_game_board[matrix_pos] = marker
    return True

def player(flag):
    return "Player A" if not flag else "Player B"

def player_win_art(flag):
    return game_art.player_A_wins_art if not flag else game_art.player_B_wins_art

def is_there_a_winner():
    global current_game_board

    for row in game_data.winning_combination:
        if current_game_board[row[0]] != " " and \
           current_game_board[row[0]] == current_game_board[row[1]] and \
           current_game_board[row[0]] == current_game_board[row[2]]:
            return True
    return False

def is_a_draw():
    global current_game_board

    for row in current_game_board:
        for x in row:
            if x == " ":
                return False
    return True

def end_current_game(draw=False):
    show_game_board(current_game_board)
    global player_flag
    if not draw:
        print(f"{player_win_art(player_flag)}")
    else:
        print(f"{game_art.draw_art}")

    global game_on
    game_on = False
    input("Press any key to continue ...")

# start game
current_game_board = game_data.game_board

while True:
    game_on = True
    player_flag = False

    os.system('clear')

    print(game_art.welcome_art)
    print("Please note the position numbering for the game")
    show_game_board(game_data.game_positions)

    ans = input("Press any key to play, q to quit: ")
    if ans.lower() == "q":
        break

    while game_on:
        while True:
            show_game_board(current_game_board)
            position = int(input(f"{player(player_flag)}: Choose position: "))
            success = update_game_board(player_flag, position)
            if success:
                break
            else:
                print("Position already chosen!")

        if is_there_a_winner():
            end_current_game()
        elif is_a_draw():
            end_current_game(True)

        player_flag = not player_flag
