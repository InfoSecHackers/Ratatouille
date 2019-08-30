from django.shortcuts import render
import json

# Create your views here.
from main.models import Country, Ip, Date, File, Voip, Url, Cred, Dns

def index(request):

	country_all = Country.objects.all().count()
	date_all = Date.objects.all().count()
	ip_all = Ip.objects.all().count()
	cred_all = Cred.objects.all().count()
	file_all = File.objects.all().count()
	voip_all = Voip.objects.all().count()
	url_all = Url.objects.all().count()
	dns_all = Dns.objects.all().count()

	country_list = Country.objects.all()
	date_list = Date.objects.all()

	context = {

	'country_all':country_all,
	'date_all':date_all,
	'ip_all':ip_all,
	'cred_all':cred_all,
	'file_all':file_all,
	'voip_all':voip_all,
	'url_all':url_all,
	'country_list':country_list,
	'date_list':date_list,
	'dns_all':dns_all,

	}

	return render(request, 'index.html', context=context)

def date(request,source):

	country_list = Country.objects.all()
	date_list = Date.objects.all()
	ip_list = Ip.objects.all()
	cred_list = Cred.objects.all()
	file_list = File.objects.all()
	voip_list = Voip.objects.all()
	url_list = Url.objects.all()

	context = {

	'country_list':country_list,
	'date_list':date_list,
	'ip_list':ip_list,
	'cred_list':cred_list,
	'file_list':file_list,
	'voip_list':voip_list,
	'url_list':url_list,
	'source':source,

	}

	return render(request,'date.html',context=context)	

def ip(request,source,date):

	country_list = Country.objects.all()
	date_list = Date.objects.all()
	ip_list = Ip.objects.all()


	cred_list = Cred.objects.all()
	cred_list_ip = Cred.objects.values('ip_id').distinct()
	cred_list_country = Cred.objects.values('country_id').distinct()
	cred_list_date = Cred.objects.values('date_id').distinct()

	file_list = File.objects.all()
	file_list_ip = File.objects.values('ip_id').distinct()
	file_list_country = File.objects.values('country_id').distinct()
	file_list_date = File.objects.values('date_id').distinct()

	voip_list = Voip.objects.all()
	voip_list_ip = Voip.objects.values('ip_id').distinct()
	voip_list_country = Voip.objects.values('country_id').distinct()
	voip_list_date = Voip.objects.values('date_id').distinct()

	url_list = Url.objects.all()
	url_list_ip = Url.objects.values('ip_id').distinct()
	url_list_country = Url.objects.values('country_id').distinct()
	url_list_date = Url.objects.values('date_id').distinct()

	dns_list = Dns.objects.all()
	dns_list_ip = Dns.objects.values('ip_id').distinct()
	dns_list_country = Dns.objects.values('country_id').distinct()
	dns_list_date = Dns.objects.values('date_id').distinct()

	date = Date.objects.get(date=date)

	context = {

	'country_list':country_list,
	'date_list':date_list,
	'ip_list':ip_list,

	'cred_list':cred_list,
	'cred_list_ip':cred_list_ip,
	'cred_list_country':cred_list_country,
	'cred_list_date':cred_list_date,

	'file_list':file_list,
	'file_list_ip':file_list_ip,
	'file_list_country':file_list_country,
	'file_list_date':file_list_date,

	'voip_list':voip_list,
	'voip_list_ip':voip_list_ip,
	'voip_list_country':voip_list_country,
	'voip_list_date':voip_list_date,

	'url_list':url_list,
	'url_list_ip':url_list_ip,
	'url_list_country':url_list_country,
	'url_list_date':url_list_date,

	'dns_list':dns_list,
	'dns_list_ip':dns_list_ip,
	'dns_list_country':dns_list_country,
	'dns_list_date':dns_list_date,

	'source':source,
	'date':date,

	}

	return render(request,'ip.html',context=context)

def data (request,source,ip,date):

	country_list = Country.objects.all()
	date_list = Date.objects.all()
	ip_list = Ip.objects.all()
	cred_list = Cred.objects.all()
	file_list = File.objects.all()
	voip_list = Voip.objects.all()
	url_list = Url.objects.all()
	dns_list = Dns.objects.all()
	ip = Ip.objects.get(ip=ip)
	date = Date.objects.get(date=date)
	context = {

	'country_list':country_list,
	'date_list':date_list,
	'ip_list':ip_list,
	'cred_list':cred_list,
	'file_list':file_list,
	'voip_list':voip_list,
	'url_list':url_list,
	'dns_list':dns_list,
	'source':source,
	'ip':ip,
	'date':date,

	}

	return render(request,'data.html',context=context)

def file_viewer(request,source,ip,date,file_id):

	file = File.objects.get(id=file_id)
	file_path =File.objects.values().get(id=file_id)
	file_path = file_path.get('file_path')
	file_path = file_path.replace('output','old_output')
	file_path = file_path.replace('/media/loop/data/PCAPS/Ratatouille','')


	context = {

	'source':source,
	'ip':ip,
	'date':date,
	'file':file,
	'file_path':file_path,

	}

	return render(request,'viewer.html',context=context)

def voip_viewer(request,source,ip,date,voip_id,src):

	voip = Voip.objects.get(id=voip_id)
	voip_path =Voip.objects.values().get(id=voip_id)
	voip_path = voip_path.get('file_path')
	voip_path = voip_path.replace('output','old_output')
	voip_path = voip_path.replace('/media/loop/data/PCAPS/Ratatouille','')


	context = {

	'source':source,
	'ip':ip,
	'date':date,
	'voip':voip,
	'voip_path':voip_path,
	'src':src,

	}

	return render(request,'viewer.html',context=context)