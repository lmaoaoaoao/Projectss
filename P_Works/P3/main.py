board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

size = 3



'''
print ('Enter the board size:', end = '')
while True:
    size = int(input())
    if 3 <= size <= 9:
        break
    else:
        print ('Invalid size. Tru again -', end = '')


i = 0
while i < size:
    board.append('•')
    i += 1
'''

# print (board[1][1])



i = 0
while i < size:    
    j = 0
    while j < size:
        print (board[i][j], end = ' ')
        j += 1
    print ('')
    i += 1
