from ftplib import FTP
from datetime import datetime
import time
from datetime import date
import os
import configparser
import re
config = configparser.ConfigParser()
config.read('config/ftpconfig.ini')

start = datetime.now()
dirdate= date.today()

ftp_ip=config['ftp']['ftp-ip']
ftp_username = config['ftp']['ftp-username']
ftp_password = config['ftp']['ftp-password']
ftp = FTP(ftp_ip)
ftp.login(ftp_username,ftp_password)

# Get All Files
files = ftp.nlst()
loc = "pcap_downloads/%s/"%dirdate
os.mkdir(loc)
os.mkdir(loc+'UAE')
os.mkdir(loc+'SAUDI')
os.mkdir(loc+'EGYPT')
os.mkdir(loc+'BAHRAIN')
# Print out the files
for file in files:
	fi1 = file.split('-')
	fi = fi1[1].split('.')
	print fi[0]
	print("Downloading..." + file)
	if 'UAE' in fi[0]:
		ftp.retrbinary("RETR " + file ,open(loc+'/UAE/'+ file, 'wb').write)
		ftp.delete(file)
	elif 'SAUDI' in fi[0]:
		ftp.retrbinary("RETR " + file ,open(loc +'/SAUDI/'+ file, 'wb').write)
		ftp.delete(file)
	elif 'BAHRAIN' in fi[0]:
		ftp.retrbinary("RETR " + file ,open(loc +'/BAHRAIN/'+ file, 'wb').write)
		ftp.delete(file)
	elif 'EGYPT' in fi[0]:
		ftp.retrbinary("RETR " + file ,open(loc +'/EGYPT/'+ file, 'wb').write)
		ftp.delete(file)
	else:
		print 'No Country Found'

ftp.close()

end = datetime.now()
diff = end - start
print('All files downloaded for ' + str(diff.seconds) + 's')

