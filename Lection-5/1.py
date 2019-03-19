import cmd  # Модуль где находятся все наши функции (Советую с начало ознакомиться с этим кодом и потом перейти на cmd)
file = open("input.txt", "r") # Пример берем из файла input.txt
text = file.read().split('\n') # text - list из сточек, допустим text[1] вернет нам 2 строку из примера
file.close()
cursor = (1, 5) # это координаты курсора, (2, 5) - третья строка, 5 символ
cmd.printing(text, cursor) # написал специальную фунцию для того, чтобы поменять цвет курсора и вывести весь текст 

cursor = cmd.cmd_h(text, cursor) # cmd_h - Функция из модули cmd, меняет курсор на лево
cmd.printing(text, cursor)

cursor = cmd.cmd_i(text, cursor) # cmd_i - меняет курсор на право
cmd.printing(text, cursor)

cursor = cmd.cmd_j(text, cursor) # сmd_j - вверх
cmd.printing(text, cursor)

cursor = cmd.cmd_k(text, cursor) # cmd_k - вниз
cmd.printing(text, cursor)

cursor = cmd.cmd_x(text, cursor) # cmd_x - удаляем элемент слево
cmd.printing(text, cursor)

cursor = cmd.cmd_d(text, cursor) # cmd_d - удаляем справо всю строку
cmd.printing(text, cursor)

cursor = cmd.cmd_dd(text, cursor) # cmd_dd - удаляем текущую строку
cmd.printing(text, cursor)

cursor = cmd.cmd_ddp(text, cursor) # cmd_ddp - меняем текущую строку со следующим
cmd.printing(text, cursor)
cursor = (0, 0)
cursor = cmd.cmd_n(text, cursor, "") # cmd_ddp - меняем текущую строку со следующим
cmd.printing(text, cursor)


