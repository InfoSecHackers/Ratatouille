import os
import sys
import json
from multiprocessing.dummy import Pool as ThreadPool
import db
import time

def getinterface(url,ip,username,password):
    allinterface = os.popen("curl -s -u %s:%s http://%s/ios_web_exec/commandset --data $'\041 COMMANDSET VERSION=\"1.0\"\n\041 OPTIONS BEGIN\n\041 MODE=\"0\"\n\041 OPTIONS END\nshow ip int brief\n\041 END\n\041 COMMANDSET END'  | grep -v ! | grep -v ERROR"%(str(username),str(password),url.strip())).read()
    interface = os.popen("curl -s -u %s:%s http://%s/ios_web_exec/commandset --data $'\041 COMMANDSET VERSION=\"1.0\"\n\041 OPTIONS BEGIN\n\041 MODE=\"0\"\n\041 OPTIONS END\nshow ip int brief\n\041 END\n\041 COMMANDSET END' | grep %s | grep -E '^(Fa|Gi)' | awk '{print$1}'"%(str(username),str(password),url.strip(),str(ip))).read()
    db.kursor.execute("UPDATE `capture_start` SET interface = '%s', allinterface = '%s' where ip='%s'" % (str(interface), str(allinterface), str(ip)))
    db.mydb.commit()
    print "Getting Interface for: "+ip

def start(url,ip,username,password,interface):
    print "\n###### Configuring Permissions ########\n"
    os.system("curl -s -u %s:%s http://%s/ios_web_exec/commandset --data $'\041 COMMANDSET VERSION=\"1.0\"\n\041 OPTIONS BEGIN\n\041 MODE=\"1\"END\nip access-list extended cap\n\041 END\n\041 COMMANDSET END'"%(str(username),str(password),url.strip()))
    os.system("curl -s -u %s:%s http://%s/ios_web_exec/commandset --data $'\041 COMMANDSET VERSION=\"1.0\"\n\041\041 OPTIONS BEGIN\n\041 MODE=\"1\"\n\041 OPTIONS END\naccess-list 101 permit ip any any\n\041 END\n\041 COMMANDSET END'"%(str(username),str(password),url.strip()))
    print "\n###### Creating Buffer ########\n"
    os.system("curl -s -u %s:%s http://%s/ios_web_exec/commandset --data $'\041 COMMANDSET VERSION=\"1.0\"\n\041 OPTIONS BEGIN\n\041 MODE=\"0\"\n\041 OPTIONS END\nmonitor capture buffer buff circular\n\041 END\n\041 COMMANDSET END'"%(str(username),str(password),url.strip()))
    os.system("curl -s -u %s:%s http://%s/ios_web_exec/commandset --data $'\041 COMMANDSET VERSION=\"1.0\"\n\041 OPTIONS BEGIN\n\041 MODE=\"0\"\n\041 OPTIONS END\nmonitor capture buffer buff filter access-list cap\n\041 END\n\041 COMMANDSET END'"%(str(username),str(password),url.strip()))
    print "\n###### Setting Interface for Capturing ########\n"
    os.system("curl -s -u %s:%s http://%s/ios_web_exec/commandset --data $'\041 COMMANDSET VERSION=\"1.0\"\n\041 OPTIONS BEGIN\n\041 MODE=\"0\"\n\041 OPTIONS END\nmonitor capture point ip cef trace %s both\n\041 END\n\041 COMMANDSET END'"%(str(username),str(password),url.strip(),str(interface).strip()))
    print "\n###### Setting Buffer Size ########\n"
    os.system("curl -s -u %s:%s http://%s/ios_web_exec/commandset --data $'\041 COMMANDSET VERSION=\"1.0\"\n\041 OPTIONS BEGIN\n\041 MODE=\"0\"\n\041 OPTIONS END\nmonitor cap point associate trace buff1\n\041 END\n\041 COMMANDSET END'"%(str(username),str(password),url.strip()))
    os.system("curl -s -u %s:%s http://%s/ios_web_exec/commandset --data $'\041 COMMANDSET VERSION=\"1.0\"\n\041 OPTIONS BEGIN\n\041 MODE=\"0\"\n\041 OPTIONS END\nmonitor capture buffer buff size 50000\n\041 END\n\041 COMMANDSET END'"%(str(username),str(password),url.strip()))
    os.system("curl -s -u %s:%s http://%s/ios_web_exec/commandset --data $'\041 COMMANDSET VERSION=\"1.0\"\n\041 OPTIONS BEGIN\n\041 MODE=\"0\"\n\041 OPTIONS END\nmonitor capture buffer buff max-size 5000\n\041 END\n\041 COMMANDSET END'"%(str(username),str(password),url.strip()))
    print "\n###### Started Capturing ########\n"
    os.system("curl -s -u %s:%s http://%s/ios_web_exec/commandset --data $'\041 COMMANDSET VERSION=\"1.0\"\n\041 OPTIONS BEGIN\n\041 MODE=\"0\"\n\041 OPTIONS END\nmonitor capture point start trace\n\041 END\n\041 COMMANDSET END'"%(str(username),str(password),url.strip()))
    db.kursor.execute("UPDATE `capture_start` SET status = 'Running' WHERE ip='%s'" % (str(ip)))
    db.mydb.commit()



