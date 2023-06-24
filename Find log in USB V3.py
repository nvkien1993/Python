import os
import time
from datetime import datetime
import math
import json

current_time = datetime.now().strftime("%H_%M_%S")

try:
	#----------------Config File----------------#
	config = open('FSN_config.ini', mode = 'r').read()
	#1. Config model name
	Model_Name_Start = config.find('Model=',0)
	Model_Name_End = config.find('\n',Model_Name_Start+6)
	Model_Name = config[Model_Name_Start+6:Model_Name_End]
	#2. Config path of log
	PATH_LOG_Start = config.find('PathLog=',0)
	PATH_LOG_End = config.find('\n',PATH_LOG_Start+8)
	PathLog = config[PATH_LOG_Start+8:PATH_LOG_End]
	#3. Setup path of series number
	PATH_SN_Start = config.find('PathSN=',0)
	PATH_SN_End = config.find('\n',PATH_SN_Start+7)
	PathSNFolder = config[PATH_SN_Start+7:PATH_SN_End]
	PathSN = PathSNFolder+r'\SN.txt'


	Result_Folder = r'%s_Result_%s'%(Model_Name, current_time)
	Detail_log = Result_Folder + r"\Detail Log"

	#----------------Load data from script file----------------#
	with open("Script.json", "r") as script:
		s_file = json.load(script)
		s_key = s_file[Model_Name]["Key"]
		s_length_key = s_file[Model_Name]["Length_Key"]
		s_length_SN = s_file[Model_Name]["Length_SN"]
	
	#----------------Find log in USB and separate to detail----------------#
	def project():
		location_SN = ReadFile.find(ListSN[j])
		qty_KEY = ReadFile.count(s_key,location_SN)
		location_start = location_SN - s_length_SN
		location_end = ReadFile.find(s_key,location_SN) - s_length_key

		if qty_KEY == 0: #case1: 1 USB has 1 log at the end
			USB_Name = str(ListName[i]).replace(".txt", "")
			Detail_Result = open(Detail_log+'\\%s [USB_%s].txt'%(ListSN[j],USB_Name), 'w')
			Detail_Result.write(ReadFile[location_start:])
			Detail_Result.close
			
		elif QtyKeyWord == 1: #case2: 1 USB has 1 log not at the end
			USB_Name = str(ListName[i]).replace(".txt", "")
			Detail_Result = open(Detail_log+'\\%s [USB_%s].txt'%(ListSN[j],USB_Name), 'w')
			Detail_Result.write(ReadFile[location_start:location_end])
			Detail_Result.close
			
		else: #case3: 1 USB have more than 1 log
			USB_Name = str(ListName[i]).replace(".txt", "")
			location_case3_start = location_start
			location_case3_end = location_end
			for cout_case3 in range(1,QtyKeyWord+1):
				if cout_case3 < QtyKeyWord: #1st log
					Detail_Result = open(Detail_log+'\\%s [USB_%s] (%s).txt'%(ListSN[j],USB_Name,cout_case3), 'w')
					Detail_Result.write(ReadFile[location_case3_start:location_case3_end])
					location_case3 = ReadFile.find(ListSN[j], location_case3_end)
					Detail_Result.close()
					location_case3_start = location_case3 - s_length_SN
					location_case3_end = ReadFile.find(s_key,location_case3) - s_length_key
					
				elif cout_case3 == QtyKeyWord: #2nd 3rd 4th ... log
					if location_case3_end < 0:
						Detail_Result = open(Detail_log+'\\%s [USB_%s] (%s).txt'%(ListSN[j],USB_Name,cout_case3), 'w')
						Detail_Result.write(ReadFile[location_case3_start:])
						Detail_Result.close()
						

					elif location_case3_end > 0:
						Detail_Result = open(Detail_log+'\\%s [USB_%s] (%s).txt'%(ListSN[j],USB_Name,cout_case3), 'w')
						Detail_Result.write(ReadFile[location_case3_start:location_case3_end])
						Detail_Result.close()
	
	#----------------Read qty USB, SN & Name of USB----------------#
	ListSN = open(PathSN).read().split('\n') #Read each SN from SN.txt
	SNQty = len(ListSN) #Read qty of SN
	ListName = os.listdir(PathLog) # Read name USB
	FileQty = len(ListName) #Read qty of USB
	print(Model_Name+'\n')
	print('Total %s SN Need Find The Log In %s USB!'%(len(ListSN),FileQty)+'\n')

	#----------------Creat Result & detail folder----------------#
	os.mkdir(Result_Folder)
	os.mkdir(Detail_log)
	USBArray = []
	
	for C_Array in range(0,len(ListSN)):
		USBArray.append([])
	for i in range(0,FileQty):
	
		#----------------Show percent completed----------------#
		percent = math.ceil((i +1)/(FileQty)*100)
		print('Completed '+str(percent)+r'%')

		#----------------Show percent completed----------------#
		File = open(PathLog+'\\%s'%(ListName[i]), mode = 'r+', encoding ='utf-8', errors = 'replace')
		ReadFile = File.read()
		for j in range(0,len(ListSN)):
			QtyKeyWord = ReadFile.count(ListSN[j])
			if QtyKeyWord != 0:
				USBArray[j].append(ListName[i])
				project()
		File.close()

		os.system('cls')
		print(Model_Name+'\n')
		print('Total %s SN Need Find The Log In %s USB!'%(len(ListSN),FileQty)+'\n')
		
	#----------------summary SN & USB to Summary.csv file----------------#
	Result_summary = open(Result_Folder +r'\%s_Summary_%s.csv'%(Model_Name, current_time), 'w')
	Result_summary.write("SN,USB\n")
	for b in range(0,len(ListSN)):
		String ='*%s, %s'%(str(ListSN[b]), USBArray[b])
		String1 = String.replace(".txt'", "").replace("[","").replace("]", "").replace("'", "USB_")
		Result_summary.write(String1+'\n')
		print(String1)
	Result_summary.close()

	#----------------summary SN, USB & last step to Detail.csv file----------------#
	ListNameDetail = os.listdir(Detail_log)
	ListNameDetail_len = len(ListNameDetail)
	Result_detail = open(Result_Folder +r'\%s_Detail_%s.csv'%(Model_Name, current_time), 'w')
	Result_detail.write("SN,USB,Description Last Step\n")

	for C_Detail in range(0,ListNameDetail_len):
		File_detail = open(Detail_log+'\\%s'%(ListNameDetail[C_Detail]), mode = 'r+', encoding ='utf-8', errors = 'replace')
		File_detail_read = File_detail.read()
		File_detail.seek(0)
		count_enter = File_detail_read.count("\n")
		for C_Readline in range(0,count_enter-1):
			File_detail.readline()
		end_line = File_detail.readline().replace(",",";")
		end_line_string = ('*%s,%s'%(ListNameDetail[C_Detail],end_line)).replace(".txt","").replace("[USB",",USB").replace("]","")
		Result_detail.write(end_line_string)
	Result_detail.close()

except:
	try:
		config = open('FSN_config.ini','x+')
		config.write('[FSN_config]\nModel=\nPathLog=\nPathSN=\n\nNote:\n- Model need select UIW4020PXM or DSI724BIS.\n- PathLog: Path of folder contain log file.\n- PathSN: Path of folder contain list SN (Name of list SN must be SN.txt).')
		config.close()
		print('FSN_config file has been created!\n')
	except:
		print('Please check information in FSN_config file!')

	try:
		config = open('Script.json','x+')
		config.write('{\n	"UIW4020PXM":{"Key":"INFO>> USB Mount path:", "Length_Key":16, "Length_SN":569},\n	"DSI724BIS":{"Key":"START SW upgrade script v0109", "Length_Key":93, "Length_SN":338}\n}')
		config.close()
		print('Script.json file has been created!\n')
	except:
		print()

print("\n@Harry")
time.sleep(1)