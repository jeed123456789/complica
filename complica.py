import random
# Complica, a variant of Connect Four
# Making the 6 x 3 gameboard
#innerlist = column
#outerlist = row
# X = first player
# O = computer

def makeBoard(FINAL_ROW,FINAL_COL):
    gameboard= []
    temp = []
    for i in range(FINAL_ROW):
        for j in range(FINAL_COL):
            temp.append(' ')
        gameboard.append(temp)
        temp = []
    return gameboard

def updateBoard(gameboard, row, col, piece):
    gameboard[row][col] = piece

def checkNextOpen(gameboard, FINAL_ROW, col):
    for r in range(FINAL_ROW-1,-1,-1):
        if gameboard[r][col] == ' ':
            return r

def printBoard(gameboard, dec1, dec2, FINAL_ROW, FINAL_COL):
    print(dec1)
    for i in range(FINAL_ROW):
        for j in range(FINAL_COL):
            dec2= dec2+gameboard[i][j]+'|'
        print(dec2)
        print(dec1)
        dec2 = '|'

def checkWinner(gameboard,piece,FINAL_ROW,FINAL_COL):
    # Check for horizontals
    if FINAL_COL>3:
        for i in range(FINAL_ROW):
            for j in range(FINAL_COL-3):
                if gameboard[i][j] == gameboard[i][j+1] == gameboard[i][j+2] == gameboard[i][j+3] == piece:
                    return True
    # Check for verticals
    if FINAL_ROW > 3:
        for i in range(FINAL_ROW-3):
            for j in range(FINAL_COL):
                if gameboard[i][j] == gameboard[i+1][j] == gameboard[i+2][j] == gameboard[i+3][j] == piece:
                    return True
    # Check for diagonals
    if FINAL_ROW > 3 and FINAL_COL > 4:
        for i in range(FINAL_ROW-3):
            for j in range(FINAL_COL-3):
                if gameboard[i][j] == piece and gameboard[i+1][j+1] == piece and gameboard[i+2][j+2] == piece and gameboard[i+3][j+3] == piece:
                    return True
        for i in range(3,FINAL_ROW):
            for j in range(FINAL_COL-3):
                if gameboard[i][j] == 'X' and gameboard[i-1][j+1] == 'X' and gameboard[i-2][j+2] == 'X' and gameboard[i-3][j+3] == 'X':
                    return True

print('Hello, user! Welcome to playing the game of Complica!')
print('Complia is a variant of Connect Four which once a Complica column is full, subsequent chips into that column push lowerlevel chips out')
print('columns are essentially an infinite queue with limited space.')
FINAL_ROW= int(input('State the numbers of rows you want in the gameboard: '))
FINAL_COL = int(input('State the number of columns you want in the gameboard: '))
print('Your piece is X.')
player_win = False
comp_win = False
# Making the board
gameboard =makeBoard(FINAL_ROW,FINAL_COL)
dec1 = '+-'*FINAL_COL+'+'
dec2 = '|'
print(dec1)
for i in range(FINAL_ROW):
    print('| '*FINAL_COL+'|')
    print(dec1)
turn = 0
noWinner = True
row = 0
while noWinner:
    # Ask user for input
    if turn==0:
        col = int(input('Player1, choose your column (0-'+str(FINAL_COL-1)+'): '))
        if col > FINAL_COL-1:
            print('That is not an available choice. Choose another column.')
        else:
        # putting user input into the board
            # if the column is not filled up
            if gameboard[0][col] == ' ':
                row = checkNextOpen(gameboard, FINAL_ROW, col)
                updateBoard(gameboard,row,col,'X')
                turn = 1
                printBoard(gameboard,dec1,dec2,FINAL_ROW,FINAL_COL)
                print()
            # if the column is filled up
            else:
                for r in range(FINAL_ROW-2,-1,-1):
                    gameboard[r+1][col] = gameboard[r][col]
                updateBoard(gameboard,0,col,'X')
                printBoard(gameboard,dec1,dec2,FINAL_ROW,FINAL_COL)
                print()
                turn = 1
    # Computer's turn
    else:
        comp_col = random.randint(0,FINAL_COL-1)
        # if the column is not filled up
        if gameboard[0][col] == ' ':
            row = checkNextOpen(gameboard, FINAL_ROW,comp_col)
            updateBoard(gameboard,row,comp_col,'O')
            turn = 0
            printBoard(gameboard,dec1,dec2,FINAL_ROW,FINAL_COL)
            print()
        # if the column is filled up
        else:
            for r in range(FINAL_ROW-2,-1,-1):
                gameboard[r+1][comp_col] = gameboard[r][comp_col]
            updateBoard(gameboard,0,comp_col,'O')
            printBoard(gameboard,dec1,dec2,FINAL_ROW,FINAL_COL)
            print()
            turn = 0
    # Checking for winner(s)
    if checkWinner(gameboard,'X',FINAL_ROW,FINAL_COL):
        player_win = True
        noWinner = False
    if checkWinner(gameboard,'O',FINAL_ROW,FINAL_COL):
        comp_win = True
        noWinner = False
#Printing the result of the game
if player_win and comp_win:
    print('The game tied')
elif player_win:
    print('You win! Congrats!')
elif comp_win:
    print('You lost! Try again!')
