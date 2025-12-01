def b_size():
    print ('Enter the board size: ', end = '')
    
    while True:
        size = int(input())
        if 3 <= size <= 9:
            break
        else:
            print ('Invalid size. Tru again - ', end = '')
    
    return size






def c_board(board, size):


    #line by line
    for b in range (size):
        line = []
        for a in range (size):
            line.append('□')
            a += 1

        board.append(line)
        b += 1
    
    return board