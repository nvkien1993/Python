import shutil
import os
import time
from datetime import datetime


current_time = datetime.now().strftime("%H_%M_%S")

try:
	print('---------Copy DLD Log---------')
	config = open('Copy_Log_Config.txt', mode = 'r').read()

	DLD_File_Type_Start = config.find('DLD_File_Type(File or Folder):',0)
	DLD_File_Type_Stop = config.find('\n',DLD_File_Type_Start+31)
	DLD_File_Type = config[DLD_File_Type_Start+31:DLD_File_Type_Stop]
	#print(DLD_File_Type)

	PATH_DLD_LOG_Start = config.find('PATH_DLD_LOG:',0)
	PATH_DLD_LOG_End = config.find('\n',PATH_DLD_LOG_Start+14)
	PATH_DLD_LOG = config[PATH_DLD_LOG_Start+14:PATH_DLD_LOG_End]
	#print(PATH_DLD_LOG)

	Result_Folder = 'DLD_LOG_%s'%(current_time)
	os.mkdir(Result_Folder)

	while True:
		USBname = input ("\nUSB NAME = ")
		if DLD_File_Type == 'File':
			try:
				shutil.copy2(PATH_DLD_LOG, Result_Folder + r'\%s.txt'%(USBname))
				print ("---------Copy USB %s Completed---------"%(USBname))
			except IOError:
				print ("\nCopy FAIL. Try again!\n")
		elif DLD_File_Type == 'Folder':
			try:
				destination = Result_Folder+'\\'+USBname
				#print(destination)
				os.mkdir(destination)
				for ListName in os.listdir(PATH_DLD_LOG):
					source = PATH_DLD_LOG +'\\'+ ListName
					shutil.copy2(source,destination)
					print(ListName)
				print ("---------Copy USB %s Completed---------"%(USBname))
			except IOError:
				print ("\nCopy FAIL. Try again!\n")
except:
	try:
		config = open('Copy_Log_Config.txt','x+')
		config.write('--------------------------------------------------------------------------------\n')
		config.write('DLD_File_Type(File or Folder):\n')
		config.write('Folder\n')
		config.write('--------------------------------------------------------------------------------\n')
		config.write('PATH_DLD_LOG:\n')
		config.write(r'E:\1. STB MODEL\...'+'\n')
		config.write('--------------------------------------------------------------------------------\n')
		config.close
		print('Copy_Log_Config file has been created!')
	except:
		print('Please check information in Copy_Log_Config file!')

time.sleep(3)