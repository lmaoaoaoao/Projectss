board = []



print ('Enter the board size:', end = '')
while True:
    size = int(input())
    if 3 <= size <= 9:
        break
    else:
        print ('Invalid size. Tru again -', end = '')


line = []
for i in range (size):
    line.append('•')
    i += 1
    
for i in range (size):
    board.append(line)
    i += 1






i = 0
while i < size:    
    j = 0
    while j < size:
        print (board[i][j], end = ' ')
        j += 1
    print ('')
    i += 1
