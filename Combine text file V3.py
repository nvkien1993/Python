# Project: COMBINE TEXT FILE
# Version:1
# Author: Harry


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import os
from datetime import datetime
import time

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(413, 305)
        Form.setMinimumSize(QtCore.QSize(413, 305))
        Form.setMaximumSize(QtCore.QSize(413, 305))
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 391, 111))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.LE_Path = QtWidgets.QLineEdit(self.groupBox)
        self.LE_Path.setGeometry(QtCore.QRect(130, 20, 201, 21))
        self.LE_Path.setObjectName("LE_Path")
        self.SB_Line_header = QtWidgets.QSpinBox(self.groupBox)
        self.SB_Line_header.setGeometry(QtCore.QRect(130, 70, 42, 22))
        self.SB_Line_header.setObjectName("SB_Line_header")
        self.LB2_Lineheader = QtWidgets.QLabel(self.groupBox)
        self.LB2_Lineheader.setGeometry(QtCore.QRect(10, 70, 111, 16))
        self.LB2_Lineheader.setObjectName("LB2_Lineheader")
        self.LB_Path_of_folder = QtWidgets.QLabel(self.groupBox)
        self.LB_Path_of_folder.setGeometry(QtCore.QRect(10, 20, 111, 16))
        self.LB_Path_of_folder.setObjectName("LB_Path_of_folder")
        self.PB_Open = QtWidgets.QPushButton(self.groupBox)
        self.PB_Open.setGeometry(QtCore.QRect(340, 20, 41, 21))
        self.PB_Open.setObjectName("PB_Open")
        self.PB_Start = QtWidgets.QPushButton(self.groupBox)
        self.PB_Start.setGeometry(QtCore.QRect(210, 60, 171, 41))
        self.PB_Start.setObjectName("PB_Start")
        self.TB_Result = QtWidgets.QTextBrowser(Form)
        self.TB_Result.setGeometry(QtCore.QRect(10, 130, 391, 161))
        self.TB_Result.setObjectName("TB_Result")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        #########################################################
        self.PB_Open.clicked.connect(self.getfiles)
        self.PB_Start.clicked.connect(self.ComBineTextFile)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Combine Text File"))
        self.LB2_Lineheader.setText(_translate("Form", "Head line number"))
        self.LB_Path_of_folder.setText(_translate("Form", "Path of folder"))
        self.PB_Open.setText(_translate("Form", "Open"))
        self.PB_Start.setText(_translate("Form", "START"))
    def getfiles(self, s):
        Folder_Path = str(QFileDialog.getExistingDirectory(None, "Select Directory"))
        if Folder_Path !="":
            self.LE_Path.setText(Folder_Path)
    def ComBineTextFile(self):
        try:
            current_time = datetime.now().strftime("%H_%M_%S")
            PathStatFile = self.LE_Path.text()
            Headline_Number = self.SB_Line_header.value()
            Result_Folder = r'Combine_Result_%s'%(current_time)
            os.makedirs(Result_Folder,exist_ok=True)
            ListName = os.listdir(PathStatFile)
            FileQty = (len(os.listdir(PathStatFile)))
            Result = Result_Folder + "\\" + Result_Folder
            Data = open(Result+'.txt', 'w',encoding ='utf-8', errors = 'replace')
            print('=============== Combine Text File ================\n')
            self.TB_Result.clear()
            self.TB_Result.append('================= Combine Text File =================\n')

            for i in range(0,FileQty):
                print(ListName[i])
                self.TB_Result.append(ListName[i])
                File = open(PathStatFile +'\\%s'%(ListName[i]), 'r+',encoding ='utf-8', errors = 'replace')
                ReadFile = File.read()
                File.seek(0)
                LineNum = ReadFile.count('\n')
                
                if i == 0:
                    for x in range(0,LineNum):
                        ReadFiles = File.readline()
                        Data.write(ReadFiles)
                else:
                    for x in range(0,LineNum):
                        if x < Headline_Number:
                            ReadFiles = File.readline()
                        else:
                            ReadFiles = File.readline()
                            Data.write(ReadFiles)
            Data.close()
            #convert to csv file
            csvFileResult = open(Result+'.csv', 'w',encoding ='utf-8', errors = 'replace')
            csvRead = open(Result+'.txt', 'r',encoding ='utf-8', errors = 'replace').read()
            csvFileResult.write(csvRead.replace('	',','))
            csvFileResult.close()
            #self.PB_Start.setText("DONE")
            #time.sleep(1)
            
            print('\n============ %s Files Combined Successfully! ============='%(FileQty))
            self.TB_Result.append('\n============ %s Files Combined Successfully! ============='%(FileQty))
        #time.sleep(1)
        except:
           # print("ERROR!")
           self.TB_Result.clear()
           self.TB_Result.append('================ ERROR! TRY AGAIN! =================')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
    time.sleep(1)