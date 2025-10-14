def m_3(z):

    if z =="1":
                a = bool(input("Введите первое значение: "))
                b = bool(input("Введите второе значение: "))
                c = a and b
    elif z =="2":
                a = bool(input("Введите первое значение: "))
                b = bool(input("Введите второе значение: "))
                c = a or b
    elif z =="3":
                a = bool(input("Введите значение: "))
                c = not a
    else:
                print ('Ошибка! Неверно выбран номер типа опертатора!')
    return c