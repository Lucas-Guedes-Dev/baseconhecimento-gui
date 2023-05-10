import sys
import typing

from PyQt5 import QtCore
from telas.login import Ui_tela_login as login
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget 

class ManipulaLogin(QMainWindow, login):
    def __init__(self, *args, obj=None, **kwargs):
        super(ManipulaLogin, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.bt_login.clicked.connect(self.on_bt_login_clicked)

        self.username_teste = 'lucas'
        self.senha_teste = '1234'

    def on_bt_login_clicked(self):
        self.bt_login.clicked.disconnect()
        self.bt_login.clicked.connect(self.on_bt_login_clicked)

        username = self.inp_username.text()
        senha = self.inp_senha.text()
        # print(username, senha)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    ui = ManipulaLogin()
    ui.show()
    sys.exit(app.exec_())