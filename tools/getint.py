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
cur.execute("SELECT * FROM capture_start WHERE interface IS NULL")
for i in cur.fetchall():
	try:	
		ip=i[1]
		ip=str(ip)
		username=i[2]
		password=i[3]
		enpassword=i[4]
		print "Getting interface of ",ip
		command="telnet "+ip
		child = pexpect.spawn(command )
		child.expect(":") # timeout in seconds
		child.sendline(username)
		child.expect(":" )
		child.sendline(password)
		child.expect(">" )
		child.sendline("en")
		child.expect(":")
		child.sendline(enpassword)
		child.expect("#" )
		child.sendline("show ip int brief")
		child.expect("#" )
		interface = child.before
		child.sendline("exit")
		sint = interface.split("\n")
		for line in reversed(sint):
			if ip in line:
				line2 = line.split(" ")
				print "Found Interface",line2[0]
				query = "UPDATE capture_start SET interface = %s ,allinterface= %s WHERE ip = %s"
				val = (line2[0],interface,ip)
				cur.execute(query,val)
				mydb.commit()
		child.interact()
		time.sleep(10) # gives control to the user
	except Exception, e:
        	print("error %s " %e)
		pass
cur.close()	
	
	
