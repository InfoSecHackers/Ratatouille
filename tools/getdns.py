import re,fileinput,os,sys

def getdns():

	try:

		path=os.getcwd()+"/pcap_downloads/"
		os.chdir(path)
		osw= os.walk(path)

		for path, dirs, files in os.walk(path):
			for filename in files:
				fullpath = os.path.join(path, filename)
				os.system("sudo python ../tools/pcap-dns.py %s " %fullpath)

	except Exception as e:

		print e
		os.chdir("..")
		getdns()