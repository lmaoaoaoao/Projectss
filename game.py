from tkinter import *

#создание и настройка главного окна
window = Tk() #создание окна

window.title('game v0.1') #имя окна
window.iconbitmap('gameLogo.ico') #иконка окна

window.geometry('1200x600') #размер
window.resizable(0,0) #запрет на изменение размера окна

window.config(bg = 'lime') #цвет фона


#Виджеты

close_Button = Button(window,
                      width=20,
                      height=2,
                      text='quit',
                      command=quit,
                      font = ('Comic Sans MS', 20, 'italic'),
                      bg = 'purple',
                      activebackground='indigo',
                      fg='black',
                      activeforeground="green"
                      )
close_Button.pack()
close_Button.place(x = 850, y = 10)

label = Label(window,
                      width=20,
                      height=2,
                      text='quit',
                      font = ('Comic Sans MS', 20, 'italic'),
                      bg = 'purple',
                      fg='black'
                      )
label.pack()
label.place(x = 100, y = 10)



img = PhotoImage(file='gameLogo.png')
l_logo = Label(window, image=img)
l_logo.pack()






#конец прорграммы (запуск)
window.mainloop()