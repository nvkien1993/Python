import time
import serial
config = open('config.cfg').read()
RELAY_PORT = config[config.find('RELAY_PORT:')+11:config.find('\n',config.find('RELAY_PORT'))]
CONSOLE_PORT = config[config.find('CONSOLE_PORT:')+13:config.find('\n',config.find('CONSOLE_PORT'))]
KEY_WORD_PASS = config[config.find('KEY_WORD_PASS:')+14:config.find('\n',config.find('KEY_WORD_PASS'))]
KEY_WORD_FAIL = config[config.find('KEY_WORD_FAIL:')+14:config.find('\n',config.find('KEY_WORD_FAIL'))]

print("RELAY_PORT:"+RELAY_PORT)
print("CONSOLE_PORT:"+CONSOLE_PORT)
print("KEY_WORD_PASS:"+KEY_WORD_PASS)
print("KEY_WORD_FAIL:"+KEY_WORD_FAIL)
#=============================Console================================

console = serial.Serial()
console.baudrate = 115200
console.port = CONSOLE_PORT
console.open()

relay = serial.Serial()
relay.baudrate = 9600
relay.port = RELAY_PORT
relay.open()


print('==========READ CONSOLE============')
relay.write(b'RELAY1_ON\r\n')
count = 1
while True:
	data = console.readline().decode(encoding='ASCII',errors='ignore')
	index_pass = data.find(KEY_WORD_PASS)
	index_fail = data.find(KEY_WORD_FAIL)
	Log_File = open('Log'+str(count)+'.txt','a+')
	Log_File.write(data)
	print(data,end='')
	if index_pass !=-1:
		relay.write(b'RELAY1_OFF\r\n')
		print('+++++++++++++++++++RELAY OFF+++++++++++++++++++')
		#Log_File.write('+++++++++++++++++++RELAY OFF+++++++++++++++++++\n')
		time.sleep(2)
		relay.write(b'RELAY1_ON\r\n')
		print('+++++++++++++++++++RELAY ON+++++++++++++++++++')
		Log_File.write('+++++++++++++++++++PASS+++++++++++++++++++\n')
		Log_File.close()
		count = count +1

	if index_fail !=-1:
		relay.write(b'RELAY1_OFF\r\n')
		print('+++++++++++++++++++RELAY OFF+++++++++++++++++++')
		#Log_File.write('+++++++++++++++++++RELAY OFF+++++++++++++++++++\n')
		time.sleep(2)
		relay.write(b'RELAY1_ON\r\n')
		print('+++++++++++++++++++RELAY ON+++++++++++++++++++')
		Log_File.write('+++++++++++++++++++FAIL+++++++++++++++++++\n')
		Log_File.close()
		count = count +1
	#update more line code
	#finish
	#Log_File.close()
