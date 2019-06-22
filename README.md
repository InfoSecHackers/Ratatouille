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
	<li>run using command "<b>python ratatouille.py </b>" </li>
</ul>

Arguments:
		
		getrouter   Get username password of router
		getint      Get Active Interface of Router
		start       Start PacketCapture On Router
		stop        Stop PacketCapture On Router
		export      Export Captured Packets To FTP SERVER
		download    Download PCAPS From FTP
		
We are working on Analysis part of tool soon we will release.
