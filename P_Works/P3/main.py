board = []


''' Creating board '''
#the size
print ('Enter the board size:', end = '')
while True:
    size = int(input())
    if 3 <= size <= 9:
        break
    else:
        print ('Invalid size. Tru again -', end = '')

#line by line
line = []
for i in range (size):
    line.append('•')
    i += 1

for i in range (size):
    board.append(line)
    i += 1
''''''








#board show
def b_show():
    print ('  ', end = '')
    for k in range (size):
        print (k + 1, end = ' ')
    print('')

    for i in range (size):
        print (i + 1, end = ' ')
        for j in range (size):
            print (board[i][j], end = ' ')
            j += 1
        print ('')
        i += 1
