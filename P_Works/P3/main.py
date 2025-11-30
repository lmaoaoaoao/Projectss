print ('Enter the board size:', end = '')
while True:
    size = int(input())
    if 3 <= size <= 9:
        break
    else:
        print ('Invalid size. Tru again -', end = '')