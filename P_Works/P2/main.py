from tkinter import *

#создание и настройка главного окна
root = Tk() #создание окна

root.title('game v0.3') #имя окна

root.geometry('1280x360') #размер
root.resizable(0,0) #запрет на изменение размера

root.config(bg = '#FAFAD2') #цвет фона


#Контейнеры
frame1 = Frame(root, width=1280, height=180, bg = "#FAFAD2")
frame1.place(x=0, y=0)


frame2 = Frame(root, width=1280, height=180, bg = "#FAFAD2")
frame2.place(x=0, y=180)

frame_l = Frame(frame2, width=256, height=50, bg = "#FAFAD2")
frame_l.place(x=128, y=65)

frame_c = Frame(frame2, width=256, height=50, bg = "#FAFAD2")
frame_c.place(x=512, y=65)

frame_r = Frame(frame2, width=256, height=50, bg = "#FAFAD2")
frame_r.place(x=896, y=65)




#массивы

mechA = ['R_card', 'B_card', 'G_card']
mech_A = []
inventory = set()

#---Диалоговые окна
d_w = {
    "t0": 'Однажды вы получаете письмо от давно умершего дедушки. \n'
    'В письме говорится, что он спрятал старинную книгу в архиве семьи, которую, вам следует перечитать. \n'
    'Пост скриптум он попросил, забрать спецальную карту,\n'
    'котрую давно отдвал на хранение вместе с картой, оставленной в письме.',

    "t1": 'Вы получили <Красную карту> и <Записку> х2',

    "t2": 'Записка:\n'
    '<<P. P. S. Используй его в первую очередь очередь>>',

    "t3": 'Записка:\n'
    '<<P. P. P. S. Стеллаж Г, полка №2, книга выбивающаяся из ряда>>',

    "t4": 'Размышляя об этом письме всё утро,\n'
    'вы вспоминаете, что в детстве ваш дед в секрете от родных он отдал вам на хранение\n'
    'некий предмет . . .   <Зелёная Карта>',

    "t5": 'Через полчаса активного поиска, вы его находите',
    
    "t6": 'Вы получили <Зелёную карту>',
    
    "t7": 'Также вы отчётливо вспомнили слова дедушки, когда он давал вам его\n'
    '<<Когда найдёшь для чего он тебе нужен используй его в последнюю очередь>>',

    "t8": 'Вы решаете немедля поехать в архив семьи',
    
    "t9": '<<<Few hours later . . .>>>',
    
    "t10": '<<<Вы вошли в локацию "Вход в семейный архив">>>',
    
    "t11": 'Вы заметили, специальный механизм, куда надо вставить три карточки',

    "t12": 'Но так как у вас всего с собой 2 карты, вы решаете осмотреться', # осмотреться
    
    "t13": 'Под клубмой рядом с дверью вы находите 3-ью карту',

    "t14": 'Вы получили <Синюю карту>', # вернуться

    "t15": 'Вставьте карты в правильном порядке',

    "t_f": 'Неудача попробуйте ещё раз',

    "t_t": 'Успех! Двери открыты', #войти

    "t16": 'Пройдя через предбанник, вы оказываетесь внутри огромного лабиринта, наполненого стеллажами книг',

    "t17": '<<<Вы вошли в "семейный архив">>>', #осмотреться

    "t18": 'Вы видите таблички на стеллажах по обе стороны от вас',
    "t_l": 'Надпись <<Д>>',
    "t_r": 'Надпись <<Е>>',

    "t_l1": 'Надпись <<В>>',
    "t_r1": 'Надпись <<Г>>',

    "t19": 'На стеллаже 3 полки',

    "t20": 'Содержимое полки достаточно пыльное\n'
    'Ничего не разгядеть',

    "t21": 'Содержимое полки достаточно пыльное\n'
    'Но есть книга, на которой слой пыли неуловимо меньше',

    "t22": 'Содержимое полки достаточно пыльное\n'
    'Ничего не разгядеть',

    "t23": 'Вы получили <Очень пыльная книга>', #встряхнуть

    "t24": 'Вы получили <Потрёпанная книга>', #осмотреть

    "t25": 'Осмотрев книгу вы обнаруживаете, что это <Граф Монте Кристо>\n'
    'Вы вспоминаете, что дед и раньше давал вам ею прочитать, но тогда она вам очень понравилась\n'
    'Ведь она показалась вам достачно кровавой и жестокой',

    "t26": 'Но ради исполнения просьбы дедушки вы забираете её с собой, чтобы прочесть её ещё раз',

    "t27": 'Good ending'
}



