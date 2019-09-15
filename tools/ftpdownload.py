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
# Print out the files
for file in files:
	
	print("Downloading..." + file)
	ftp.retrbinary("RETR " + file ,open(loc+'/'+ file, 'wb').write)
	ftp.delete(file)

ftp.close()

end = datetime.now()
diff = end - start
print('All files downloaded for ' + str(diff.seconds) + 's')