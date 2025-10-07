def m_3(z):
    a = bool(input("Введите первое значение: "))
    if z =="1":
                b = bool(input("Введите второе значение: "))
                c = a and b
    elif z =="2":
                b = bool(input("Введите второе значение: "))
                c = a or b
    elif z =="3":
                c = not a
    return c