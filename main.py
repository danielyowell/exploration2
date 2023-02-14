import random

def threeCheck(board, array):
    count = 0
    for i in range( len(array) ):
        if board[array[i]] == 'X':
            count = count + 1
    if count == 3:
        return True

def horiCheck(board):
    print("BEGIN HORICHECK")
    hwin1 = [0,1,2]
    hwin2 = [3,4,5]
    hwin3 = [6,7,8]

    if threeCheck(board, hwin1):
        return True
    if threeCheck(board, hwin2):
        return True
    if threeCheck(board, hwin3):
        return True
    return False

def vertCheck(board):

    vwin1 = [0,3,6]
    vwin2 = [1,4,7]
    vwin3 = [2,5,8]

    if threeCheck(board, vwin1):
        return True
    if threeCheck(board, vwin2):
        return True
    if threeCheck(board, vwin3):
        return True
    return False

def diagCheck(board):

    dwin1 = [0,4,8]
    dwin2 = [2,4,6]

    if threeCheck(board, dwin1):
        return True
    if threeCheck(board, dwin2):
        return True
    return False

def resetBoard(board):
    board = ["_" for i in range(9)]
    return board

# if the board has 3 Xs in a row
def gameWon(board):
    if horiCheck(board):
        return True
    if vertCheck(board):
        return True
    if diagCheck(board):
        return True
    return False

def main():
# local variables
    board = ["_" for i in range(9)]
    print("hello world")
    print(board)
    print(board[8])
    moves = 0

    while gameWon(board) == False:
        action = random.choice(range(9))
        print("action: ", action)
        if board[action] != 'X':
            board[action] = 'X'
            moves = moves + 1
    print("New board: ", board)
    print("Total moves: ", moves)
    board = resetBoard(board)
    
    print("program complete")

if __name__ == '__main__':
    main()