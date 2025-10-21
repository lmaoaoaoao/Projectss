from tkinter import *
from random import *

#создание и настройка главного окна
root = Tk() #создание окна

root.title('game v0.3') #имя окна

root.geometry('1280x360') #размер
root.resizable(0,0) #запрет на изменение размера окна

root.config(bg = '#FAFAD2') #цвет фона

#Диалоговые окна

text='Однажды утром вы получаете странное письмо от давно умершего дедушкё. \nВ письме говорится, что он спрятал семейную реликвию (старинную книгу) в архиве семьи. \nДедушка просит вас отправиться туда и вернуть книгу домой.'
text1='/Спустя некотрое время/'
text2='Вы стоите перед массивной дверью старого архива.\nЧтобы войти внутрь, вам нужно подобрать комбинацию замка.\nДверь охраняется тремя различными механизмами, каждый из которых требует особого подхода.'
text3='Механизм А:'




#Функции
def d_w1():
    label.configure (text=text1, font=('Times New Roman', 25))
    btn1.configure(command=d_w2)

def d_w2():
    label.configure (text=text2, font=('Comic Snas MS', 20))
    btn1.configure(command=d_w3)

def d_w3():
    label.configure (text=text3, font=('Times New Roman', 25))
    btn1.configure(command=d_w4)

def d_w4():
    label.configure (text='mhm', font=('Comic Snas MS', 20))
    btn1.pack_forget()   
    btnl.pack(anchor=SW,pady=20,padx=150)
    btn1.pack(side=BOTTOM,pady=20)
    btnr.pack(anchor=SE,pady=20,padx=150)

def d_w5():
    label.configure (text='tak-s')




#Виджеты

label = Label(root, text=text, fg ='white', font=('Comic Snas MS', 20), bg = "black")
label.pack(padx=20, pady=30)


btn1 = Button(root,
               text='Далее',
               font=('Comic Snas MS', 20), 
               bg = "white",
               command=d_w1
               )
btn1.pack(side=BOTTOM,pady=50)


btnl = Button(root,
               text='левый',
               font=('Comic Snas MS', 20), 
               bg = "white",
               command=d_w5
               )

btnc = Button(root,
               text='посередине',
               font=('Comic Snas MS', 20), 
               bg = "white",
               command=d_w5
               )

btnr = Button(root,
               text='справа',
               font=('Comic Snas MS', 20), 
               bg = "white",
               command=d_w5
               )




























#конец прорграммы (запуск)
root.mainloop()