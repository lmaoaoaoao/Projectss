def b_show(board, size):
    print ('')
    print ('  ', end = '')
    for k in range (size):
        print (k+1, end = ' ')
    print('')

    for c in range (size):
        print (c+1, end = ' ')
        for d in range (size):
            print (board[c][d], end = ' ')
            d += 1
        print ('')
        c += 1
    
    print ('', end = '\n')