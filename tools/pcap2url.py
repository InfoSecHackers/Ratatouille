#!/usr/bin/env python
#
# pcap2url v0.2 (on 19 Feb 2017)
# Any issue/suggestion, please email to m[d0t]khairulazam[@]gmail[d0t]com

import sys,os,re,string
from scapy.all import *
from scapy.layers import http
from datetime import date

try:
    import scapy.all as scapy
except ImportError:
    import scapy

f = open(sys.argv[1], "rb")
packets = scapy.rdpcap(f)
dirdate= str(date.today())
fname = os.path.split(os.getcwd())[0]
filename = os.path.basename(sys.argv[1])
filename = filename.replace('.pcap','')
outfname = fname +"/output/urls/"+ dirdate +"/"+ filename
print "outfilename"+outfname
outfolder = fname +"/output/urls/"+dirdate
dirdate= str(date.today())
try:
    os.mkdir(outfolder)
    
except Exception as e:
    #print e
    pass
    
for p in packets:
    if p.haslayer("HTTPRequest"):
        ip_layer = p.getlayer('IP')
        http_layer = p.getlayer('HTTPRequest')
        req = '\n{0[src]} just requested a {1[Method]} {1[Host]}{1[Path]}'.format(ip_layer.fields, http_layer.fields)+'\n'
        o = open(outfname, "a")
        o.write(req)
        o.close()
    if p.haslayer("HTTPResponse"):
        http_response = p.getlayer('HTTPResponse')
        res = 'Response code {0[Status-Line]}'.format(http_response.fields)+'\n\n'
        o = open(outfname, "a")
        o.write(res)
        o.close()

print '\n'+filename+"  \nDone. End of pcap"


