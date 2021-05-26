board=[]
for i in range(11):
    board.append(str(i))
def drawboard():
    print("               ||========================||")
    print("               ||  "     + board[7] + "    |    "  + board[8] + "   |   " + board[9],"  ||")
    print("               ||========================||")
    print("               ||  "     + board[4] + "    |    "  + board[5] + "   |   " + board[6],"  ||")
    print("               ||========================||")
    print("               ||  "     + board[1] + "    |    "  + board[2] + "   |   " + board[3],"  ||")
    print("               ||========================||")
def askside():
    print("Player 1, choose your side")
    player1=""
    while not(player1=="X" or player1=="O"):
        print("Choose X or O ")
        player1= input().upper()
    print("Player1 is "+player1)
    player2=""
    if player1=="X":
        player2="O"
    else:
        player2="X"
    print("Player2 is " + player2)
    return [player1,player2]

def askmove():
    validmove=[]
    for i in range(11):
        validmove.append(str(i))
    move=0
    while not(move in validmove):
        print("Make a move (1,9)")
        move=input()
    return int(move)
def winner(b,c):
   return (b[7]==c and b[8]==c and b[9]==c) or \
          (b[4]==c and b[5]==c and b[6]==c) or \
          (b[1]==c and b[2]==c and b[3]==c) or \
          (b[7]==c and b[4]==c and b[1]==c) or \
          (b[8]==c and b[5]==c and b[2]==c) or \
          (b[9]==c and b[6]==c and b[3]==c) or \
          (b[7]==c and b[5]==c and b[3]==c) or \
          (b[9]==c and b[5]==c and b[1]==c)
def gamecon():
    drawboard()
    sides=askside()
    turn="P1"
    p1choise=sides[0]
    p2choise=sides[1]
    gameplaying=True
    while gameplaying:
        if turn=="P1":
            print("\nPlayer 1 turn \n")
            moveindex=askmove()
            board[moveindex]=p1choise
            drawboard()
            if (winner(board,p1choise)):
                print("Player 1 Won")
                gameplaying=False
            turn="P2"
        elif turn=="P2":
            print("\n Player 2 turn \n")
            moveindex = askmove()
            board[moveindex] = p2choise
            drawboard()
            if (winner(board,p2choise)):
                print("Player 2 Won")
                gameplaying=False
            turn = "P1"


gamecon()