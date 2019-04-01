import cmd_2  # Модуль где находятся все наши функции (Советую с начало ознакомиться с этим кодом и потом перейти на cmd)
file = open("input.txt", "r") # Пример берем из файла input.txt
text = file.read().split('\n') # text - list из сточек, допустим text[1] вернет нам 2 строку из примера
file.close()
cursor = (2, 30)
cursor = cmd_2.cmd_r(text, cursor, "han")
cmd_2.printing(text, cursor)

cursor = cmd_2.cmd_t(text, cursor)
cmd_2.printing(text, cursor)

cursor = cmd_2.cmd_plus(text, cursor)
cmd_2.printing(text, cursor)

cursor = cmd_2.cmd_insert(text, cursor, "Word")
cmd_2.printing(text, cursor)