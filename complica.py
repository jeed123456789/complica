import random
# Complica, a variant of Connect Four
# Making the 6 x 3 gameboard
#innerlist = column
#outerlist = row
# X = first player
# O = computer

print('Hello, user! Welcome to playing the game of Complica!')
print('Complia is a variant of Connect Four which once a Complica column is full, subsequent chips into that column push lowerlevel chips out; columns are essentially an infinite queue with limited space.')
FINAL_ROW= int(input('State the numbers of rows you want in the gameboard: '))
FINAL_COL = int(input('State the number of columns you want in the gameboard: '))
player_win = False
comp_win = False
gameboard = [[' ']*FINAL_COL]*FINAL_ROW
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
        col = int(input('Player1, choose your column (0~'+str(FINAL_COL-1)+'): '))
        if col > FINAL_COL-1:
            print('That is not an available choice. Choose another column.')
        else:
        # putting user input into the board
            # if the column is not filled up
            if gameboard[0][col] == ' ':
                for r in range(FINAL_ROW-1,-1,-1):
                    if gameboard[r][col] == ' ':
                        row = r
                        break
                print(row)
                gameboard[row][col] = 'X'
                print('filled user piece into board' )
                print(gameboard)
                turn = 1
                print(dec1)
                for i in range(FINAL_ROW):
                    for j in range(FINAL_COL):
                        dec2= dec2+gameboard[i][j]+'|'
                    print(dec2)
                    print(dec1)
                    dec2 = '|'
            # if the column is filled up 
            else: 
                for r in range(FINAL_ROW-2,-1,-1):
                    gameboard[r+1][col] = gameboard[r][col]
                gameboard[0][col] = 'X'
                turn = 1
                print(dec1)
                for i in range(FINAL_ROW):
                    for j in range(FINAL_COL):
                        dec2= dec2+gameboard[i][j]+'|'
                    print(dec2)
                    print(dec1)
                    dec2 = '|'
    # Computer's turn
    else:
        comp_col = random.randint(0,FINAL_COL-1)
        # if the column is not filled up 
        if gameboard[0][col] == ' ':
            for r in range(FINAL_ROW-1,-1,-1):
                if gameboard[FINAL_ROW-r-1][comp_col] == ' ':
                    row = r
            gameboard[row][comp_col]= 'O'
            turn = 0
            print(dec1)
            for i in range(FINAL_ROW):
                for j in range(FINAL_COL):
                    dec2= dec2+gameboard[i][j]+'|'
                print(dec2)
                print(dec1)
                dec2 = '|'
        # if the column is filled up
        else:
            for r in range(FINAL_ROW-2,-1,-1):
                gameboard[r+1][comp_col] = gameboard[r][comp_col]
            gameboard[0][comp_col] = 'O'
            print(dec1)
            for i in range(FINAL_ROW):
                for j in range(FINAL_COL):
                    dec2= dec2+gameboard[i][j]+'|'
                print(dec2)
                print(dec1)
                dec2 = '|'
            turn = 0
    # Checking for winner(s)
    # Check for horizontals
    for i in range(FINAL_ROW):
        for j in range(FINAL_COL-3):
            if gameboard[i][j] == 'X' and gameboard[i][j+1] == 'X' and gameboard[i][j+2] == 'X' and gameboard[i][j+3] == 'X':
                player_win = True
                noWinner = False
                break
    for i in range(FINAL_ROW):
        for j in range(FINAL_COL-3):
            if gameboard[i][j] == 'O' and gameboard[i][j+1] == 'O' and gameboard[i][j+2] == 'O' and gameboard[i][j+3] == 'O':
                comp_win = True
                noWinner = False
                break
    # Check for verticals
    for i in range(FINAL_ROW-3):
        for j in range(FINAL_COL):
            if gameboard[i][j] == 'X' and gameboard[i+1][j] == 'X' and gameboard[i+2][j] == 'X' and gameboard[i+3][j] == 'X':
                player_win = True
                noWinner = False
                break
    for i in range(FINAL_ROW-3):
        for j in range(FINAL_COL):
            if gameboard[i][j] == 'O' and gameboard[i+1][j] == 'O' and gameboard[i+2][j] == 'O' and gameboard[i+3][j] == 'O':
                comp_win = True
                noWinner = False
                break
    # Check for diagonals
##    for i in range(FINAL_ROW-3):
##        for j in range(FINAL_COL-3):
##            if gameboard[i][j] == 'X' and gameboard[i+1][j+1] == 'X' and gameboard[i+2][j+2] == 'X' and gameboard[i+3][j+3] == 'X':
##                player_win = True
##                noWinner = False
##                break
##    for i in range(FINAL_ROW-3):
##        for j in range(FINAL_COL-3):
##            if gameboard[i][j] == 'O' and gameboard[i+1][j+1] == 'O' and gameboard[i+2][j+2] == 'O' and gameboard[i+3][j+3] == 'O':
##                comp_win = True
##                noWinner = False
##                break
##    for i in range(3,FINAL_ROW):
##        for j in range(FINAL_COL-3):
##            if gameboard[i][j] == 'X' and gameboard[i-1][j+1] == 'X' and gameboard[i-2][j+2] == 'X' and gameboard[i-3][j+3] == 'X':
##                player_win = True
##                noWinner = False
##                break
##    for i in range(3,FINAL_ROW):
##       for j in range(FINAL_COL-3):
##            if gameboard[i][j] == 'O' and gameboard[i-1][j+1] == 'O' and gameboard[i-2][j+2] == 'O' and gameboard[i-3][j+3] == 'O':
##                comp_win = True
##                noWinner = False
##                break
#Printing the result of the game
if player_win and comp_win:
    print('The game tied')
elif player_win:
    print('You win! Congrates!')
elif comp_win:
    print('You lost! Try again!')
        
