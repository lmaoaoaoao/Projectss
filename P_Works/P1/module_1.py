def m_1 (z,a,b):
        if z =="1":
                c = a + b
        elif z =="2":
                c = a - b
        elif z =="3":
                c = a * b
        elif z =="4":
                try:
                        c = a / b
                except ZeroDivisionError:
                        print ('Ошибка! Деление на 0!')
        elif z =="5":
                try:
                        c = a // b
                except ZeroDivisionError:
                        print ('Ошибка! Деление на 0!')
        elif z =="6":
                try:
                        c = a % b
                except ZeroDivisionError:
                        print ('Ошибка! Деление на 0!')
        elif z =="7":
                c = a ** b
        else:
                print ('Ошибка! Неверно выбран номер типа опертатора!')
        return c
