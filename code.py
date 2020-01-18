board_val = [1, 2, 3, 4, 5, 6, 7, 8, 9]
win_val = False


def board_print():

    print(str(board_val[0]) + "|" + str(board_val[1]) + "|" + str(board_val[2]))
    print(str(board_val[3]) + "|" + str(board_val[4]) + "|" + str(board_val[5]))
    print(str(board_val[6]) + "|" + str(board_val[7]) + "|" + str(board_val[8]))


def win_check():
    global win_val
    if board_val[0] == board_val[1] == board_val[2] or board_val[3] == board_val[4] == board_val[5] or board_val[6] == board_val[7] == board_val[8]:
        win_val = True
    elif board_val[0] == board_val[3] == board_val[6] or board_val[1] == board_val[4] == board_val[7] or board_val[2] == board_val[5] == board_val[8]:
        win_val = True
    elif board_val[0]== board_val[4] == board_val[8] or board_val[2] == board_val[4] == board_val[6]:
        win_val = True
    return win_val


def board_input(val):
    user_1 = int(input(f"Player {val} Input  ")) - 1
    while user_1 >= 9:
        print("Input out of Bound ")
        user_1 = int(input("Please enter a value from 1-9 ")) - 1
        while board_val[user_1] == "X" or board_val[user_1] == "O":
            user_1 = int(input("Player Input already exists ")) - 1
    while board_val[user_1] == "X" or board_val[user_1] == "O":
        user_1 = int(input("Player Input already exists ")) - 1
        while user_1 >= 9:
            print("Input out of Bound ")
            user_1 = int(input("Please enter a value from 1-9 ")) - 1
    if val == 1:
        board_val[user_1] = "X"
    else:
        board_val[user_1] = "O"
    board_print()
    print("\n")


def game_run():
    print("\n")
    print("User 1 input would be = X and User 2 input would be = O  \nPlease Enter the place on board where you want to place your mark \nFrom 1-9")
    board_print()
    while True:
        board_input(1)
        win = win_check()
        if win:
            print("Player 1 wins !!")
            break
        board_input(2)
        win = win_check()
        if win:
            print("Player 2 wins !!")
            break


def run():
    print("TicTacToe v1.0")
    print("1.Start Game \n2.End\n")
    x = input("Choose please  ")
    while x == "1":
        global board_val
        board_val = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        global win_val
        win_val = False
        game_run()
        print("------------------")
        print("1.Start Game \n2.End\n")
        x = input("Choose please ")


run()









