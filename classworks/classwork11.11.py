add = lambda x,y:x+y
print (add(3, 5))

emploees=[
    {"name": 'abubakr', "otdel": 'prodaji', "zp": 70000}, 
    {"name": 'manul', "otdel": 'admin', "zp": 50000}, 
    {"name": 'zahar', "otdel": 'IT-bezopasnost', "zp": 120000}, 
    {"name": 'ismail', "otdel": 'ohrana', "zp": 45000}, 
    {"name": 'teodor', "otdel": 'prodaji', "zp": 75000}, 
    {"name": 'maga', "otdel": 'ohrana', "zp": 55000}, 
    {"name": 'katya', "otdel": 'admin', "zp": 50000}
    ]



sort1 = list(sorted(emploees, key=lambda emploees:emploees["zp"]))
# sort2 = sorted(sort1, key=lambda emploees:emploees["name"], reverse=1)
# sort3 = sorted(sort2, key=lambda emploees: (emploees["otdel"], emploees["zp"]))

for i in sort1:
    print (sort1[i], end='\n')





# # file = open('example.py', 'w')
# # file.write('print("mda-ms")')
# # file.close()

# # with open('file.py', 'w', encoding='utf-8') as file:
# #     file.write ('print("that\'s file.py")\n')
# #     a = ['print("misha")\n', 'print("nastya")\n', 'print("lena")\n']
# #     file.writelines(a)


# with open('file.py', 'r', encoding='utf-8') as file:
#     a = file.readlines()
#     print(a)
    