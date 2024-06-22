bc = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
turn = 1
game_on = True


def show_board(letter):
    return f'''
     {bc[0][0]} | {bc[0][1]} | {bc[0][2]}
     ---------
     {bc[1][0]} | {bc[1][1]} | {bc[1][2]}
     ---------
     {bc[2][0]} | {bc[2][1]} | {bc[2][2]}
     
     The number refers to each position in the board
     Stat with "{letter}" chose your position
    '''


def game(player):
    global bc
    choice = input(show_board(player))
    if choice == str:
        print("Make another choice")
    else:
        choice_index = int(choice)
        if 1 <= choice_index <= 3:
            bc[0][choice_index - 1] = player
        elif 4 <= choice_index <= 6:
            bc[1][choice_index - 4] = player
        elif 7 <= choice_index <= 9:
            bc[2][choice_index - 7] = player
        else:
            print("Make another choice")


def player_turn():
    global turn
    if turn % 2 == 0:
        game("O")
    else:
        game("X")
    turn += 1


def verify_win():
    global game_on
    for i in range(3):
        if bc[i][0] == bc[i][1] == bc[i][2]:
            input(f"Player: {bc[i][0]} win")
            game_on = False
        elif bc[0][i] == bc[1][i] == bc[2][i]:
            input(f"Player: {bc[0][i]} win")
            game_on = False
    if bc[0][0] == bc[1][1] == bc[2][2]:
        input(f"Player: {bc[0][0]} win")
        game_on = False
    elif bc[0][2] == bc[1][1] == bc[2][0]:
        input(f"Player: {bc[0][2]} win")
        game_on = False


while game_on:
    player_turn()
    verify_win()
