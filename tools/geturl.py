import re,fileinput,os,sys

def geturl():

	try:

		path=os.getcwd()+"/pcap_downloads/"
		os.chdir(path)
		osw= os.walk(path)

		for path, dirs, files in os.walk(path):
			for filename in files:
				fullpath = os.path.join(path, filename)
				os.system("sudo python ../tools/parse.py %s " %fullpath)

	except Exception as e:

		print e
		os.chdir("..")
		geturl()