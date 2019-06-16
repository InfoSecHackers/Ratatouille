import os
import time
import socket
import platform
import pexpect
import MySQLdb
import re
import db
mydb = db.connect()
cur = mydb.cursor()
cur.execute("SELECT * FROM capture_start WHERE status ='Running'")
for i in cur.fetchall():
	try:
		ip=i[1]
		ip=str(ip)
		print ip
		username=i[2]
		password=i[3]
		enpassword=i[4]
		command="telnet "+ip
		child = pexpect.spawn(command )
		child.expect(":", timeout=10) # timeout in seconds
		child.sendline(username)
		child.expect(":" , timeout=10)
		child.sendline(password)
		child.sendline("en")
		child.sendline(enpassword)
		child.sendline("monitor capture point stop trace")
		child.sendline("monitor capture buffer buff clear")
		child.expect("#" , timeout=10)
		child.sendline("exit")
		query = "UPDATE capture_start SET status = %s WHERE ip = %s"
		stat = 'Stopped'
		val = (stat,ip)
		cur.execute(query,val)
		mydb.commit()
		#child.interact() # gives control to the user
	except Exception, e:
        	#print("error %s with host" %e )
		pass
cur.close()