import re,fileinput,os,sys

path=os.getcwd()+"/pcap_downloads/"
print os.getcwd()
os.chdir(path)
osw= os.walk(path)

for path, dirs, files in os.walk(path):
    for filename in files:
        fullpath = os.path.join(path, filename)
        os.system("sudo bro -Cr %s   ../file/plugins/extract-all-files.bro  " %fullpath)
try:
    os.system("mkdir ../output/files/`date +%F`")
    os.system("find ../output/files/ -maxdepth 1 -type f -print0 | xargs -0 mv -t ../output/files/`date +%F`  ")
    os.system("rm ../pcap_downloads/*.log && rm -r ../pcap_downloads/extract_files  ")
    print "Files Extracted to output/files/current_date"
except Exception:
    pass
