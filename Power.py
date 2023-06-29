from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import os


class MyUI(QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi("Power.ui", self)
		self.show()
#self.OK_Button.clicked.connect(self.getfiles)
		self.Shut_Down_Button.clicked.connect(self.Shut_Down)
		self.Restart_Button.clicked.connect(self.Restart)
	def Shut_Down(self):
		print('Shut down')
		os.system('shutdown -s 3')

	def Restart(self):
		print('Restart')
if __name__ == "__main__":
	app = QApplication([])
	UI = MyUI()
	app.exec()