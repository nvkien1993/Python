import serial
import time
import os
console = serial.Serial()
console.baudrate = 9600
console.port = 'COM4'
console.open()

loop = int(input("Nhap so lan loop: "))
for i in range(1,loop+1):
	print("Vong loop "+str(i))
	console.write(b'RELAY1_ON\r\n')
	print('ON')
	time.sleep(2)
	console.write(b'RELAY1_OFF\r\n')
	print('OFF')
	time.sleep(2)

input("Finished")
