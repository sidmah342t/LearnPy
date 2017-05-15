import random

B = '\033[30m'
G = '\033[32m' # green
O = '\033[33m' # orange

def init_board():
    bl = []

    for i in range(1,10):
        bl.append(str(i))
    # print (bl)

    return bl

def clearboard(bl):
    bl.clear()


def print_curr_pos_board():
    print(' ' + board[0] + '   |' + '  ' + board[1] + '  |' + '  ' + board[2])
    print('-----|-----|-----')
    print(' ' + board[3] + '   |' + '  ' + board[4] + '  |' + '  ' + board[5])
    print('-----|-----|-----')
    print(' ' + board[6] + '   |' + '  ' + board[7] + '  |' + '  ' + board[8])

def make_move(b,p,s):
    b[p-1] = s

def rolldice():
    return random.randint(1,7)

def check_game_end(b,s):
    # 1,2,3 1,4,7 1,5,9 2,5,8, 3,6,9 3,5,7 game won
    # All positions filled except one, game drawn if no one has won
    if b[0] == s  and b[1] == s and b[2] == s:
        return False
    elif b[0] == s  and b[3] == s and b[6] == s:
        return False
    elif b[0] == s  and b[4] == s and b[8] == s:
        return False
    elif b[1] == s  and b[4] == s and b[7] == s:
        return False
    elif b[2] == s  and b[5] == s and b[8] == s:
        return False
    elif b[2] == s  and b[4] == s and b[6] == s:
        return False
    elif b.count(s) >= 8:
        return False
    else:
        return True



class Player:

    def __init__(self, pname,pmark,pturn):
        self.pname = pname
        self.pmark = pmark
        self.pturn = pturn

# Main Program

print('----------------------------------------------------------------------------')
print ('Welcome !! . Let us set up Players and who plays first by rolling dice')


p1 = input('Enter Player 1 name:');
p2 = input('Enter Player 2 name:');

d1 = d2 = 0
while d1 == d2:
        print('Player 1 ' + p1 + ' Rolling dice:')
        d1 = rolldice();
        print('Player 1 ' + p1 + ' Rolled :' + str(d1))
        print('Player 2 ' + p2 + ' Rolling dice:')
        d2 = rolldice();
        print('Player 2 ' + p2 + ' Rolled :' + str(d2))

else:
        if d1>d2:
            print(p1 + ' goes first')
            Play1 = Player(p1,'X',True)
            Play2 = Player(p2,'O',False)
        else:
            print(p2 + ' goes first')
            Play1 = Player(p2, 'X',True)
            Play2 = Player(p1, 'O',False)


print('----------------------------------------------------------------------------')
print ('Welcome !! . Let us start. The Board is displayed for you now')
board = init_board()
aslots = board[:] # make sure this is not referenced
print('Available slots :' + str(aslots))
print_curr_pos_board()

print('----------------------------------------------------------------------------')
print ('Start the Game: ' + Play1.pname + ' Your Marker is :' + Play1.pmark + ' Your Turn:' + str(Play1.pturn))

# Loop it from here till game gets over
game = True
while game:


    if Play1.pturn:
        if aslots == []:
            print (O+'Game Drawn'+B)
            break
        print(Play1.pname + ' Available slots :' + str(aslots))
        p = int(input(Play1.pname + ' Enter a number from available::\n'))
        while str(p) not in aslots:
            p = int(input('Invalid entry :' + Play1.pname + ' Re-enter a number from available slots:\n'))

        else:
            make_move(board, p, Play1.pmark)
            print_curr_pos_board()
            print(aslots)
            aslots.remove(str(p))
            print('Slots available post move ' + str(aslots))
            Play1.pturn = False
            Play2.pturn = True
            game = check_game_end(board,Play1.pmark)
            if (game == False):
                print(G + Play1.pname + ' won !!!! Hurray!!!!'+B)
    else:
        if aslots == []:
            print(O+'Game Drawn!!!!!!!'+B)
            break
        print(Play2.pname + ' Available slots :' + str(aslots))
        p = int(input(Play2.pname + ' Enter a number from available:\n'))
        while str(p) not in aslots:
            p = int(input('Invalid entry:' + Play2.pname + ' ReEnter a number from available slots:\n'))

        else:
            make_move(board, p, Play2.pmark)
            print_curr_pos_board()
            print(aslots)
            aslots.remove(str(p))
            print('Slots available post move ' + str(aslots))
            Play1.pturn = True
            Play2.pturn = False
            game = check_game_end(board, Play1.pmark)
            if(game == False):
                print(G + Play2.pname + ' won!!!! Hurray!!!!'+B)

    print('----------------------------------------------------------------------------')
    game = check_game_end(board,Play1.pmark)
    print('Game Position :' + str(game))

    ## print('Checking if game is won or drawn. This has to be a loop condition')
    ## print('Continue if game not won or drawn else exit')

# Loop ends here

print('----------------------------------------------------------------------------')
print('Final Game Position:')
print_curr_pos_board()

print('----------------------------------------------------------------------------')
print ('Okay !! . Let us clear the Board. The Board is displayed afresh for you now')
clearboard(board)
board = init_board()
aslots = board[:]
print('Available slots :' + str(aslots))
print_curr_pos_board()