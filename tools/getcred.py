import re,fileinput,os,sys
from colorama import Style 

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

try:
	path="pcap_downloads"
	os.chdir(path)

	for path, dirs, files in os.walk(path):
		for filename in files:
			fullpath = os.path.join(path, filename)
			pwd = os.getcwd()
			print pwd
			try:
				os.system("sudo %s/net-creds.py -p %s " %(pwd,fullpath))
			except Exception, e:
				print e
except IndexError,NameError:
	print (bcolors.OKBLUE+bcolors.BOLD +"\nUses: pyhton re-net-creds.py dir-path-of-pcapfiles")
	print(Style.RESET_ALL)