import telnetlib
import time
import os
print('+++ RECOVERY BP3 FILE +++\n')
ip = '192.168.100.1'
os.system ("adb connect 192.168.100.1")
time.sleep(0.5)
tn = telnetlib.Telnet(ip)
tn.write(b'Get_CPU_Description\n')
time.sleep(0.5)
CPU_Des = tn.read_very_eager().decode('ascii')
CPU_ID = (CPU_Des[len(CPU_Des)-102:len(CPU_Des)-86]).lower()
#print(CPU_ID)
list_bp3 = os.listdir()

#Rename bp3 file with first character is "-"
for bp3 in list_bp3:
	if bp3[0] == '-':
		new_bp3 = ""+bp3[1:len(bp3)]
		os.rename(bp3,""+bp3[1:len(bp3)])

#Recovery BP3
list_bp3 = os.listdir()
for bp3 in list_bp3:
	flag = bp3.find(CPU_ID)
	#print(flag)
	#print(bp3)
	if flag != -1:

		tn.write(b'Do_Memory_Write -o /dev/hwcfg/indivdatas.binary -a 0x000140 -d 0x02\n')
		time.sleep(0.5)
		os.system ("adb push %s /dev/hwcfg/bp3.bin"%(bp3))
		tn.write(b'sync\n')
		tn.write(b'reboot\n')
		print("\nRecovery %s Success!"%(bp3))
input()