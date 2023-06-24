import os
from os import path
import shutil
from datetime import datetime
import glob

current_time = datetime.now().strftime("%H%M%S")
KEY = 'pearl:/ # echo -e "FLAG_1'
List_SN = r'C:\Users\V0936280\Desktop\SN.txt'
path_folder = r'C:\Users\V0936280\Desktop\ZBPW'
#Case1 = 'Name_File' #Name_File or Content
Case1 = 'Content' #Name_File or Content
#Case2 = 'KEY'
Case2 = 'ListSN'

def Case_KEY_Name_File():
	Result_Folder = r'SPR_%s'%(current_time)
	os.mkdir(Result_Folder)
	ListName = glob.glob(path_folder+'/**', recursive = True)
	FileQty = len(glob.glob(path_folder+'/**', recursive = True))
	for i in range(0,FileQty):
		#FileName = ListName[i]
		if str(path.isfile(ListName[i])) == 'True':
			Index = ListName[i].rfind('\\')
			Count_Key = ListName[i][Index:].find(KEY)
			if Count_Key != -1:
				print(ListName[i])
				shutil.copy2(ListName[i], Result_Folder)
def Case_KEY_Content():			
	Result_Folder = r'SPR_%s'%(current_time)
	os.mkdir(Result_Folder)
	ListName = glob.glob(path_folder+'/**', recursive = True)
	FileQty = len(glob.glob(path_folder+'/**', recursive = True))
	for i in range(0,FileQty):
		#FileName = ListName[i]
		if str(path.isfile(ListName[i])) == 'True':
			file_open = open(ListName[i],mode = 'r', encoding ='utf-8', errors = 'replace').read()
			Count_Key = file_open.find(KEY)
			if Count_Key != -1:
				print(ListName[i])
				shutil.copy2(ListName[i], Result_Folder)
def Case_ListSN_Name_File():
	Result_Folder = r'SPR_%s'%(current_time)
	os.mkdir(Result_Folder)
	ListName = glob.glob(path_folder+'/**', recursive = True)
	FileQty = len(glob.glob(path_folder+'/**', recursive = True))
	F_SN = open(List_SN).readlines()
	SN_Qty = len(F_SN)
	for i in range(0,FileQty):
		if str(path.isfile(ListName[i])) == 'True':
			for j in range(0,SN_Qty):
				SN = F_SN[j].replace('\n','')
				Index = ListName[i].rfind('\\')
				Count_Key = ListName[i][Index:].find(SN)
				if Count_Key != -1:
					print(ListName[i])
					shutil.copy2(ListName[i], Result_Folder)
def Case_ListSN_Content():
	Result_Folder = r'SPR_%s'%(current_time)
	os.mkdir(Result_Folder)
	ListName = glob.glob(path_folder+'/**', recursive = True)
	FileQty = len(glob.glob(path_folder+'/**', recursive = True))
	F_SN = open(List_SN).readlines()
	SN_Qty = len(F_SN)
	for i in range(0,FileQty):
		if str(path.isfile(ListName[i])) == 'True':
			file_open = open(ListName[i],mode = 'r', encoding ='utf-8', errors = 'replace').read()
			for j in range(0,SN_Qty):
				SN = F_SN[j].replace('\n','')
				Count_Key = file_open.find(SN)
				#Index = ListName[i].rfind('\\')
				#Count_Key = ListName[i][Index:].find(b)
				if Count_Key != -1:
					print(ListName[i])
					shutil.copy2(ListName[i], Result_Folder)

if Case1 == 'Name_File' and Case2 == 'KEY':
	print("=====================================================\n=========== Separate by Key & Name of Log File ============\n=====================================================\n")
	Case_KEY_Name_File()
elif Case1 == 'Content'and Case2 == 'KEY':
	print("=====================================================\n========== Separate by Key & Content of Log File ==========\n=====================================================\n")
	Case_KEY_Content()
elif Case1 == 'Name_File'and Case2 == 'ListSN':
	print("=====================================================\n====== Separate by List SN & Name of Log File =======\n=====================================================\n")
	Case_ListSN_Name_File()
elif Case1 == 'Content'and Case2 == 'ListSN':
	print("=====================================================\n===== Separate by List SN & Content of Log File =====\n=====================================================\n")
	Case_ListSN_Content()