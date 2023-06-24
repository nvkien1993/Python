from ftplib import FTP
import socket,os,sys,time,threading
Version_Name = "Send & Receive V4"
Version = int(Version_Name[16:17])
def Send():
	try:
		print(open('config.cfg').read())
		config = open('config.cfg').readlines()
		while True:
			try:
				i = input()
				if int(i) > 0 and int(i) < len(config)-1:
					IP = config[int(i)][config[int(i)].find(':')+1:config[int(i)].find('\n')]
					PORT = 6900
					server_address = (IP, PORT)
					print('Connected to %s'%IP)
					while True:
						input_path = input()
						index = input_path.find('"')
						FTP_CLIENT = FTP("10.228.110.181")
						FTP_CLIENT.login(user="F1313128", passwd = "F1313128")
						FTP_CLIENT.cwd("/mnt/hdd1/F1313128/PE/HARRY/Send & Receive")
						
						#Chuong trinh con push file len FTP
						def Pushfile(FTP_CLIENT, PATH_FOLDER):
							for NAME in os.listdir(PATH_FOLDER):
								#print(NAME)
								FULLPATH = os.path.join(PATH_FOLDER, NAME)
								if os.path.isfile(FULLPATH):
									print(NAME)
									FTP_CLIENT.storbinary('STOR ' + NAME, open(FULLPATH,'rb'))
								elif os.path.isdir(FULLPATH):
									try:
										FTP_CLIENT.mkd(NAME)
									except:
										pass
									FTP_CLIENT.cwd(NAME)
									Pushfile(FTP_CLIENT, FULLPATH)		   
									FTP_CLIENT.cwd("..")
						#----------------------------------------------------------------------
						if index !=-1: #link included "". Example: "C:\Users\"
							path1 = input_path[1:len(input_path)-1]
							if os.path.isfile(path1): # file
								file_name = path1.split('\\')[len(path1.split('\\'))-1]
								#print(file_name)
								FTP_CLIENT.storbinary('STOR '+file_name, open(path1,'rb'))
								s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
								s.connect(server_address)
								s.sendall(bytes(file_name, "UTF-8"))
								s.close()
								print("--> [Send Done]")
							elif os.path.isdir(path1): #folder
								RootFolder = path1.split('\\')[len(path1.split('\\'))-1]
								try:
									FTP_CLIENT.mkd(RootFolder)
								except:
									pass
								FTP_CLIENT.cwd(RootFolder)
								Pushfile(FTP_CLIENT, path1)
								s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
								s.connect(server_address)
								s.sendall(bytes(RootFolder, "UTF-8"))
								s.close()
								print("--> [Send Done]")
						else:	#link not included "". Example: C:\Users\
							if os.path.isfile(input_path): # file
								file_name = input_path.split('\\')[len(input_path.split('\\'))-1]
								#print(file_name)
								FTP_CLIENT.storbinary('STOR '+file_name, open(input_path,'rb'))
								s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
								s.connect(server_address)
								s.sendall(bytes(file_name, "UTF-8"))
								s.close()
								print("--> [Send Done]")
							elif os.path.isdir(input_path): #folder
								RootFolder = input_path.split('\\')[len(input_path.split('\\'))-1]
								try:
									FTP_CLIENT.mkd(RootFolder)
								except:
									pass
								FTP_CLIENT.cwd(RootFolder)
								Pushfile(FTP_CLIENT, input_path)
								s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
								s.connect(server_address)
								s.sendall(bytes(RootFolder, "UTF-8"))
								s.close()
								print("--> [Send Done]")
			except:
				if i =="exit":
					break
				else:
					pass
	except:
		config = open('config.cfg','x+')
		config.write('----------------------------\n1.Harry:10.228.28.131\n----------------------------')
		config.close()
		print('Config File Has Been Created!')
		time.sleep(1)

def Receive():
	PORT = 6900		
	PC_Name = socket.gethostname()
	HOST = socket.gethostbyname(PC_Name)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((HOST, PORT))
	s.listen(2)
	print('----------------------------')
	print ('PC: %s'%(PC_Name))
	print ('IP: %s'%(HOST))
	try:
		while True:
			client, addr = s.accept()
			data = client.recv(1024)
			str_data = data.decode("utf8")
			FTP_CLIENT = FTP("10.228.110.181")
			FTP_CLIENT.login(user="F1313128", passwd="F1313128")
			Storage_path = "/mnt/hdd1/F1313128/PE/HARRY/Send & Receive"
			FTP_CLIENT.cwd(Storage_path)
			Path = Storage_path + '/' + str_data
			try:
				FTP_CLIENT.cwd(Path)
				try:
					os.mkdir(str_data)
				except:
					pass
				os.chdir(str_data)
				def Getfile():
					for name_list in FTP_CLIENT.nlst():
						try:
							FTP_CLIENT.cwd(name_list)
							try:
								os.mkdir(name_list)
							except:
								pass
							os.chdir(name_list)
							Getfile()
							FTP_CLIENT.cwd('..')
							FTP_CLIENT.rmd(name_list)
							os.chdir('..')
						except:
							print('[%s] %s'%(addr[0],name_list))
							current_path = os.getcwd()
							localpath = os.path.join(current_path, name_list)
							FTP_CLIENT.retrbinary('RETR ' + name_list, open(localpath,'wb').write)
							FTP_CLIENT.delete(name_list)
				Getfile()
				os.chdir('..')
				FTP_CLIENT.cwd(Storage_path)
				FTP_CLIENT.rmd(str_data)
				
				
			except:
				current_path = os.getcwd()
				localpath = os.path.join(current_path, str_data)
				FTP_CLIENT.retrbinary('RETR ' + str_data, open(localpath,'wb').write)
				print('[%s] %s'%(addr[0],str_data))
				FTP_CLIENT.delete(str_data)
			print("--> [Receive Done]")
	except:
		pass

def Update():
	#os.system('cls')
	FTP_CLIENT = FTP("10.228.110.181")
	FTP_CLIENT.login(user="F1313128", passwd = "F1313128")
	FTP_CLIENT.cwd("/mnt/hdd1/F1313128/PE/HARRY/Send & Receive/Updates")
	update_value = FTP_CLIENT.nlst()
	if update_value !=[]:
		for update in FTP_CLIENT.nlst():
			print('''A new version of Upgrader is avaiable! Version is "%s"\n'''%(update))
			FTP_CLIENT.retrbinary('RETR ' + update, open(update,'wb').write)
			print("Latest Version Already Updated!")
		
	else:
		print("This is latest version!")
	input()

if __name__ =="__main__":
	FTP_CLIENT = FTP("10.228.110.181")
	FTP_CLIENT.login(user="F1313128", passwd = "F1313128")
	FTP_CLIENT.cwd("/mnt/hdd1/F1313128/PE/HARRY/Send & Receive/Updates")
	update_value = FTP_CLIENT.nlst()
	if update_value !=[]:
		try:
			New_Version = int(update_value[0][16:17])
		except:
			input('New Version Check Failed!')
			exit()
		if New_Version > Version:
			FTP_CLIENT.retrbinary('RETR ' + update_value[0], open(update_value[0],'wb').write)
			input("New Version V"+str(New_Version) + " Already Updated!")
			exit()

	print(Version_Name)

	Thread_Receive = threading.Thread(target=Receive)
	Thread_Send = threading.Thread(target=Send)
	
	Thread_Receive.start()
	time.sleep(0.02)
	Thread_Send.start()