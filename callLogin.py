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
        self.ai.pushButtonSend.clicked.connect(self.reply)
        self.ai.pushButtonRefresh.clicked.connect(self.refresh_reply)
        w.hide()
        self.window.show()

    def send_info(self, operation):
        login = self.ui.lineEditLogin.text()
        password = self.ui.lineEditPassword.text()
        list = [operation, login, password]
        n = Network()
        reply = n.send(list)
        return reply

    def set_status_text(self):
        reply = MyForm.send_info(self, "login")
        if reply == "True":
            self.ui.label.setText("<font color='green'>Successful</font>")
            print("Successful")
            MyForm.open_window(self)
            MyForm.set_user_information(self)
            return True
        else:
            self.ui.label.setText("<font color='red'>Wrong login or password</font>")
            print("Failed")
            return False

    def set_user_information(self):
        reply = MyForm.send_info(self, "account")
        self.ai.labelUserEditable.setText(reply[0])
        self.ai.lineEditAccountNumber.setText(str(reply[1]))
        self.ai.lineEditCurrentBalance.setText(str(reply[2]))

    def send_information_to_check(self):
        name = self.ai.labelUser.text()
        sender_number = self.ai.lineEditSenderNumber.text()
        receiver_number = self.ai.lineEditReceiverNumber.text()
        amount = self.ai.lineEditAmount.text()
        if name and sender_number and receiver_number and amount != "":
            list_of_information = ["transfer", name, sender_number, receiver_number, amount]
            n = Network()
            reply = n.send(list_of_information)
            return reply
        else:
            self.ai.label_2.setText("<font color='red'>Fill in all fields</font>")




    def reply(self):
        reply = MyForm.send_information_to_check(self)
        print(reply)
        if reply is False:
            self.ai.label_2.setText("<font color='red'>User doesn't exist</font>")

    def send_refresh(self):
        name = self.ai.labelUserEditable.text()
        n = Network()
        reply = n.send(["refresh", name])
        return reply

    def refresh_reply(self):
        reply1 = MyForm.send_refresh(self)
        self.ai.lineEditCurrentBalance.setText(reply1)



if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())