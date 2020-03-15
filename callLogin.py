import sys
from PyQt5.QtWidgets import QApplication, QDialog
from demoLogin import *
from network import *
from demoUserWindow import *


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.set_status_text)
        self.show()

    def open_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ai = Ui_UserWindow()
        self.ai.setupUi(self.window)
        w.hide()
        self.window.show()

    def send_info(self):
        login = self.ui.lineEditLogin.text()
        password = self.ui.lineEditPassword.text()
        list = [login, password]
        n = Network()
        reply = n.send(list)
        return reply

    def set_status_text(self):
        reply = MyForm.send_info(self)
        if reply == "True":
            self.ui.label.setText("<font color='green'>Successful</font>")
            print("Successful")
            MyForm.open_window(self)
            return True
        else:
            self.ui.label.setText("<font color='red'>Wrong login or password</font>")
            print("Failed")
            return False


if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())