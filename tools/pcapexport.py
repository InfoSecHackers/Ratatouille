import os
import time
import socket
import platform
import pexpect
import MySQLdb
import re
import datetime
import db
import configparser
config = configparser.ConfigParser()
config.read('config/ftpconfig.ini')
mydb = db.connect()
cur = mydb.cursor()
ts = time.time()
timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
cur.execute("SELECT * FROM capture_start WHERE status='Running'")
for i in cur.fetchall():
	try:
		ip=i[1]
		ip=str(ip)
		print ip
		username=i[2]
		password=i[3]
		enpassword=i[4]
		country = i[9]
		command="telnet "+ip
		ftp_ip=config['ftp']['ftp-ip']
		ftp_username = config['ftp']['ftp-username']
		ftp_password = config['ftp']['ftp-password']
		export="monitor capture buffer buff export ftp://%s:%s@%s/%s-%s.pcap"%(ftp_username,ftp_password,ftp_ip,ip,country)
		child = pexpect.spawn(command )
		child.expect(":", timeout=10) # timeout in seconds
		child.sendline(username)
		child.expect(":" , timeout=10)
		child.sendline(password)
		child.sendline("en")
		child.sendline(enpassword)
		child.sendline("monitor capture point stop trace")
		child.sendline(export)
		child.sendline("monitor capture buffer buff clear")
		child.sendline("monitor capture point start trace")
		child.expect("#" , timeout=10)
		child.sendline("exit")
		query = "UPDATE capture_start SET records = %s WHERE ip = %s"
		val = (timestamp,ip)
		cur.execute(query,val)
		mydb.commit()
		child.interact() 
	except Exception, e:
        	#print("error %s with host" %e )
		pass
cur.close()