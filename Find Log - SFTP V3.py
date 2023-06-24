import paramiko, os, shutil

try:
	config = open('config.cfg').read()
	ListSN = open('SN.txt').read().split('\n')

	FTP_ADDRESS = config[config.find('FTP_ADDRESS:')+12:config.find('\n',config.find('FTP_ADDRESS:'))]
	FTP_USER = config[config.find('FTP_USER:')+9:config.find('\n',config.find('FTP_USER:'))]
	FTP_PASS = config[config.find('FTP_PASS:')+9:config.find('\n',config.find('FTP_PASS:'))]
	FTP_PORT = config[config.find('FTP_PORT:')+9:config.find('\n',config.find('FTP_PORT:'))]
	Model = config[config.find('Model:')+6:config.find('\n',config.find('Model:'))]
	Station = config[config.find('Station:')+8:config.find('\n',config.find('Station:'))].split(',')
	FTP_Path = config[config.find('FTP_Path:')+9:config.find('\n',config.find('FTP_Path:'))]

	Start_Time = config[config.find('Start_Time:')+11:config.find('\n',config.find('Start_Time:'))]
	End_Time = config[config.find('End_Time:')+9:config.find('\n',config.find('End_Time:'))]
	start_day = int(Start_Time[0:2])
	start_month = int(Start_Time[3:5])
	start_year = int(Start_Time[6:10])

	end_day = int(End_Time[0:2])
	end_month = int(End_Time[3:5])
	end_year = int(End_Time[6:10])

	if end_day < 10:
		if end_month <10:
			End_Time_Compare = str(end_year)+'-'+'0'+str(end_month)+'-'+'0'+str(end_day)
		else:
			End_Time_Compare = str(end_year)+'-'+str(end_month)+'0'+'-'+str(end_day)
	else:
		if end_month <10:
			End_Time_Compare = str(end_year)+'-'+'0'+str(end_month)+'-'+str(end_day)
		else:
			End_Time_Compare = str(end_year)+'-'+str(end_month)+'-'+str(end_day)
	for folder in ListSN:
		Path_log = Model + '_' + folder
		try:
			os.mkdir(Path_log)
		except:
			shutil.rmtree(Path_log)
			os.mkdir(Path_log)

	Path_folder = os.getcwd()
	Transport = paramiko.Transport((FTP_ADDRESS,int(FTP_PORT)))
	Transport.connect(None,FTP_USER,FTP_PASS) 
	Sftp_Client = paramiko.SFTPClient.from_transport(Transport)

	print('Model: '+Model)
	for s in Station:
		print('\n+++ '+s+' Station'+' +++')
		Sftp_Client.chdir(FTP_Path+Model+'/'+s)

		for TestPC in Sftp_Client.listdir():
			#print('++++++++++++++++'+ TestPC)
			day = start_day
			try:
				Sftp_Client.chdir(FTP_Path+Model+'/'+s+'/'+TestPC)
				for y in range(0, end_year - start_year +1):
					if y ==0:
						for m in range(start_month,13):
							for d in range(day,32):
								if d < 10:
									if m < 10:
										Time_Compare = str(start_year + y)+'-'+'0'+str(m)+'-'+'0'+str(d)
									else:
										Time_Compare = str(start_year + y)+'-'+ str(m)+'-'+'0'+str(d)
								else:
									if m < 10:
										Time_Compare = str(start_year+y)+'-'+'0'+str(m)+'-'+str(d)
									else:
										Time_Compare = str(start_year+y)+'-'+ str(m)+'-'+str(d)
								try:
									Sftp_Client.chdir(FTP_Path+Model+'/'+s+'/'+TestPC+'/'+Time_Compare)
									List_Log = Sftp_Client.listdir()
									for Log_file in List_Log:
										for SN in ListSN:
											flag = Log_file.find(SN)
											if flag != -1:
												print(TestPC +'    ' +Time_Compare +'    ' +Log_file)
												Sftp_Client.get(FTP_Path+Model+'/'+s+'/'+TestPC+'/'+Time_Compare+'/'+Log_file,Path_folder+'/'+Model+'_'+SN+'/'+s+'_'+TestPC+'_'+Time_Compare+'_'+Log_file)
								
								except:
									error = 1
								day = 1
								#print(Time_Compare)
								if End_Time_Compare == Time_Compare:
									break
							if End_Time_Compare == Time_Compare:
									break
					else:
						for m in range(1,13):
							for d in range(1,32):
								if d < 10:
									if m < 10:
										Time_Compare = str(start_year + y)+'-'+'0'+str(m)+'-'+'0'+str(d)
									else:
										Time_Compare = str(start_year + y)+'-'+ str(m)+'-'+'0'+str(d)
								else:
									if m < 10:
										Time_Compare = str(start_year+y)+'-'+'0'+str(m)+'-'+str(d)
									else:
										Time_Compare = str(start_year+y)+'-'+str(m)+'-'+str(d)
								try:
									Sftp_Client.chdir(FTP_Path+Model+'/'+s+'/'+TestPC+'/'+Time_Compare)
									List_Log = Sftp_Client.listdir()
									for Log_file in List_Log:
										for SN in ListSN:
											flag = Log_file.find(SN)
											if flag != -1:
												print(TestPC +'    ' +Time_Compare +'    ' +Log_file)
												print('test')
												Sftp_Client.get(FTP_Path+Model+'/'+s+'/'+TestPC+'/'+Time_Compare+'/'+Log_file,Path_folder+'/'+Model+'_'+SN+'/'+s+'_'+TestPC+'_'+Time_Compare+'_'+Log_file)
												#print(Path_folder+'/'+Model+'_'+'SN'+'/'+s+'_'+Log_file)
								except:
									error = 1
								#print(Time_Compare)
								if End_Time_Compare == Time_Compare:
									break
							if End_Time_Compare == Time_Compare:
								break
			except:
				error=1					
	input('\n@Harry\n\nVersion: 03\n\nPress Enter To Exit!')
except:
	try:
		config = open('config.cfg','x+')
		config.write('------------------FTP Information------------------\nFTP_ADDRESS:10.228.110.182\nFTP_USER:Logs\nFTP_PASS:Logs\nFTP_PORT:6900\nFTP_Path:/mnt/hdd2/Logs/Logs/\n-----------Time Information (DD/MM/YYYY)-----------\nStart_Time:01/08/2022\nEnd_Time:24/08/2022\n----------------Product Information----------------\nModel:U46C382.25\nStation:PT,FT1,RC,RC1,UK,RC2\n---------------------------------------------------')
		config.close()
		input('config.cfg file has been created. Press Enter To Exit!\n')
	except:
		try:
			config = open('SN.txt','x+')
			input('SN.txt file has been created. Press Enter To Exit!\n')
		except:
			input('Please check information in config.cfg & SN.txt. Press Enter To Exit!')
	