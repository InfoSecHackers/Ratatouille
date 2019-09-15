import re,fileinput,os,sys
import sqlite3
from django.shortcuts import render
from main import setup
setup.setup()
from main.models import Country,Ip,Date,Cred,File,Voip,Url,Dns,Graph
base = os.getcwd()

def cred():

		path=os.getcwd()+"/output/credentials/"
		os.chdir(path)
		osw= os.walk(path)



		for path, dirs, files in os.walk(path):
			try:

				for filename in files:
					columns = filename.partition('-')
					ip = columns[0]
					country = columns[2]
					date = os.path.basename(path)
					fullpath = os.path.join(path, filename)
					f = open(fullpath,'r',encoding="utf8", errors='ignore')
					creds = f.readlines()
					#To Store Country
					##print (((Country.objects.filter(country_name=country).values('id'))[0]).get('id'))
					if Country.objects.filter(country_name=country).distinct().values():
						print ("Country Availiable ")
					else:
						print ("Inserting Country: "+country)
						c=Country()
						c.country_name = country
						c.save()
					#To Save Date
					if Date.objects.filter(date=date).values('id'):
						print ("Date Availiable")
					else:
						print ("Inserting Date: "+date)
						d = Date()
						d.date = date
						d.save()

					#To save Ip
					if Ip.objects.filter(ip=ip).values('id'):

						print ("Ip Availiable")
					else:
						print ("Inserting Ip: "+ip)
						i = Ip()
						i.ip = ip
						i.country_id = ((Country.objects.filter(country_name=country).values('id'))[0]).get('id')
						i.save() 

					for cred in creds:

						k = Cred()
						k.cred = cred
						k.country_id = ((Country.objects.filter(country_name=country).values('id'))[0]).get('id')
						k.date_id = ((Date.objects.filter(date=date).values('id'))[0]).get('id')
						k.ip_id = ((Ip.objects.filter(ip=ip).values('id'))[0]).get('id')
						k.save()

			except Exception as e:
				print (e)
				pass
		os.chdir(base)

def files():

		path=os.getcwd()+"/output/files/"
		os.chdir(path)
		osw= os.walk(path)



		for path, dirs, files in os.walk(path):
			try:

				for filename in files:
					columns = os.path.basename(path).partition('-')
					ip = columns[0]
					country = columns[2]
					date = os.path.basename(os.path.dirname(os.path.abspath(path)))
					fullpath = os.path.join(path, filename)
					f = open(fullpath,'r',encoding="utf8", errors='ignore')
					files = f.read()
					#To Store Country

					if Country.objects.filter(country_name=country).distinct().values():
						print ("Country Availiable ")
					else:
						print ("Inserting Country: "+country)
						c=Country()
						c.country_name = country
						c.save()
					#To Save Date
					if Date.objects.filter(date=date).values('id'):
						print ("Date Availiable")
					else:
						print ("Inserting Date: "+date)
						d = Date()
						d.date = date
						d.save()

					#To save Ip
					if Ip.objects.filter(ip=ip).values('id'):

						print ("Ip Availiable")
					else:
						print ("Inserting Ip: "+ip)
						i = Ip()
						i.ip = ip
						i.country_id = ((Country.objects.filter(country_name=country).values('id'))[0]).get('id')
						i.save() 

					k = File()
					k.file_name = filename
					k.file_path = path
					k.country_id = ((Country.objects.filter(country_name=country).values('id'))[0]).get('id')
					k.date_id = ((Date.objects.filter(date=date).values('id'))[0]).get('id')
					k.ip_id = ((Ip.objects.filter(ip=ip).values('id'))[0]).get('id')
					k.save()


			except Exception as e:
				print (e)
				pass
		os.chdir(base)

def urls():

		path=os.getcwd()+"/output/urls/"
		os.chdir(path)
		osw= os.walk(path)



		for path, dirs, files in os.walk(path):
			try:

				for filename in files:
					columns = filename.partition('-')
					ip = columns[0]
					country = columns[2]
					date = os.path.basename(path)
					fullpath = os.path.join(path, filename)
					f = open(fullpath,'r',encoding="utf8", errors='ignore')
					urls = f.readlines()
					#To Store Country

					if Country.objects.filter(country_name=country).distinct().values():
						print ("Country Availiable ")
					else:
						print ("Inserting Country: "+country)
						c=Country()
						c.country_name = country
						c.save()
					#To Save Date
					if Date.objects.filter(date=date).values('id'):
						print ("Date Availiable")
					else:
						print ("Inserting Date: "+date)
						d = Date()
						d.date = date
						d.save()

					#To save Ip
					if Ip.objects.filter(ip=ip).values('id'):

						print ("Ip Availiable")
					else:
						print ("Inserting Ip: "+ip)
						i = Ip()
						i.ip = ip
						i.country_id = ((Country.objects.filter(country_name=country).values('id'))[0]).get('id')
						i.save() 

					
					for url in urls:
						
						k = Url()
						k.url = url
						k.country_id = ((Country.objects.filter(country_name=country).values('id'))[0]).get('id')
						k.date_id = ((Date.objects.filter(date=date).values('id'))[0]).get('id')
						k.ip_id = ((Ip.objects.filter(ip=ip).values('id'))[0]).get('id')
						k.save()


			except Exception as e:
				print (e)
				pass
		os.chdir(base)

