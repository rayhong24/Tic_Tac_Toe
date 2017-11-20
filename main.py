import numpy as np

def query_board(pos):
    row = int(move[0]) - 1
    col = int(move[1]) - 1
    return board[row, col]


def row_and_col(move):
    row = int(move[0]) - 1
    col = int(move[1]) - 1
    return row, col

def print_board():
    list = []
    for w in board:
        for x in w:
            if x == 1:
                list.append("X")
            elif x == 0:
                list.append(" ")
            elif x == -1:
                list.append("O")
    print("\n", list[0], "|", list[1], "|", list[2], "\n", list[3], "|", list[4], "|", list[5], "\n", list[6], "|", list[7], "|", list[8])

board = np.zeros([3, 3])
valid = ['11', '12', '13', '21', '22', '23', '31', '32', '33']

print("jack sucks")
while True:
    if (sum(sum(board))) == 1:
        print("It's O to move")
    if (sum(sum(board))) == 0:
        print("It's X to move")
    move = input("Input a move:")
    if move not in valid or query_board(move) != 0:
        print("That was invalid, try again,")
        print("These are the valid move in their corresponding positions", "\n", 11, "|", 12, "|", 13, "\n", 21, "|",
              22, "|", 23, "\n", 31, "|", 32, "|", 33)
        print("The current position is:")
        print_board()
    elif (sum(sum(board))) == 0:
        if query_board(move) == 0:
            insert_1 = row_and_col(move)
            board[insert_1] = 1
            print_board()

    elif (sum(sum(board))) == 1:
        if query_board(move) == 0:
            insert_2 = row_and_col(move)
            board[insert_2] = -1
            print_board()

    if np.any(np.sum(board, axis=0) == 3) \
            or np.any(np.sum(board, axis=1) == 3) \
            or np.any(np.sum(np.diag(board)) == 3) \
            or np.any(np.sum(np.diag(np.fliplr(board))) == 3):
        print("X won!!!")
        break

    if np.any(np.sum(board, axis=0) == -3) \
            or np.any(np.sum(board, axis=1) == -3) \
            or np.any(np.sum(np.diag(board)) == -3) \
            or np.any(np.sum(np.diag(np.fliplr(board))) == -3):
        print("O won!!!")
        break
    # if sum(board[0]) == 3 or sum(board[1]) == 3 or sum(board[2]) == 3:
    #     print("X won!!!")
    #     break
    # if board[0,0] + board[1,0] + board[2,0] == 3 or board[0,1] + board[1,1] + board[2,1] == 3 or board[0,2] + board[1,2] + board[2,2] == 3:
    #     print("X won!!!")
    #     break
    # if board[0,0] + board[1,1] + board[2,2] == 3 or board[2,0] + board[1,1] + board[0,2] == 3:
    #     print("X won!!!")
    #     break
    # if sum(board[0]) == -3 or sum(board[1]) == -3 or sum(board[2]) == -3:
    #     print("O won!!!")
    #     break
    # if board[0,0] + board[1,0] + board[2,0] == -3 or board[0,1] + board[1,1] + board[2,1] == -3 or board[0,2] + board[1,2] + board[2,2] == -3:
    #     print("O won!!!")
    #     break
    # if board[0,0] + board[1,1] + board[2,2] == -3 or board[2,0] + board[1,1] + board[0,2] == -3:
    #     print("O won!!!")
    #     break
    if 0 not in board:
        print("The game ends in a tie.")
        break