def stop(url,ip,username,password):
    print "\n###### Stopped Capturing ########\n"
    os.system("curl -s -u %s:%s http://%s/ios_web_exec/commandset --data $'\041 COMMANDSET VERSION=\"1.0\"\n\041 OPTIONS BEGIN\n\041 MODE=\"0\"\n\041 OPTIONS END\nmonitor capture point stop trace\n\041 END\n\041 COMMANDSET END'"%(str(username),str(password),url.strip()))
    print "\n###### Clearing Buffer ########\n"
    os.system("curl -s -u %s:%s http://%s/ios_web_exec/commandset --data $'\041 COMMANDSET VERSION=\"1.0\"\n\041 OPTIONS BEGIN\n\041 MODE=\"0\"\n\041 OPTIONS END\nmonitor capture buffer buff clear\n\041 END\n\041 COMMANDSET END'"%(str(username),str(password),url.strip()))
    db.kursor.execute("UPDATE `capture_start` SET status = 'Stop' WHERE ip='%s'" % (str(ip)))
    db.mydb.commit()




def export(url,ip,username,password,interface,country):
        print "\n###### Stopped Capturing ########\n"
        os.system("curl -s -u %s:%s http://%s/ios_web_exec/commandset --data $'\041 COMMANDSET VERSION=\"1.0\"\n\041 OPTIONS BEGIN\n\041 MODE=\"0\"\n\041 OPTIONS END\nmonitor capture point stop trace\n\041 END\n\041 COMMANDSET END'"%(str(username),str(password),url.strip()))
        print "\n###### Exporting PCAPS to FTP Server ########\n"
        os.system("curl -s -u %s:%s http://%s/ios_web_exec/commandset --data $'\041 COMMANDSET VERSION=\"1.0\"\n\041 OPTIONS BEGIN\n\041 MODE=\"0\"\n\041 OPTIONS END\nmonitor capture buffer buff export ftp://admin:asdf@123qwe@212.7.217.133/%s-%s.pcap\n\041 END\n\041 COMMANDSET END'"%(str(username),str(password),url.strip(),str(ip),str(country)))
        print "\n###### Resuming Capturing ########\n"
        start(url,ip,username,password,interface)      





    


if __name__ == '__main__':
    try:
        choice= sys.argv[1]
    except IndexError:
        print "\nFor USAGE Run: python %s -h\n"%sys.argv[0]
        sys.exit(1)
    
    if choice == '-h':
        print "\n\nAvailable Methods\n\n"
        print "1. getinterface\t\tfor grepping interface\n2. start\t\tfor starting capturing\n3. export\t\tfor exporting PCAPS to server\n4. stop\t\t\tfor stopping capturing\n\nExample-1: python %s getinterface\nExample-2: python %s start"%(sys.argv[0],sys.argv[0])

    if choice.lower() == 'getinterface':
        db.kursor.execute("SELECT ip,port,username,password FROM `capture_start` WHERE allinterface IS NULL OR interface =''")
        plist = db.kursor.fetchall()
        for i in plist:
            url=i[0]+':'+i[1]
            getinterface(url,i[0],i[2],i[3])

    if choice.lower() == 'start':
        db.kursor.execute("SELECT ip,port,username,password,interface FROM `capture_start` WHERE interface IS NOT NULL AND status is NULL ")
        #db.kursor.execute("SELECT ip,port,username,password,interface FROM `capture_start` WHERE country = 'SA'")
        plist = db.kursor.fetchall()
        for i in plist:
            url=i[0]+':'+i[1]
            print url+'\n'
            start(url,i[0],i[2],i[3],i[4])
    if choice.lower() == 'export':
        db.kursor.execute("SELECT ip,port,username,password,interface,country FROM `capture_start` WHERE status = 'Running'")
        plist = db.kursor.fetchall()
        for i in plist:
            url=i[0]+':'+i[1]
            export(url,i[0],i[2],i[3],i[4],i[5])
    if choice.lower() == 'stop':
        db.kursor.execute("SELECT ip,port,username,password FROM `capture_start` WHERE status = 'Running'")
        plist = db.kursor.fetchall()
        for i in plist:
            url=i[0]+':'+i[1]
            stop(url,i[0],i[2],i[3])


    exit(0)

