![](/images/ratatouille.jpg)
# About

Advanced Tool For Router Packet Capture and Analysis.

<h5> All the tool provided here is just for education and research purpose don't misuse it in any illegal activity.<br>Author is not responsible for any misuse by you.</h5>

<h3> Required Inputes </h3>
<ul>
	<li>User Need to input IP address of router in a file perline </li>
	<li>Country Name </li>
	<li>Ftp Server Details</li>
</ul>

# Installation and Uses:

<h4> Install bro and tshark </h4>
<ul>
	<li>sudo apt install bro</li>
	<li>sudo apt install tshark</li>
</ul>

<h4> Configure Database </h4>
<ul>
	<li>Import "capture_start.sql" in mysql</li>
	<li>Put the sql server IP and credentials in <b>config/bdconfig.ini</b></li>
</ul>
<h4> Configure FTP </h4>
<ul>
	<li>Put FTP credentials in <b>config/ftpconfig.ini</b> </li>
</ul>
<h4> Configure Router IP Input </h4>
<ul>
	<li>Put Router IP file in <b>ip-files</b> </li>
	<li>Put file name of ip in <b>config/routerconfig.ini</b> </li>
</ul>
<h4> Install the requirements </h4>
<ul>
	<li>Install Python requirements using command "<b>pip install -r requirements.txt</b>" </b> </li>
</ul>

<h4>Uses</h4>
<ul>
	<li>run using command "<b>python ratatouille.py help </b>" </li>
</ul>

<b>! Run Before Use </b>

	mkdir old_pacp output old_output pcap_downloads && cd output && mkdir credentials  dns  files  graph  urls  voip && cd .. && cd old_output && mkdir credentials  dns  files  graph  urls  voip

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
                analyse 	It will Extract Credentials, HTTP Url's, Files, VOIP Calls, Dns Requests From PCAP to output/ folder and it will make IP source and Destination Link
		
#GUI Configurations

To Configure Gui You need to run the following commands:
	
	sudo pip3 install django
	sudo python3 manage.py makemigrations
	sudo pyhton3 manage.py migrate
	sudo pyhton3 manage.py runserver
	
	with the following commands you will get the server up and running on http://0.0.0.0:8000 .



Special Thanks to [Net-Cred](https://github.com/DanMcInerney/net-creds)
