board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
player = 1
Game = 0
Mark = 'X'

#This Function Draws Game Board
def DrawBoard():
    print(" %c | %c | %c " % (board[1],board[2],board[3]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[4],board[5],board[6]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[7],board[8],board[9]))
    print("   |   |   ")

#This Function Checks position is empty or not
def CheckPosition(x):
    if(board[x] == ' '):
        return True
    else:
        return False

    #This Function Checks player has won or not
def CheckWin():
    global Game
    #Horizontal winning condition
    if(board[1] == board[2] and board[2] == board[3] and board[1] != ' '):
        Game = 1
    elif(board[4] == board[5] and board[5] == board[6] and board[4] != ' '):
        Game = 1
    elif(board[7] == board[8] and board[8] == board[9] and board[7] != ' '):
        Game = 1
        #Vertical Winning Condition
    elif(board[1] == board[4] and board[4] == board[7] and board[1] != ' '):
        Game = 1
    elif(board[2] == board[5] and board[5] == board[8] and board[2] != ' '):
        Game = 1
    elif(board[3] == board[6] and board[6] == board[9] and board[3] != ' '):
        Game=1
        #Diagonal Winning Condition
    elif(board[1] == board[5] and board[5] == board[9] and board[5] != ' '):
        Game = 1
    elif(board[3] == board[5] and board[5] == board[7] and board[5] != ' '):
        Game=1
        #Match Tie or Draw Condition
    elif(board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' ' and board[9]!=' '):
        Game=2
    else:
        Game=0

print("Player 1 [X] --- Player 2 [O]\n")
print()
print()
print("Please Wait...")
while(Game == 0):
    DrawBoard()
    if(player % 2 != 0):
        print("Player 1's chance")
        Mark = 'X'
    else:
        print("Player 2's chance")
        Mark = 'O'
    choice = int(input("Enter the position between [1-9] where you want to mark : "))
    if(CheckPosition(choice)):
        board[choice] = Mark
        player+=1
        CheckWin()

DrawBoard()
if(Game==2):
    print("Game Draw")
elif(Game==1):
    player-=1
    if(player%2!=0):
        print("Player 1 Won")
    else:
        print("Player 2 Won")