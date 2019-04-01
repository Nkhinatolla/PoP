import cmd_1  # Модуль где находятся все наши функции (Советую с начало ознакомиться с этим кодом и потом перейти на cmd)
file = open("input.txt", "r") # Пример берем из файла input.txt
text = file.read()[:-1] # text - одна строка без символа \n
file.close()
cursor = 30
cmd_1.printing(text, cursor) # написал специальную фунцию для того, чтобы поменять цвет курсора и вывести весь текст 

cursor = cmd_1.cmd_r(text, cursor, "han") 
cmd_1.printing(text, cursor)

text = cmd_1.cmd_t(text, cursor) 
cmd_1.printing(text, cursor)

text = cmd_1.cmd_insert(text, cursor, "Word")
cmd_1.printing(text, cursor)

