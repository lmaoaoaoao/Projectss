#PvP

def step_p(board, size, actor_1):
    if actor_1:
        print('    The ✕ turn')
    else:
        print('    The O turn')

    while True:
        #location
        print ('Enter the line', end = '')
        lin = int(input(' - ')) - 1
        col = int(input('And the column - ')) - 1

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


import random as r
#PvE

def step_b(board, size, actor_1):
    print('    The O turn (bot)')

    while True:
        #location
        lin = r.randint(0, size-1)
        col = r.randint(0, size-1)

        if board[lin][col] == '□':
            print (f'The line - {lin+1}, and the column - {col+1}')
            break


    board[lin][col] = 'O'
    actor_1 = True

    print ('', end = '\n\n')
    return actor_1