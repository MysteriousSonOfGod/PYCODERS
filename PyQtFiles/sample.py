import sys
from PyQt5.QtWidgets import QApplication,QWidget

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title="Kalyani Ravi"
        self.left=10
        self.top=10
        self.width=640
        self.height=480
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
#
if __name__=="__main__":
    app=QApplication(sys.argv)
    ex=App()
    sys.exit(app.exec())
#
# # if __name__=="__main__":
# #     app=QApplication(sys.argv)
# #     w=QWidget()
# #     w.resize(1000,300)
# #     w.move(300, 300)
# #     w.setWindowTitle("Ravi Prasad Kalyani")
# #     w.show()
# #
# #     sys.exit(app.exec())
# import sys
# print("Hello {}. Welcome to {} tutorial".format(sys.argv[1], sys.argv[2]))