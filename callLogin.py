import sys
from PyQt5.QtWidgets import QApplication, QDialog
from demoLogin import *
from network import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.setStatusText)
        self.show()

    def sendInfo(self):
        login = self.ui.lineEditLogin.text()
        password = self.ui.lineEditPassword.text()
        list = [login, password]
        n = Network()
        reply = n.send(list)
        return reply

    def setStatusText(self):
        reply = MyForm.sendInfo(self)
        if reply == "True":
            self.ui.label.setText("<font color='green'>Successful</font>")
            print("Successful")
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