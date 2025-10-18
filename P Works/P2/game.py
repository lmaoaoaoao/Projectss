from tkinter import *
from random import *

#создание и настройка главного окна
window = Tk() #создание окна

window.title('game v0.2') #имя окна

window.geometry('600x400') #размер
window.resizable(0,0) #запрет на изменение размера окна

window.config(bg = 'lime') #цвет фона

#Функции
def sps():
    sps = ['Stone', 'Paper', 'Scissors']
    value = choice(sps)
    label_Text.configure (text=value)






#Виджеты

label_Text = Label(window, text='', fg ='white', font=('Comic Snas MS', 20), bg = "black")
label_Text.place(y=150, x=250)

stone = Button(window,
               text='Stone',
               font=('Comic Snas MS', 20), 
               bg = "white",
               command=sps
               )
stone.place(x=50, y=300)

paper = Button(window,
               text='Paper',
               font=('Comic Snas MS', 20), 
               bg = "white",
               command=sps
               )
paper.place(x=250, y=300)

scissors = Button(window,
               text='Scissors',
               font=('Comic Snas MS', 20), 
               bg = "white",
               command=sps
               )
scissors.place(x=450, y=300)



#конец прорграммы (запуск)
window.mainloop()