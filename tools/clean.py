import os

def clean():
	

	os.system("sudo rsync -av pcap_downloads/ old_pacp/")
	os.system("sudo rm -R pcap_downloads/*")
	print "All files moved to old_pacp download folder is clean now"