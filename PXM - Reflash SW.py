import serial
import time
import os
try:	
	console = serial.Serial()
	console.baudrate = 115200
	console.port = 'COM1'
	console.open()
	print('************** Reflash SW ***************')
	while True:
		data = console.readline().decode(encoding='ASCII',errors='ignore')
		#data = console.readline().decode(encoding='ASCII')
		print(data,end='')
		key_word1 = data.find('Board:')
		key_word2 = data.find('CFG_CUSTOM_CODE in custom_main')
		key_word3 = data.find('ipaddr')
		key_word4 = data.find('splash-feedback: failed to open media 2')

		if key_word1 !=-1:
			console.write(b'\x03') #CTRL + C
		if key_word2 !=-1:
			console.write(b'\n')
			console.write(b'verifyboot -bsu flash0.bsu_i;android fastboot -transport=tcp -device=flash0\n')
		if key_word3 !=-1:
			index = data.find(',',key_word3)
			IP = data[key_word3+7:index]
			print(IP)
		if key_word4 !=-1:
			console.close()
			os.system('RUN.bat '+IP)
			print('\n********************* Finished! **********************\n')
			console.open()
except:
	input('Errors or no found RUN.bat. Please try again! ')
