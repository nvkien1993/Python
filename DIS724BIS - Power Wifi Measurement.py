import telnetlib
import time
import os
print('==== DSI724BIS - POWER MEASUREMENT ====')
ip = '192.168.100.1'
W1_5G_CH40 = 'wl ap 0;wl mpc 0;wl phy_watchdog 0;wl tempsense_disable 1;wl scansuppress 1;wl interference 0;wl down;wl band a;wl country ALL;wl bi 65535;wl ampdu 1;wl txchain 0x01;wl rxchain 0x01;wl 5g_rate -h 7 -b 20;wl chanspec 40/20;wl up;wl join aaa imode adhoc;wl disassoc;wl phy_forcecal 1;wl txpwr1 -o -d 14;wl pkteng_start 00:11:22:33:44:55 tx 100 1500 0;echo PKTENG_START_END'
W1_5G_CH60 = 'wl ap 0;wl mpc 0;wl phy_watchdog 0;wl tempsense_disable 1;wl scansuppress 1;wl interference 0;wl down;wl band a;wl country ALL;wl bi 65535;wl ampdu 1;wl txchain 0x01;wl rxchain 0x01;wl 5g_rate -h 7 -b 20;wl chanspec 60/20;wl up;wl join aaa imode adhoc;wl disassoc;wl phy_forcecal 1;wl txpwr1 -o -d 14;wl pkteng_start 00:11:22:33:44:55 tx 100 1500 0;echo PKTENG_START_END'
W1_5G_CH108 = 'wl ap 0;wl mpc 0;wl phy_watchdog 0;wl tempsense_disable 1;wl scansuppress 1;wl interference 0;wl down;wl band a;wl country ALL;wl bi 65535;wl ampdu 1;wl txchain 0x01;wl rxchain 0x01;wl 5g_rate -h 7 -b 20;wl chanspec 108/20;wl up;wl join aaa imode adhoc;wl disassoc;wl phy_forcecal 1;wl txpwr1 -o -d 14;wl pkteng_start 00:11:22:33:44:55 tx 100 1500 0;echo PKTENG_START_END'
W1_5G_CH153 = 'wl ap 0;wl mpc 0;wl phy_watchdog 0;wl tempsense_disable 1;wl scansuppress 1;wl interference 0;wl down;wl band a;wl country ALL;wl bi 65535;wl ampdu 1;wl txchain 0x01;wl rxchain 0x01;wl 5g_rate -h 7 -b 20;wl chanspec 153/20;wl up;wl join aaa imode adhoc;wl disassoc;wl phy_forcecal 1;wl txpwr1 -o -d 14;wl pkteng_start 00:11:22:33:44:55 tx 100 1500 0;echo PKTENG_START_END'
W2_5G_CH40 = 'wl ap 0;wl mpc 0;wl phy_watchdog 0;wl tempsense_disable 1;wl scansuppress 1;wl interference 0;wl down;wl band a;wl country ALL;wl bi 65535;wl ampdu 1;wl txchain 0x02;wl rxchain 0x02;wl 5g_rate -h 7 -b 20;wl chanspec 40/20;wl up;wl join aaa imode adhoc;wl disassoc;wl phy_forcecal 1;wl txpwr1 -o -d 14;wl pkteng_start 00:11:22:33:44:55 tx 100 1500 0;echo PKTENG_START_END'
W2_5G_CH60 = 'wl ap 0;wl mpc 0;wl phy_watchdog 0;wl tempsense_disable 1;wl scansuppress 1;wl interference 0;wl down;wl band a;wl country ALL;wl bi 65535;wl ampdu 1;wl txchain 0x02;wl rxchain 0x02;wl 5g_rate -h 7 -b 20;wl chanspec 60/20;wl up;wl join aaa imode adhoc;wl disassoc;wl phy_forcecal 1;wl txpwr1 -o -d 14;wl pkteng_start 00:11:22:33:44:55 tx 100 1500 0;echo PKTENG_START_END'
W2_5G_CH108 = 'wl ap 0;wl mpc 0;wl phy_watchdog 0;wl tempsense_disable 1;wl scansuppress 1;wl interference 0;wl down;wl band a;wl country ALL;wl bi 65535;wl ampdu 1;wl txchain 0x02;wl rxchain 0x02;wl 5g_rate -h 7 -b 20;wl chanspec 108/20;wl up;wl join aaa imode adhoc;wl disassoc;wl phy_forcecal 1;wl txpwr1 -d 14;wl pkteng_start 00:11:22:33:44:55 tx 100 1500 0;echo PKTENG_START_END'
W2_5G_CH153 = 'wl ap 0;wl mpc 0;wl phy_watchdog 0;wl tempsense_disable 1;wl scansuppress 1;wl interference 0;wl down;wl band a;wl country ALL;wl bi 65535;wl ampdu 1;wl txchain 0x02;wl rxchain 0x02;wl 5g_rate -h 7 -b 20;wl chanspec 153/20;wl up;wl join aaa imode adhoc;wl disassoc;wl phy_forcecal 1;wl txpwr1 -d 14;wl pkteng_start 00:11:22:33:44:55 tx 100 1500 0;echo PKTENG_START_END'
W1_2G_CH1 = 'wl ap 0;wl mpc 0;wl phy_watchdog 0;wl tempsense_disable 1;wl scansuppress 1;wl interference 0;wl down;wl band b;wl country ALL;wl bi 65535;wl ampdu 1;wl txchain 0x01;wl rxchain 0x01;wl 2g_rate -h 7 -b 20;wl chanspec 1/20;wl up;wl join aaa imode adhoc;wl disassoc;wl phy_forcecal 1;wl txpwr1 -o -d 14;wl pkteng_start 00:11:22:33:44:55 tx 100 1500 0;echo PKTENG_START_END'
W1_2G_CH7 = 'wl ap 0;wl mpc 0;wl phy_watchdog 0;wl tempsense_disable 1;wl scansuppress 1;wl interference 0;wl down;wl band b;wl country ALL;wl bi 65535;wl ampdu 1;wl txchain 0x01;wl rxchain 0x01;wl 2g_rate -h 7 -b 20;wl chanspec 7/20;wl up;wl join aaa imode adhoc;wl disassoc;wl phy_forcecal 1;wl txpwr1 -o -d 14;wl pkteng_start 00:11:22:33:44:55 tx 100 1500 0;echo PKTENG_START_END'
W1_2G_CH13 = 'wl ap 0;wl mpc 0;wl phy_watchdog 0;wl tempsense_disable 1;wl scansuppress 1;wl interference 0;wl down;wl band b;wl country ALL;wl bi 65535;wl ampdu 1;wl txchain 0x01;wl rxchain 0x01;wl 2g_rate -h 7 -b 20;wl chanspec 13/20;wl up;wl join aaa imode adhoc;wl disassoc;wl phy_forcecal 1;wl txpwr1 -o -d 14;wl pkteng_start 00:11:22:33:44:55 tx 100 1500 0;echo PKTENG_START_END'
W2_2G_CH1 = 'wl ap 0;wl mpc 0;wl phy_watchdog 0;wl tempsense_disable 1;wl scansuppress 1;wl interference 0;wl down;wl band b;wl country ALL;wl bi 65535;wl ampdu 1;wl txchain 0x02;wl rxchain 0x02;wl 2g_rate -h 7 -b 20;wl chanspec 1/20;wl up;wl join aaa imode adhoc;wl disassoc;wl phy_forcecal 1;wl txpwr1 -o -d 14;wl pkteng_start 00:11:22:33:44:55 tx 100 1500 0;echo PKTENG_START_END'
W2_2G_CH7 = 'wl ap 0;wl mpc 0;wl phy_watchdog 0;wl tempsense_disable 1;wl scansuppress 1;wl interference 0;wl down;wl band b;wl country ALL;wl bi 65535;wl ampdu 1;wl txchain 0x02;wl rxchain 0x02;wl 2g_rate -h 7 -b 20;wl chanspec 7/20;wl up;wl join aaa imode adhoc;wl disassoc;wl phy_forcecal 1;wl txpwr1 -o -d 14;wl pkteng_start 00:11:22:33:44:55 tx 100 1500 0;echo PKTENG_START_END'
W2_2G_CH13 = 'wl ap 0;wl mpc 0;wl phy_watchdog 0;wl tempsense_disable 1;wl scansuppress 1;wl interference 0;wl down;wl band b;wl country ALL;wl bi 65535;wl ampdu 1;wl txchain 0x02;wl rxchain 0x02;wl 2g_rate -h 7 -b 20;wl chanspec 13/20;wl up;wl join aaa imode adhoc;wl disassoc;wl phy_forcecal 1;wl txpwr1 -o -d 14;wl pkteng_start 00:11:22:33:44:55 tx 100 1500 0;echo PKTENG_START_END'
ip = '192.168.100.1'
for x in range(1,20):
	try:
		tn = telnetlib.Telnet(ip)
		time.sleep(0.2)
		tn.write(b'root\n')
		time.sleep(0.2)
		tn.write(b'source /usr/factory_tools/factory.sh\n')
		time.sleep(0.3)
		tn.write(b'Set_Wifi -m On\n')
		time.sleep(0.3)
		tn.write(b'Get_Wifi_Status\n')
		time.sleep(0.3)
		print(tn.read_very_eager().decode('ascii'))
		print('''	
		==== Power Wifi 5G/2.4G Item ====
		2.  TST#2  - PWR - W1/5G/CH40n
		3.  TST#3  - PWR - W1/5G/CH60n 
		4.  TST#4  - PWR - W1/5G/CH108n 
		5.  TST#5  - PWR - W1/5G/CH153n

		6.  TST#6  - PWR - W2/5G/CH40n
		7.  TST#7  - PWR - W2/5G/CH60n
		8.  TST#8  - PWR - W2/5G/CH108n 
		9.  TST#9  - PWR - W2/5G/CH153n 

		10. TST#10 - PWR - W1/2.4G/CH1n
		11. TST#11 - PWR - W1/2.4G/CH7n
		12. TST#12 - PWR - W1/2.4G/CH13n
		
		13. TST#13 - PWR - W2/2.4G/CH1n
		14. TST#14 - PWR - W2/2.4G/CH7n
		15. TST#15 - PWR - W2/2.4G/CH13n 
		''')
		for i in range(1, 100):
			item = input('Item test = ')
			if item == '2':
				tn.write(W1_5G_CH40.encode('ascii') + b'\n')
			elif item == '3':
				tn.write(W1_5G_CH60.encode('ascii') + b'\n')
			elif item == '4':
				tn.write(W1_5G_CH108.encode('ascii') + b'\n')
			elif item == '5':
				tn.write(W1_5G_CH153.encode('ascii') + b'\n')
			elif item == '6':
				tn.write(W2_5G_CH40.encode('ascii') + b'\n')
			elif item == '7':
				tn.write(W2_5G_CH60.encode('ascii') + b'\n')
			elif item == '8':
				tn.write(W2_5G_CH108.encode('ascii') + b'\n')
			elif item == '9':
				tn.write(W2_5G_CH153.encode('ascii') + b'\n')
			elif item == '10':
				tn.write(W1_2G_CH1.encode('ascii') + b'\n')
			elif item == '11':
				tn.write(W1_2G_CH7.encode('ascii') + b'\n')
			elif item == '12':
				tn.write(W1_2G_CH13.encode('ascii') + b'\n')
			elif item == '13':
				tn.write(W2_2G_CH1.encode('ascii') + b'\n')
			elif item == '14':
				tn.write(W2_2G_CH7.encode('ascii') + b'\n')
			elif item == '15':
				tn.write(W2_2G_CH13.encode('ascii') + b'\n')	
			else:
				print('\n==== NEW TELNET SESSION ====\n')
				break
	except IOError:
			print("\n==== Telnet Fail. Check connection! ====")
			reponse = os.system("ping 192.168.100.1 -t -n 5")
			print(reponse)