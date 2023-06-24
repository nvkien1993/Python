import telnetlib
import time
import os
print('+++ BACKUP BP3 FILE +++\n')
ip = '192.168.100.1'
os.system ("adb connect 192.168.100.1")
time.sleep(0.5)
tn = telnetlib.Telnet(ip)
tn.write(b'Get_CPU_Description\n')
time.sleep(0.5)
CPU_Des = tn.read_very_eager().decode('ascii')
CPU_ID = (CPU_Des[len(CPU_Des)-102:len(CPU_Des)-86]).lower()
#print(CPU_ID)
os.system ("adb pull /dev/hwcfg/bp3.bin %s"%(CPU_ID+'-BP3.bin'))
print("\nBackup %s Success!"%(CPU_ID+'-BP3.bin'))
input()
