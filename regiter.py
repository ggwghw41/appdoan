
from PyQt6 import QtCore,QtGui,QtWidgets,uic
from PyQt6.QtWidgets import*
from PyQt6.uic import loadUi
import sys
import MySQLdb as sql
from PyQt6.QtWidgets import QApplication
#gọi cửa sổ tạo tài khoản ra
class RegisterForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.is_closed = False
        uic.loadUi('regiter.ui',self)
        self.click_tk.clicked.connect(self.tao)
    #nhập user và pass để tạo tài khoản và trả dữ liệu vè PHP Admin    
    def tao(self):
        user_dn=self.username_tk.text()
        password_dn=self.pass_tk.text()
        comfimpas=self.comfimpass.text()
        db=sql.connect('localhost','root','','user')

        query=db.cursor()
        query.execute("select * from user where  user='"+user_dn+"' and pass='"+password_dn+"'")

        kt=query.fetchone()
        #xét điều kiện tạo tài khoản
        if kt:
            QMessageBox.information(self,"TẠO TÀI KHOẢN","Nhập lại đêii cha nội,tài khoản này có đăng kí rồi -_-")
        elif self.pass_tk.text() != self.comfimpass.text():
            QMessageBox.information(self,"TẠO TÀI KHOẢN","Nhập lại đêii cha nội,")
        else:
            query.execute("insert into user value('"+user_dn+"','"+password_dn+"')")
            db.commit()
            QMessageBox.information(self,"TẠO TÀI KHOẢN","TẠO TÀI KHOẢN")
            self.close()
       