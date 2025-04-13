#initialising the board
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

#displaying the board
def show():
    for j in board:
        print(j)

#making a move
def move(Cursor):
    while True: #making sure the input is valid
        player = int(input())
        if player not in range(1, 10): #so that the input doesn't go out of the range
            print("Invalid input. Please try again.")
            continue
        import math
        move = [(math.ceil(player / 3) - 1), ((player - 1) % 3)] #placing the x and y coordinates of the input
        if board[move[0]][move[1]] != ' ': #so that we don't overwrite an existing slot
            print("This spot is already filled. Please try again.")
            continue
        else:
            break
    board[move[0]][move[1]] = "X" if (Cursor % 2 == 0) else "O" #placing X and O accordingly
    show()

def wincondition():
    global winning
    winner = ""
    for i in board:
        if (i[0] == i[1] == i[2] != " "): #checking all rows for a match
            winner = i[0] #declaring the winning symbol
            winning = True
            break
    for i in range(3):
        if (board[0][i] == board[1][i] == board[2][i] != " "): #checking all columns for a match
            winner = board[0][i] #declaring the winning symbol
            winning = True
            break
    if ((board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0]) and (board[1][1] != " ")): #checking all diagonals for a match
        winner = board[1][1] #declaring the winning symbol
    if winner == "X":
        print("Player 1 is the winner.")
    elif winner == "O":
        print("Player 2 is the winner.")
    elif counter == 9: #if the board is full without any winners
        print("It's a draw.")
        winning = "Draw"

#initialising the constants
counter = 0
Cursor = 0
winning = False

print("""This is the board:
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]""")

while True:
    move(Cursor)
    counter += 1
    wincondition()
    if winning != False:
        break
    Cursor += 1