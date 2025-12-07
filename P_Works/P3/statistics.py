import os
import the_winner as w

def stat(choice, board, size, actor_1, step_count):

    
    if not (os.path.isdir('/Users/User/Desktop/Education/Python/projectss/P_Works/P3/statistics')):
            os.mkdir('/Users/User/Desktop/Education/Python/projectss/P_Works/P3/statistics')


    if choice == 1:

        file = open('/Users/User/Desktop/Education/Python/projectss/P_Works/P3/statistics/PvP.txt', 'a')


        if actor_1:
            file.write('The first player: X\n\n')
        else:
            file.write('The first player: O \n\n')

        file.write(f"Size of board: {size}!\n\n")

        if w.winx(board, size):    
            file.write(f"The X - WIN'S in {step_count} steps!\n\n\n\n")

        elif w.wino(board, size):
            file.write(f"The O - WIN'S in {step_count} steps!\n\n\n\n")

        elif w.draw(board, size):
            file.write(f"Draw in {step_count} steps!\n\n\n\n")



        file.close()




    elif choice == 2:

        file = open('/Users/User/Desktop/Education/Python/projectss/P_Works/P3/statistics/PvE.txt', 'a')


        if actor_1:
            file.write('The first player: Player\n\n')
        else:
            file.write('The first player: Bot \n\n')

        file.write(f"Size of board: {size}!\n\n")

        if w.winx(board, size):    
            file.write(f"The Player - WIN'S in {step_count} steps!\n\n\n\n")

        elif w.wino(board, size):
            file.write(f"The Bot - WIN'S in {step_count} steps!\n\n\n\n")

        elif w.draw(board, size):
            file.write(f"Draw in {step_count} steps!\n\n\n\n")


        file.close()