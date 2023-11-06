from PyQt6.QtWidgets import QApplication
from login import login_from
#goi cửa sổ đăng nhập ra
if __name__=="__main__":
    app =QApplication([])
    login_from=login_from()
    login_from.show()
    app.exec()    