#Функции
def d_w1():
    label.configure (text=d_w['t1'])
    btn1.configure(command=d_w2, text='Осмотреть')
    inventory.add('R_card')

def d_w2():
    label.configure (text=d_w['t2'])
    btn1.configure(command=d_w3, text='Далее')

def d_w3():
    label.configure (text=d_w['t3'])
    btn1.configure(command=d_w4)

def d_w4():
    label.configure (text=d_w['t4'])
    btn1.configure(command=d_w5, text='Искать')

def d_w5():
    label.configure (text=d_w['t5'])
    btn1.configure(command=d_w6, text='Далее')

def d_w6():
    label.configure (text=d_w['t6'])
    btn1.configure(command=d_w7)
    inventory.add('G_card')

def d_w7():
    label.configure (text=d_w['t7'])
    btn1.configure(command=d_w8)

def d_w8():
    label.configure (text=d_w['t8'])
    btn1.configure(command=d_w9)

def d_w9():
    label.configure (text=d_w['t9'])
    btn1.configure(command=d_w10)

def d_w10():
    label.configure (text=d_w['t10'])
    btn1.configure(command=d_w11)

def d_w11():
    label.configure (text=d_w['t11'])
    btn1.configure(command=d_w12, text='Oсмотреться')

def d_w12():
    label.configure (text=d_w['t12'])
    btn1.configure(command=d_w13, text='Далее')

def d_w13():
    label.configure (text=d_w['t13'])
    btn1.configure(command=d_w14)

def d_w14():
    label.configure (text=d_w['t14'])
    btn1.configure(command=d_w15)
    inventory.add('B_card')


def d_w15():
    label.configure (text=d_w['t15'])
    btn1.place_forget()
    btnrc.place(anchor=CENTER, relx=0.5, rely=0.5)
    btnbc.place(anchor=CENTER, relx=0.5, rely=0.5)
    btngc.place(anchor=CENTER, relx=0.5, rely=0.5)

def d_rc():
    if ("R_card" in inventory) and ("R_card" not in mech_A):
        mech_A.append('R_card')
        print ('Вы вставили: ', mech_A)
        d_w_check()
    
def d_gc():
    if "G_card" in inventory and ("G_card" not in mech_A):
        mech_A.append('G_card')
        print ('Вы вставили: ', mech_A)
        d_w_check()

def d_bc():
    if "B_card" in inventory and ("B_card" not in mech_A):
        mech_A.append('B_card')    
        print ('Вы вставили: ', mech_A)
        d_w_check()

def d_w_check():
    if ("R_card" in mech_A) and ("G_card" in mech_A) and ("B_card" in mech_A):
        if mech_A == mechA:
            label.configure (text=d_w['t_t'])
            btnrc.place_forget()
            btngc.place_forget()
            btnbc.place_forget()
            btn1.place(anchor=CENTER, relx=0.5, rely=0.5)
            btn1.configure(command=d_w16)
        else:
            label.configure (text=d_w['t_f'])
            mech_A.clear()

    
def d_w16():
    label.configure (text=d_w['t16'])
    btn1.configure(command=d_w17)

def d_w17():
    label.configure (text=d_w['t17'])
    btn1.configure(command=d_w18, text='Oсмотреться')


def d_w18():
    label.configure (text=d_w['t18'])
    btn1.place_forget()
    btn_с.place_forget()
    btn_l.configure(command=d_w_l, text='Осмотреть слева')
    btn_r.configure(command=d_w_r, text='Осмотреть справа')
    btn_l.place(anchor=CENTER, relx=0.5, rely=0.5)
    btn_r.place(anchor=CENTER, relx=0.5, rely=0.5)



def d_w_r():
    label.configure (text=d_w['t_r'])    
    btn_r.configure(command=d_w_r2, text='Пойти вправо')
    btn_l.place_forget()
    btn_с.place(anchor=CENTER, relx=0.5, rely=0.5)
def d_w_r2():
    label.configure (text='Похоже там нет ничего нужного нам')
    btn_l.place_forget()
    btn_r.place_forget()
    btn_с.place(anchor=CENTER, relx=0.5, rely=0.5)


def d_w_l():
    label.configure (text=d_w['t_l'])
    btn_r.place_forget()
    btn_l.configure(command=d_w_l_2, text='Пойти влево')
    btn_с.place(anchor=CENTER, relx=0.5, rely=0.5)


