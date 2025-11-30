board = []


''' Creating board '''
#the size
print ('Enter the board size: ', end = '')
while True:
    size = int(input())
    if 3 <= size <= 9:
        break
    else:
        print ('Invalid size. Tru again - ', end = '')

#line by line
for b in range (size):
    line = []
    for a in range (size):
        line.append('□')
        a += 1

    board.append(line)
    b += 1
''''''

''' Functions '''
#board show
def b_show():
    print ('  ', end = '')
    for k in range (size):
        print (k, end = ' ')
    print('')

    for c in range (size):
        print (c, end = ' ')
        for d in range (size):
            print (board[c][d], end = ' ')
            d += 1
        print ('')
        c += 1
    
    print ('', end = '\n\n')

#player select & move
actor_1 = True
def step(actor_1):
    while True:
        if actor_1:
            print('The ✕ turn')
        else:
            print('The O turn')

        #location
        print ('Enter the line', end = '')
        lin = int(input(' - '))
        col = int(input('And the column - '))

        #check
        if lin < 0:
            print ('Invalid location. Too low line')
        elif lin >= size:
            print ('Invalid location. Too high line')
        elif col < 0:
            print ('Invalid location. Too low column')
        elif col >= size:
            print ('Invalid location. Too high column')
        elif board[lin][col] != '□':
            print ('Invalid location. Occupied')
        else:
            break

    #player select
    if actor_1:
        board[lin][col] = '✕'
        actor_1 = False
    else:
        board[lin][col] = 'O'
        actor_1 = True

    print ('', end = '\n\n')
    return actor_1

#who win's?

#for x
def winx():
    win = False

    #by lines
    for e in range (size):

        for f in range (size-2):

            if board[e][f] == '✕':
                if board[e][f+1] == '✕':
                    if board[e][f+2] == '✕':
                        win = True

            f += 1
        e += 1

    #by columnes
    for e in range (size-2):

        for f in range (size):

            if board[e][f] == '✕':
                if board[e+1][f] == '✕':
                    if board[e+2][f] == '✕':
                        win = True

            f += 1
        e += 1
    
    #by diagonal 1
    for e in range (size-2):

        for f in range (size-2):

            if board[e][f] == '✕':
                if board[e+1][f+1] == '✕':
                    if board[e+2][f+2] == '✕':
                        win = True

            f += 1
        e += 1
    
    #by diagonal 2
    for e in range (size-2):

        for f in range (size-2):

            if board[e+2][f] == '✕':
                if board[e+1][f+1] == '✕':
                    if board[e][f+2] == '✕':
                        win = True

            f += 1
        e += 1
    
    return win

#for o
def wino():
    win = False

    #by lines
    for e in range (size):

        for f in range (size-2):

            if board[e][f] == 'O':
                if board[e][f+1] == 'O':
                    if board[e][f+2] == 'O':
                        win = True

            f += 1
        e += 1

    #by columnes
    for e in range (size-2):

        for f in range (size):

            if board[e][f] == 'O':
                if board[e+1][f] == 'O':
                    if board[e+2][f] == 'O':
                        win = True

            f += 1
        e += 1
    
    #by diagonal 1
    for e in range (size-2):

        for f in range (size-2):

            if board[e][f] == 'O':
                if board[e+1][f+1] == 'O':
                    if board[e+2][f+2] == 'O':
                        win = True

            f += 1
        e += 1
    
    #by diagonal 2
    for e in range (size-2):

        for f in range (size-2):

            if board[e+2][f] == 'O':
                if board[e+1][f+1] == 'O':
                    if board[e][f+2] == 'O':
                        win = True

            f += 1
        e += 1
    
    return win

''''''





b_show()
while True:
    actor_1 = step(actor_1)
    b_show()
    if winx():
        print ("The ✕  - WIN'S!")
        break
    elif wino():
        print ("The O  - WIN'S!")
        break
