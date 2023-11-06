from PyQt6.QtWidgets import*
from PyQt6 import QtCore, uic
from PyQt6.QtWidgets import QMainWindow, QWidget
from PyQt6.QtSql import QSqlQuery
import MySQLdb as sql
from regiter import RegisterForm
from PyQt6.uic import loadUi
from PyQt6 import   QtWidgets,QtGui
from do_an import Food_from
#thiết lập nút đăng nhập và nhập user và pass
class login_from(QMainWindow):
    def __init__(self):
        super(login_from,self).__init__()
        uic.loadUi('login.ui',self)
        self.pushButton.clicked.connect(self.login_Main)
        self.tao_tk.clicked.connect(self.Regiter)
        self.registerForm = None
    def login_Main(self):
        user_dn=self.ten.text()
        pass_dn =self.mat_khau.text()
#liên kết sql phpAdmin
        db= sql.connect('localhost','root','','user')
        query=db.cursor()
        query.execute("select * from user where  user='"+user_dn+"' and pass='"+pass_dn+"'")
        kt = query.fetchone()
        if kt:
            QMessageBox.information(self,"Đăng nhập","Đăng nhập thành công")
            Food_fro= Food_from()
            self.Food_fro = Food_fro
            Food_fro.show()

        else:
            QMessageBox.information(self,"Đăng nhập","Sai rồi bạn êi -_-")
#lien ket với tạo tài khoản
    def Regiter(self):
        RegisterFor = RegisterForm()
        self.RegisterFor = RegisterFor
        RegisterFor.show()
        if RegisterFor.is_closed:
            self.show()
