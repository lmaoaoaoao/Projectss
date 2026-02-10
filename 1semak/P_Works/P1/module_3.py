def m_3(z):

    if z =="1":
                try:
                    a = bool(input("Введите первое значение: "))
                except TypeError:
                    print ('Ошибка! непрвальный тип введённой переменных!')
    
                try:
                    b = bool(input("Введите второе значение: "))
                except TypeError:
                    print ('Ошибка! непрвальный тип введённой переменных!')
                               
                c = a and b
    elif z =="2":
                try:
                    a = bool(input("Введите первое значение: "))
                except TypeError:
                    print ('Ошибка! непрвальный тип введённой переменных!')
    
                try:
                    b = bool(input("Введите второе значение: "))
                except TypeError:
                    print ('Ошибка! непрвальный тип введённой переменных!')
                c = a or b
    elif z =="3":
                try:
                    a = bool(input("Введите первое значение: "))
                except TypeError:
                    print ('Ошибка! непрвальный тип введённой переменных!')
                c = not a
    else:
                print ('Ошибка! Неверно выбран номер типа опертатора!')
    return c