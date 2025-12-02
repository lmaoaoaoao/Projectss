import os

import board_create as c
import board_show as sh
import moves as m
import act_rand
import the_winner as w




if not (os.path.isdir('/Users/User/Desktop/Education/Python/projectss/P_Works/P3/statistics')):
        os.mkdir('/Users/User/Desktop/Education/Python/projectss/P_Works/P3/statistics')





print ('')
print ('MAIN MENU')
print ('')
print ('1. player vs player')
print ('2. player vs bot')
print ('')
choice = int(input())
print ('')





while True:    
    step_count = 1

    actor_1 = act_rand.player()

    if choice == 1:
        
        file = open('/Users/User/Desktop/Education/Python/projectss/P_Works/P3/statistics/PvP.txt', 'a')

        # create/re-create & show board
        board = []
        size = c.b_size()
        board = c.c_board(board, size)
        sh.b_show(board, size)
        

        while True:
            print (f'The {step_count} step:')
            actor_1 = m.step_p(board, size, actor_1)
            sh.b_show(board, size)

            if w.winx(board, size):
                print (f"The ✕  - WIN'S in {step_count} steps!")
                file.write(f"The X - WIN'S in {step_count} steps!\n")
                break
            elif w.wino(board, size):
                print (f"The O  - WIN'S in {step_count} steps!")
                file.write(f"The O - WIN'S in {step_count} steps!\n")
                break
            elif w.draw(board, size):
                print (f"Draw in {step_count} steps!")
                file.write(f"Draw in {step_count} steps!\n")
                break

            
            step_count += 1

        file.close()

        

    elif choice == 2:
        file = open('/Users/User/Desktop/Education/Python/projectss/P_Works/P3/statistics/PvE.txt', 'a')

        # create/re-create & show board
        board = []
        size = c.b_size()
        board = c.c_board(board, size)
        sh.b_show(board, size)
        

        while True:
            print (f'The {step_count} step:')
            if actor_1:                    
                actor_1 = m.step_p(board, size, actor_1)
                sh.b_show(board, size)
            else:
                actor_1 = m.step_b(board, size, actor_1)
                sh.b_show(board, size)

            if w.winx(board, size):
                print (f"The ✕  (player) - WIN'S in {step_count} steps!")
                file.write(f"The X  (player) - WIN'S in {step_count} steps!!\n")
                break
            elif w.wino(board, size):
                print (f"The O  (bot) - WIN'S in {step_count} steps!")
                file.write(f"The O (bot) - WIN'S in {step_count} steps!\n")
                break
            elif w.draw(board, size):
                print (f"Draw in {step_count} steps!")
                file.write(f"Draw in {step_count} steps!\n")
                break

            step_count += 1

        file.close()
        


    elif choice == 3:
        print ('Game exit')
        break

    else:
        print ('Error! Try again')
    

    print ('')
    print ('MAIN MENU')
    print ('')
    print ('1. player vs player')
    print ('2. player vs bot')
    print ('3. exit')
    print ('')
    choice = int(input())
    print ('')
