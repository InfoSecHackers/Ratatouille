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
cur.execute("SELECT * FROM capture_start WHERE interface IS NOT NULL")
for i in cur.fetchall():
	try:
		ip=i[1]
		ip=str(ip)
		print "Starting Capture On ",ip
		username=i[2]
		password=i[3]
		enpassword=i[4]
		interface =i[5]
		interface=str(interface)
		command="telnet "+ip
		child = pexpect.spawn(command )
		child.expect(":") # timeout in seconds
		child.sendline(username)
		child.expect(":" )
		child.sendline(password)
		child.sendline("en")
		child.expect(":")
		child.sendline(enpassword)
		child.expect("")
		child.sendline("configure terminal")
		child.expect("")
		child.sendline("ip access-list extended cap")
		child.expect("")
		child.sendline("permit ip any any")
		child.expect("")
		child.sendline("end")
		child.expect("")
		child.sendline("monitor capture buffer buff circular")
		child.expect("")
		child.sendline("monitor capture buffer buff filter access-list cap")
		child.expect("")
		cmd = "monitor capture point ip cef trace %s both"%interface
		child.sendline(cmd)
		child.expect("")
		child.sendline("mon cap point associate trace buff")
		child.expect("")
		child.sendline("monitor capture buffer buff size 50000")
		child.expect("")
		child.sendline("monitor capture buffer buff max-size 5000")
		child.expect("")
		child.sendline("monitor capture point start trace")
		child.expect("")
		child.sendline("exit")
		child.expect("")
		query = "UPDATE capture_start SET status = %s WHERE ip = %s"
		stat = 'Running'
		val = (stat,ip)
		cur.execute(query,val)
		mydb.commit()
		#child.interact() # gives control to the user
		time.sleep(10)
	except Exception, e:
        	#print("error %s " %e )
		pass
cur.close()
	
	
