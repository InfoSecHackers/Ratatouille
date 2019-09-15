import argparse
import sys,os

started =os.getcwd()

try:
	parser = argparse.ArgumentParser(description='Advanced Tool For Router PacketCapture and Analysis')
	parser.add_argument("option", default='help')
	args = parser.parse_args()

	#print sys.argv[1]
	if args.option == 'getint':
		from tools import getint
	elif args.option == 'start':
		from tools import capturestart
	elif args.option == 'stop':
		from tools import capturestop
	elif args.option == 'export':
		from tools import pcapexport
	elif args.option == 'download':
		from tools import ftpdownload
	elif args.option == 'getrouter':
		from tools import getrouter
	elif args.option == 'analyse':
		from tools import getcred
		getcred.getcred()
		os.chdir(started)
		from tools import geturl
		geturl.geturl()
		os.chdir(started)
		from tools import getfile
		getfile.getfile()
		os.chdir(started)
		from tools import getvoip
		getvoip.getvoip()
		os.chdir(started)
		from tools import getdns
		getdns.getdns()
		os.chdir(started)
		from tools import getgraph
		getgraph.getgraph()
		os.chdir(started)
		from tools import clean
		clean.clean()
		os.chdir(started)
		os.system("sudo python3 insert.py")
	elif args.option == "help":
		print """
Description:

    Advanced Tool For Router PacketCapture and Analysis

        Arguments:
        
            Capture:
                getrouter   Get username password of router
                getint      Get Active Interface of Router
                start       Start PacketCapture On Router
                stop        Stop PacketCapture On Router
                export      Export Captured Packets To FTP SERVER
                download    Download PCAPS From FTP
                
            Analysis:
                analyse 	It will Extract Credentials, HTTP Url's, Files, VOIP Calls, Dns Requests From PCAP to output/ folder and it will make IP source and Destination Link \n"""
	else:
		print "Enter help for uses" 
except Exception, e:
	print e
    #pass
