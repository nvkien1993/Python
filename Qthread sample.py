from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from PyQt5.QtCore import QThread, QObject, pyqtSignal as Signal, pyqtSlot as Slot
import time





class Worker(QObject):
	progress = Signal(int)
	completed = Signal(int)

	@Slot(int)
	def do_work(self, n):
		for i in range(1, n+1):
			time.sleep(1)
			print(n)
			self.progress.emit(i)

		self.completed.emit(i)

class MyUI(QMainWindow):
	work_requested = Signal(int)
	def __init__(self):
		super().__init__()
		uic.loadUi("Sample.ui", self)
		self.show()

		self.worker = Worker()
		self.worker_thread = QThread()

		self.pushButton_1.clicked.connect(self.start)

		self.worker.progress.connect(self.update_progress)
		self.worker.completed.connect(self.complete)

		self.work_requested.connect(self.worker.do_work)

		# move worker to the worker thread
		self.worker.moveToThread(self.worker_thread)

		# start the thread
		self.worker_thread.start()

	def start(self):
		n = 5
		self.progressBar_1.setMaximum(n)
		self.work_requested.emit(n)

	def update_progress(self, v):
		self.progressBar_1.setValue(v)

	def complete(self, v):
		self.progressBar_1.setValue(v)

if __name__ == "__main__":
	app = QApplication([])
	UI = MyUI()
	app.exec()