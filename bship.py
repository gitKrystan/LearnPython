from random import randint

#Create board
board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

#Place ship
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

#Start Game
turn = 0
print "Let's play Battleship!"
print_board(board)

#Game Loop for 10 turns
for turn in range(10):
    print "\n***Turn " + str(turn + 1) + "***"
    #Make guess
    guess_row = int(raw_input("Guess Row:")) - 1
    guess_col = int(raw_input("Guess Column:")) - 1
    #Check guess
    if guess_row == ship_row and guess_col == ship_col:
        print "\nCongratulations! You sunk my battleship!\n"
        break
    #Validate guess
    else:
        if (guess_row not in range(5)) or \
            (guess_col not in range(5)):
            print "\nOops, that's not even in the ocean.\n"
        elif(board[guess_row][guess_col] == "X"):
            print "\nYou guessed that one already.\n"
        #Miss
        else:
            print "\nYou missed my battleship!\n"
            board[guess_row][guess_col] = "X"
        if turn == 4:
            print "\n***Game Over***"
        print_board(board)
