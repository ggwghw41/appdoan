
import typing
from PyQt6 import QtCore,QtGui,QtWidgets,uic
from PyQt6.QtWidgets import*
from PyQt6.uic import loadUi
import sys
import MySQLdb as sql
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6 import QtCore, QtGui, QtWidgets
class Food_from(QMainWindow):
    def __init__(self) :
        super(Food_from,self).__init__()
        uic.loadUi('do_an_nhanh.ui',self)
        self.tra.clicked.connect(self.tinh_tien)
    def tinh_tien(self):
        menu = {
            "ga_ran":40000,
            "tra_sua":30000,
            "banh_my":20000,
            "hamberger":25000,
            "cafe":20000,
            "com_ga":50000
             }
        garan=int(self.ga_ran.text())*menu["ga_ran"]   
        trasua=int(self.tra_sua.text())*menu["tra_sua"]  
        banhmy=int(self.banh_my.text())*menu["banh_my"] 
        hamberge=int(self.hamberger.text())*menu["hamberger"] 
        ca_phe=int(self.cafe.text())*menu["cafe"] 
        comga=int(self.com_ga.text())*menu["com_ga"] 
        sum=garan+trasua+banhmy+hamberge+ca_phe+comga

        self.thanh_tien.setText(str(sum))
        hoa_hon=QtWidgets.QMessageBox()
        hoa_hon.setInformativeText(f'Tiền Phải Trả là: {sum}')
        hoa_hon.exec()
