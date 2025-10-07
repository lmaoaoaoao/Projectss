def m_2 (z,a,b):
        if z =="1":
                c = a == b
        elif z =="2":
                c = a != b
        elif z =="3":
                c = a > b
        elif z =="4":
                c = a < b
        elif z =="5":
                c = a >= b
        elif z =="6":
                c = a <= b
        return c