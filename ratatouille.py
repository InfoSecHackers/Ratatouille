#import capturestart
#import capturestop
#import ftpdownload
#import getint
#import pcapexport

import argparse
import sys

try:
	parser = argparse.ArgumentParser(description='Advanced Tool For Router PacketCapture and Analysis')
	parser.add_argument("option", default='help')
	args = parser.parse_args()
	parser.print_help()

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
	elif args.option == 'getcred':
		from tools import getcred
	elif args.option == 'geturl':
		from tools import geturl
	elif args.option == 'getfile':
		from tools import getfile
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
                getcred     Extract Credentials from PCAP
                geturl      Extract HTTP Url's From PCAP
                getfile     Extract Files From PCAP \n"""
	else:
		print "Enter help for uses" 
except Exception, e:
    pass
