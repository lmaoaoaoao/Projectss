#for x
def winx(board, size):

    winx = False

    #by lines
    for e in range (size):

        for f in range (size-2):

            if board[e][f] == '✕':
                if board[e][f+1] == '✕':
                    if board[e][f+2] == '✕':
                        winx = True

            f += 1
        e += 1

    #by columnes
    for e in range (size-2):

        for f in range (size):

            if board[e][f] == '✕':
                if board[e+1][f] == '✕':
                    if board[e+2][f] == '✕':
                        winx = True

            f += 1
        e += 1
    
    #by diagonal 1
    for e in range (size-2):

        for f in range (size-2):

            if board[e][f] == '✕':
                if board[e+1][f+1] == '✕':
                    if board[e+2][f+2] == '✕':
                        winx = True

            f += 1
        e += 1
    
    #by diagonal 2
    for e in range (size-2):

        for f in range (size-2):

            if board[e+2][f] == '✕':
                if board[e+1][f+1] == '✕':
                    if board[e][f+2] == '✕':
                        winx = True

            f += 1
        e += 1

    return winx


#for o
def wino(board, size):

    wino = False

    #by lines
    for e in range (size):

        for f in range (size-2):

            if board[e][f] == 'O':
                if board[e][f+1] == 'O':
                    if board[e][f+2] == 'O':
                        wino = True

            f += 1
        e += 1

    #by columnes
    for e in range (size-2):

        for f in range (size):

            if board[e][f] == 'O':
                if board[e+1][f] == 'O':
                    if board[e+2][f] == 'O':
                        wino = True

            f += 1
        e += 1
    
    #by diagonal 1
    for e in range (size-2):

        for f in range (size-2):

            if board[e][f] == 'O':
                if board[e+1][f+1] == 'O':
                    if board[e+2][f+2] == 'O':
                        wino = True

            f += 1
        e += 1
    
    #by diagonal 2
    for e in range (size-2):

        for f in range (size-2):

            if board[e+2][f] == 'O':
                if board[e+1][f+1] == 'O':
                    if board[e][f+2] == 'O':
                        wino = True

            f += 1
        e += 1

    return wino
    


