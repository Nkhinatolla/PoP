import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from PyQt5 import QtGui, QtCore
import design, firstwindow, statistics  # Это наш конвертированный файл дизайна
import os, random
class FirstWindow(QtWidgets.QMainWindow, firstwindow.Ui_FirstWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.mousePressEvent = self.Signx
        self.label_2.mousePressEvent = self.Signo

    def Signo(self, event):
        global username
        username = self.lineEdit.text()
        if (username == ''):
            username = 'Guest'
        window2.sign = 'o'
        window2.sign_c = 'x'
        window2.show()
        window2.computer()
        self.close()
    def Signx(self, event):
        global username
        username = self.lineEdit.text()
        if (username == ''):
            username = 'Guest'
        window2.sign = 'x'
        window2.sign_c = 'o'
        window2.show()
        self.close()

class SecondWindow(QtWidgets.QMainWindow, design.Ui_MainWindow):
    Free_Labels = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    Player_Labels = []
    Comp_Labels = []
    sign = 'x'
    sign_c = 'o'
    State = 0
    _translate = QtCore.QCoreApplication.translate
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        for i in range(1,10):
            label = self.findChild(QtWidgets.QLabel, "label_" + str(i))
            label.mousePressEvent = self.clicked_label

    def clicked_label(self, event):
        if (self.State != 0):
            return
        x = event.globalX() - self.x() - 13
        y = event.globalY() - self.y() - 49
        number = (x // 150 + 1) + (y // 150) * 3
        if (number not in self.Free_Labels):
            return
        self.Free_Labels.remove(number)
        self.Player_Labels.append(number)
        label = self.findChild(QtWidgets.QLabel, "label_" + str(number))
        label.setText(self._translate("MainWindow", '<html><head/><body><p><img src=":/' + self.sign + '/' + self.sign + '_img.png"/></p></body></html>'))
        self.status()
        self.computer()
        self.status()
        if (self.State):
            file = open("standings", "w")
            ListOfUsers = []
            if username in users:
                users[username] = users[username] + self.point
            else:
                users[username] = self.point
            for key in users:
                ListOfUsers.append((key, users[key]))
                file.write(key + " " + str(users[key]) + '\n')
            ListOfUsers =  sorted(ListOfUsers,key=lambda x:(-x[1],x[0]))
            for i in ListOfUsers:
                window3.listWidget.addItem(i[0] + " " + str(i[1]))
            window3.show()

    def computer(self):
        if (self.State != 0):
            return
        number = random.choice(self.Free_Labels)
        self.Free_Labels.remove(number)
        self.Comp_Labels.append(number)
        label = self.findChild(QtWidgets.QLabel, "label_" + str(number))
        label.setText(self._translate("MainWindow", '<html><head/><body><p><img src=":/' + self.sign_c + '/' + self.sign_c + '_img.png"/></p></body></html>'))
    def status(self):
        if (self.check(self.Player_Labels) == True):
            self.State = 1
            self.point = 2
            self.setWindowTitle(self._translate("Player Win", "Player Win"))
        elif (self.check(self.Comp_Labels) == True):
            self.State = 2
            self.point = -1
            self.setWindowTitle(self._translate("Computer Win", "Computer Win"))
        elif (len(self.Free_Labels) == 0):
            self.State = 3
            self.point = 1
            self.setWindowTitle(self._translate("Draw", "Draw"))
    def check(self, l):
        if (1 in l and 2 in l and 3 in l):
            return True
        if (4 in l and 5 in l and 6 in l):
            return True
        if (7 in l and 8 in l and 9 in l):
            return True
        if (1 in l and 4 in l and 7 in l):
            return True
        if (2 in l and 5 in l and 8 in l):
            return True
        if (3 in l and 6 in l and 9 in l):
            return True
        if (1 in l and 5 in l and 9 in l):
            return True
        if (3 in l and 5 in l and 7 in l):
            return True
        return False

class ThirdWindow(QtWidgets.QMainWindow, statistics.Ui_TableList):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ResetButton.clicked.connect(self.ResetFunc)
    def ResetFunc(self):
        window2.close()
        self.close()
        os.system("python main.py")
        app.exit()

users = {}
username = ''
file = open('standings', 'r')
for line in file:
    line = line.split()
    users[line[0]] = int(line[1])
file.close()
app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
window1 = FirstWindow()  # Создаём объект класса FirstWindow()
window2 = SecondWindow()  # Создаём объект класса SecondWindow()
window3 = ThirdWindow() # Создаём объект класса ThirdWindow()
window1.show() 
app.exec_()  # и запускаем приложение

