#!/usr/bin/env python

# by @catalyst256
import sys
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
from datetime import date

# Add some colouring for printing packets later
YELLOW = '\033[93m'
GREEN = '\033[92m'
END = '\033[0m'
RED = '\033[91m'

def find_dns(pkts,outfname):
	o = open(outfname, "a")
	for p in pkts:
		if p.haslayer(DNSQR) and p.haslayer(DNSRR):
			rrname = p.getlayer(DNSRR).rrname
			ancount = p.getlayer(DNS).ancount
			rttl = p.getlayer(DNSRR).ttl
			rdata = p.getlayer(DNSRR).rdata
			data = rrname, ancount, rttl, rdata
			if ancount > 4:
				print RED + '[-] DNS Query for: ' + rrname + ' / TTL: ' + str(rttl) + ' / Returned IP: ' + rdata + ' / Number of records: ' + str(ancount) + END
				o.write('[-] DNS Query for: ' + rrname + ' / TTL: ' + str(rttl) + ' / Returned IP: ' + rdata + ' / Number of records: ' + str(ancount) + '\n')
			else:
				print YELLOW +'[-] DNS Query for: ' + rrname + ' / TTL: ' + str(rttl) + ' / Returned IP: ' + rdata + ' / Number of records: ' + str(ancount) + END
				o.write('[-] DNS Query for: ' + rrname + ' / TTL: ' + str(rttl) + ' / Returned IP: ' + rdata + ' / Number of records: ' + str(ancount) + '\n')
	o.close()

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print 'Usage is ./pcap-dns.py <input pcap file>'
		print 'Example - ./pcap-dns.py sample.pcap'
		sys.exit(1)

	pkts = rdpcap(sys.argv[1])
	dns_records = []
	print GREEN + '[+] Initial DNS Dump....' + END
	dirdate= str(date.today())
	fname = os.path.split(os.getcwd())[0]
	filename = os.path.basename(sys.argv[1])
	filename = filename.replace('.pcap','')
	outfname = fname +"/output/dns/"+ dirdate +"/"+ filename
	print "outfilename"+outfname
	outfolder = fname +"/output/dns/"+dirdate
	dirdate= str(date.today())
	try:
	    os.mkdir(outfolder)
	    
	except Exception as e:
	    pass
	find_dns(pkts,outfname)
