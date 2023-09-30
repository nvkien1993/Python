from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

class MyUI(QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi("Sample.ui", self)
		self.show()

if __name__ == "__main__":
	app = QApplication([])
	UI = MyUI()
	app.exec()