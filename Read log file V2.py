import os
from datetime import datetime
import time
current_time = datetime.now().strftime("%H_%M_%S")

try:
	#Config File:
	config = open('RLF_config.ini', mode = 'r').read()

	#1. Config path of stat file
	PATH_Start = config.find('PathFile=',0)
	PATH_End = config.find('\n',PATH_Start+9)
	PathFile = config[PATH_Start+9:PATH_End]
	#print(PathStatFile)

	#3. Setup key
	Key_Start = config.find('Key=',0)
	Key_End = config.find('\n',Key_Start+4)
	Key = config[Key_Start+4:Key_End]

	#3. Setup index
	Index_start = config.find('Index=',0)
	Index_End = config.find('\n',Index_start+6)
	Index = config[Index_start+6:Index_End]

	open('RLF_config.ini', mode = 'r').close()

	print('[READ LOG FILE]\n')

	def Index_All():
		for i in range(0, FileQty):
			lstString = (open(PathFile + r'\%s' %(ListName[i]), mode = 'r', encoding ='utf-8', errors = 'replace')).read().splitlines()
			flag = 1
			for j in range(0,len(lstString)):
				count_key = lstString[j].count(Key)
				if count_key != 0:
					if flag == 1:
						Result.write(ListName[i] + ',' + lstString[j].replace(',' , ';') + '\n')
						flag = 0
					else:
						Result.write(',' + lstString[j].replace(',' , ';') + '\n')
						print(lstString[j])

	def Index_First():
		for i in range(0, FileQty):
			lstString = (open(PathFile + r'\%s' %(ListName[i]), mode = 'r', encoding ='utf-8', errors = 'replace')).read().splitlines()
			flag = 1
			for j in range(0,len(lstString)):
				count_key = lstString[j].count(Key)
				if count_key != 0:
					if flag == 1:
						Result.write(ListName[i] + ',' + lstString[j].replace(',' , ';') + '\n')
						flag = 0
						print(lstString[j])

	def Index_Final():
		for i in range(0, FileQty):
			lstString = (open(PathFile + r'\%s' %(ListName[i]), mode = 'r', encoding ='utf-8', errors = 'replace')).read().splitlines()
			flag = -1
			for j in range(0,len(lstString)):
				count_key = lstString[j].count(Key)
				if count_key != 0:
					flag = j
			if flag != -1:
				Result.write(ListName[i] + ',' + lstString[flag].replace(',' , ';') + '\n')
				print(lstString[flag])


	Result = 'Result_%s_Index_%s' %(Index,current_time)
	Result = open(Result + '.csv', 'w')
	Result.write('Serial Number' + ',' + Key + '\n')
	ListName = os.listdir(PathFile)
	FileQty = len(ListName)


	if Index == 'All':
		Index_All()
	elif Index == 'First':
		Index_First()
	elif Index == 'Final':
		Index_Final()

except:
	try:
		config = open('RLF_config.ini','x+')
		config.write('[READ LOG FILE]\nPathFile=\nKey=\nIndex=All\n\nNote:\n- PathFile: Path of folder contain log file.\n- Key: Keyword need to search.\n- Index: Select one of (First, Final, All).\n\t+ First: Get value for first index.\n\t+ Final: Get value for final index.\n\t+ All: Get value for all index.\n')
		config.close()
		print('RLF_config file has been created!\n')
	except:
		print('Please check information in RLF_config file!')

print("\n@Harry")
time.sleep(1)