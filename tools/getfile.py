import re,fileinput,os,sys

def getfile():

	path=os.getcwd()+"/pcap_downloads/"
	os.chdir(path)
	osw= os.walk(path)
	
	for path, dirs, files in os.walk(path):
		try:
			for filename in files:
					fullpath = os.path.join(path, filename)
					filename = os.path.splitext(filename)[0]
					os.system("sudo bro -Cr %s   ../file/plugins/extract-all-files.bro  " %fullpath)
					os.system("sudo mkdir -p ../output/files/`date +%F`/"+filename)
					os.system("sudo find ../output/files/ -maxdepth 1 -type f -print0 | sudo xargs -0 mv {} -t  ../output/files/`date +%F`/"+filename)
					os.system("sudo rm ../pcap_downloads/*.log && sudo rm -r ../pcap_downloads/extract_files && sudo rm -r .state ")
	
		except Exception as e:
			os.system("sudo rm ../pcap_downloads/*.log && sudo rm -r ../pcap_downloads/extract_files && sudo rm -r state ")
			#print e
			pass
	print "Files Extracted to output/files/current_date/filename"
	os.system("sudo rm ../pcap_downloads/*.log && sudo rm -r ../pcap_downloads/extract_files")
	os.system("sudo rm -r ../pcap_downloads/.state && sudo rm -r ../output/files/`date +%F`/state ")