def voip():

		path=os.getcwd()+"/output/voip/"
		os.chdir(path)
		osw= os.walk(path)



		for path, dirs, files in os.walk(path):
			try:

				for filename in files:
					columns = filename.partition('-')
					ip = columns[0]
					country = columns[2]
					date = os.path.basename(path)
					fullpath = os.path.join(path, filename)
					f = open(fullpath,'r',encoding="utf8", errors='ignore')
					voip = f.read()
					#To Store Country

					if Country.objects.filter(country_name=country).distinct().values():
						print ("Country Availiable ")
					else:
						print ("Inserting Country: "+country)
						c=Country()
						c.country_name = country
						c.save()
					#To Save Date
					if Date.objects.filter(date=date).values('id'):
						print ("Date Availiable")
					else:
						print ("Inserting Date: "+date)
						d = Date()
						d.date = date
						d.save()

					#To save Ip
					if Ip.objects.filter(ip=ip).values('id'):

						print ("Ip Availiable")
					else:
						print ("Inserting Ip: "+ip)
						i = Ip()
						i.ip = ip
						i.country_id = ((Country.objects.filter(country_name=country).values('id'))[0]).get('id')
						i.save() 

					k = Voip()
					k.file_name = filename
					k.file_path = path
					k.country_id = ((Country.objects.filter(country_name=country).values('id'))[0]).get('id')
					k.date_id = ((Date.objects.filter(date=date).values('id'))[0]).get('id')
					k.ip_id = ((Ip.objects.filter(ip=ip).values('id'))[0]).get('id')
					k.save()

			except Exception as e:
				print (e)
				pass
		os.chdir(base)

def dns():

		path=os.getcwd()+"/output/dns/"
		os.chdir(path)
		osw= os.walk(path)



		for path, dirs, files in os.walk(path):
			try:

				for filename in files:
					columns = filename.partition('-')
					ip = columns[0]
					country = columns[2]
					date = os.path.basename(path)
					fullpath = os.path.join(path, filename)
					f = open(fullpath,'r',encoding="utf8", errors='ignore')
					dnss = f.readlines()
					#To Store Country

					if Country.objects.filter(country_name=country).distinct().values():
						print ("Country Availiable ")
					else:
						print ("Inserting Country: "+country)
						c=Country()
						c.country_name = country
						c.save()
					#To Save Date
					if Date.objects.filter(date=date).values('id'):
						print ("Date Availiable")
					else:
						print ("Inserting Date: "+date)
						d = Date()
						d.date = date
						d.save()

					#To save Ip
					if Ip.objects.filter(ip=ip).values('id'):

						print ("Ip Availiable")
					else:
						print ("Inserting Ip: "+ip)
						i = Ip()
						i.ip = ip
						i.country_id = ((Country.objects.filter(country_name=country).values('id'))[0]).get('id')
						i.save() 

					
					for dns in dnss:
						
						k = Dns()
						k.dns = dns
						k.country_id = ((Country.objects.filter(country_name=country).values('id'))[0]).get('id')
						k.date_id = ((Date.objects.filter(date=date).values('id'))[0]).get('id')
						k.ip_id = ((Ip.objects.filter(ip=ip).values('id'))[0]).get('id')
						k.save()


			except Exception as e:
				print (e)
				pass
		os.chdir(base)

def graph():

		path=os.getcwd()+"/output/graph/"
		os.chdir(path)
		osw= os.walk(path)



		for path, dirs, files in os.walk(path):
			try:

				for filename in files:
					columns = filename.partition('-')
					ip = columns[0]
					country = columns[2]
					date = os.path.basename(path)
					fullpath = os.path.join(path, filename)
					filename = filename.strip()
					#f = open(fullpath,'r',encoding="utf8", errors='ignore')
					#files = f.read()
					#To Store Country

					if Country.objects.filter(country_name=country).distinct().values():
						print ("Country Availiable ")
					else:
						print ("Inserting Country: "+country)
						c=Country()
						c.country_name = country
						c.save()
					#To Save Date
					if Date.objects.filter(date=date).values('id'):
						print ("Date Availiable")
					else:
						print ("Inserting Date: "+date)
						d = Date()
						d.date = date
						d.save()

					#To save Ip
					if Ip.objects.filter(ip=ip).values('id'):

						print ("Ip Availiable")
					else:
						print ("Inserting Ip: "+ip)
						i = Ip()
						i.ip = ip
						i.country_id = ((Country.objects.filter(country_name=country).values('id'))[0]).get('id')
						i.save() 

					k = Graph()
					k.file_name = filename
					k.file_path = path
					k.country_id = ((Country.objects.filter(country_name=country).values('id'))[0]).get('id')
					k.date_id = ((Date.objects.filter(date=date).values('id'))[0]).get('id')
					k.ip_id = ((Ip.objects.filter(ip=ip).values('id'))[0]).get('id')
					k.save()


			except Exception as e:
				print (e)
				pass
		os.chdir(base)
if __name__ == '__main__':
	
	cred();files();urls();dns();voip();graph()
	os.system("sudo find output/files/* -type d -maxdepth 1 -print0 | sudo xargs -0 mv  {} -t  `pwd`/old_output/files/")
	os.system("sudo find output/credentials/* -type d -maxdepth 1 -print0 | sudo xargs -0 mv  {} -t  `pwd`/old_output/credentials/")
	os.system("sudo find output/urls/* -type d -maxdepth 1 -print0 | sudo xargs -0 mv  {} -t  `pwd`/old_output/urls/")
	os.system("sudo find output/voip/* -type d -maxdepth 1 -print0 | sudo xargs -0 mv  {} -t  `pwd`/old_output/voip/")
	os.system("sudo find output/dns/* -type d -maxdepth 1 -print0 | sudo xargs -0 mv  {} -t  `pwd`/old_output/dns/")
	os.system("sudo find output/graph/* -type d -maxdepth 1 -print0 | sudo xargs -0 mv  {} -t  `pwd`/old_output/graph/")