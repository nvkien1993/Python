import telnetlib
import serial
import time
import os
from datetime import datetime, date
console = serial.Serial()
console.baudrate = 9600
console.port = 'COM4'
console.open()
Loop_Num = 0
PASS_Num = 0
FAIL_Num = 0

#print(tn.read_very_eager().decode('ascii'))
#time.sleep(2)
start_time = time.time()
current_time = datetime.now().strftime("%H_%M_%S")
today = date.today().strftime("%d_%m_%Y")
while True:

	try:
		console.write(b'RELAY1_ON\r\n')
		print('RELAY1_ON')
		ip = '192.168.1.1'
		tn = telnetlib.Telnet(ip)
		tn.write(b'admin\n')
		time.sleep(1)
		tn.write(b'admin\n')
		time.sleep(1)
		tn.write(b'sh\n')
		time.sleep(1)

		
		#for loop in range(0,int(loop_num)):
		try:
			os.mkdir('Log')
		except:
			try:
				os.mkdir('Log\\'+today)
			except:
				
				Data = open('Log\\'+today+'\\'+current_time+'.txt', 'a',encoding ='utf-8', errors = 'replace')
				end_time = time.time() - start_time
				print('======================================================================')
				Data.write('======================================================================\n')
				console.write(b'RELAY1_ON\r\n')
				#print('RELAY1_ON')
				tn.write(b'wl -i wl0 ver\n')
				time.sleep(1)
				result=tn.read_very_eager().decode('ascii')
				print(result)
				Data.write('%s\n'%(result))
				flag1=result.find('17.10.188.75',0)
				#print(flag1)

				tn.write(b'wl -i wl1 ver\n')
				time.sleep(1)
				result=tn.read_very_eager().decode('ascii')
				print(result)
				Data.write('%s\n'%(result))
				flag2=result.find('17.10.188.75',0)
				#print(flag2)

				tn.write(b'wl -i wl2 ver\n')
				time.sleep(1)
				result=tn.read_very_eager().decode('ascii')
				print(result)
				Data.write('%s\n'%(result))
				flag3=result.find('17.10.188.75',0)
				#print(flag3)

				if (flag1!=-1) and (flag2!=-1) and (flag3!=-1):
					
					PASS_Num = PASS_Num + 1
					print('PASS')
					print('PASS:%s | FAIL:%s'%(PASS_Num,FAIL_Num))
					Data.write('PASS\n')
					Data.write('PASS:%s | FAIL:%s\n'%(PASS_Num,FAIL_Num))

				else:
					print('FAIL\n')
					Data.write('FAIL\n')
					FAIL_Num = FAIL_Num + 1
					print('FAIL')
					print('PASS:%s | FAIL:%s'%(PASS_Num,FAIL_Num))
					Data.write('FAIL\n')
					Data.write('PASS:%s | FAIL:%s\n'%(PASS_Num,FAIL_Num))


				console.write(b'RELAY1_OFF\r\n')
				print('RELAY1_OFF')
				time.sleep(2)
				Loop_Num = Loop_Num +1
				#print("Loop = "+str(Loop_Num))
				#Data.write("Loop = "+str(Loop_Num)+"\n")
				Data.close()
	except IOError:
			print("Waiting Product Bootup ...")
			Data = open('Log\\'+today+'\\'+current_time+'.txt', 'a',encoding ='utf-8', errors = 'replace')
			Data.write('Waiting Product Bootup ...\n')
			Data.close()
			time.sleep(10)