import re,fileinput,os,sys

def getvoip():
	
	path=os.getcwd()+"/pcap_downloads/"
	os.chdir(path)
	osw= os.walk(path)

	for path, dirs, files in os.walk(path):
		for filename in files:
			fullpath = os.path.join(path, filename)
			os.system("sudo ../pcap2wav -z %s  %s" %(fullpath,filename))