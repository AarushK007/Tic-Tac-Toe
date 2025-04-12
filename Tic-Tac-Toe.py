#initialising the board
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

key = [
    ["a", [1, 1]],
    ["b", [1, 2]],
    ["c", [1, 3]],
    ["d", [2, 1]],
    ["e", [2, 2]],
    ["f", [2, 3]],
    ["g", [3, 1]],
    ["h", [3, 2]],
    ["i", [3, 3]]
]

inputs = "abcedfghi"

def show():
    for j in board:
        print(j)

def player1move():
    while True:
        player = input().lower()[0]
        if (player not in inputs):
            print("Invalid input. Please try again.")
            continue
        for i in key:
            if player == i[0]:
                index = i[1]
        if board[index[0] - 1][index[1] - 1] != ' ':
            print("This spot is already filled. Please try again.")
            continue
        else:
            break
    board[int(index[0]) - 1][int(index[1]) - 1] = "X"
    show()

def player2move():
    while True:
        player = input().lower()[0]
        if (player not in inputs):
            print("Invalid input. Please try again.")
            continue
        for i in key:
            if player == i[0]:
                index = i[1]
        if board[index[0] - 1][index[1] - 1] != ' ':
            print("This spot is already filled. Please try again.")
            continue
        else:
            break
    board[int(index[0]) - 1][int(index[1]) - 1] = "O"
    show()

def wincondition():
    global winning
    winner = ""
    winning = False
    for i in board:
        if (i[0] == i[1] == i[2] != " "):
            winner = i[0]
            winning = True
            break
    for i in range(3):
        if (board[0][i] == board[1][i] == board[2][i] != " "):
            winner = board[0][i]
            winning = True
            break
    if ((board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0]) and (board[1][1] != " ")):
        winner = board[1][1]
    if winner == "X":
        print("Player 1 is the winner.")
    elif winner == "O":
        print("Player 2 is the winner.")
    elif counter == 9:
        print("It's a draw.")
        winning = "Draw"

counter = 0
print("""This is the board:
[a, b, c],
[d, e, f],
[g, h, i]""")

while True:
    player1move()
    counter += 1
    wincondition()
    if winning != False:
        break
    player2move()
    counter += 1
    wincondition()
    if winning != False:
        break