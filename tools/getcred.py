import re,fileinput,os,sys

def getcred():

	path=os.getcwd()+"/pcap_downloads/"
	print os.getcwd()
	os.chdir(path)
	osw= os.walk(path)

	for path, dirs, files in os.walk(path):
		for filename in files:
			fullpath = os.path.join(path, filename)
			os.system("sudo python ../tools/net-creds.py -p %s " %fullpath)
#os.chdir("..")