def d_w_l_2():
    label.configure (text=d_w['t18'])
    btn_l.place(anchor=CENTER, relx=0.5, rely=0.5)
    btn_l.configure(command=d_w_l_3, text='Осмотреть слева')
    btn_r.place(anchor=CENTER, relx=0.5, rely=0.5)
    btn_r.configure(command=d_w_r3, text='Осмотреть справа')
    btn_с.configure(command=d_w_l_2)
    btn_с.place_forget()

def d_w_l_3():
    label.configure (text=d_w['t_l1'])    
    btn_l.configure(command=d_w_l4, text='Пойти влево')
    btn_r.place_forget()
    btn_с.place(anchor=CENTER, relx=0.5, rely=0.5)
def d_w_l4():
    label.configure (text='Похоже там нет ничего нужного нам')
    btn_l.place_forget()
    btn_r.place_forget()
    btn_с.place(anchor=CENTER, relx=0.5, rely=0.5)


def d_w_r3():
    label.configure (text=d_w['t_r1'])    
    btn_r.configure(command=shelf, text='Осмотреть')
    btn_l.place_forget()
    btn_с.place(anchor=CENTER, relx=0.5, rely=0.5)


def shelf():
    label.configure (text=d_w['t19'])
    btn_l.place(anchor=CENTER, relx=0.5, rely=0.5)
    btn_с.place(anchor=CENTER, relx=0.5, rely=0.5)
    btn_r.place(anchor=CENTER, relx=0.5, rely=0.5)
    btn_l.configure(command=shelf1, text='Осмотреть полку №1')
    btn_с.configure(command=shelf2, text='Осмотреть полку №2')
    btn_r.configure(command=shelf3, text='Осмотреть полку №3')

def shelf1():
    label.configure (text=d_w['t20'])
    btn_l.place(anchor=CENTER, relx=0.5, rely=0.5)
    btn_l.place_forget()
    btn_с.configure(command=shelf, text='Вернуться')
    btn_r.place_forget()
def shelf2():
    label.configure (text=d_w['t21'])
    btn_l.place(anchor=CENTER, relx=0.5, rely=0.5)
    btn_l.place_forget()
    btn_с.configure(command=d_w23, text='Взять книгу')
    btn_r.place_forget()
def shelf3():
    label.configure (text=d_w['t22'])
    btn_l.place(anchor=CENTER, relx=0.5, rely=0.5)
    btn_l.place_forget()
    btn_с.configure(command=shelf, text='Вернуться')
    btn_r.place_forget()

def d_w23():
    label.configure(text=d_w['t23'])
    btn_с.configure(command=d_w24, text='Отряхнуть')

def d_w24():
    label.configure(text=d_w['t24'])
    btn_с.configure(command=d_w25, text='Осмотреть')

def d_w25():
    label.configure(text=d_w['t25'])
    btn_с.configure(command=d_w26, text='Дальше')

def d_w26():
    label.configure(text=d_w['t26'])
    btn_с.configure(command=d_w27, text='Дальше')

def d_w27():
    label.configure(text=d_w['t27'])
    btn_с.configure(command=quit, text='Закрыть игру')




#Виджеты

label = Label(frame1,
              text=d_w['t0'],
              fg ='white',
              font=('Comic Sans MS', 17),
              bg = "black"
              )
label.place(anchor=CENTER, relx=0.5, rely=0.5)



btn1 = Button(frame_r,
            text='Осмотреть',
            font=('Comic Sans MS', 17), 
            bg = "white",
            command=d_w1
            )
btn1.place(anchor=CENTER, relx=0.5, rely=0.5)


btnrc = Button(frame_l,
            text='Красная карта',
            font=('Comic Sans MS', 17), 
            bg = "white",
            command=d_rc
            )

btngc = Button(frame_c,
            text='Зелёная карта',
            font=('Comic Sans MS', 17), 
            bg = "white",
            command=d_gc
            )

btnbc = Button(frame_r,
            text='Синяя карта ',
            font=('Comic Sans MS', 17), 
            bg = "white",
            command=d_bc
            )



btn_l = Button(frame_l,
            text='Осмотреть слева',
            font=('Comic Sans MS', 17), 
            bg = "white",
            command=d_w_l
            )

btn_r = Button(frame_r,
            text='Осмотреть справа',
            font=('Comic Sans MS', 17), 
            bg = "white",
            command=d_w_r
            )

btn_с = Button(frame_c,
            text='Вернуться',
            font=('Comic Sans MS', 17), 
            bg = "white",
            command=d_w18
            )














#конец прорграммы (запуск)
root.mainloop()