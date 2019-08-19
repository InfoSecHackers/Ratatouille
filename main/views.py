from django.shortcuts import render

# Create your views here.
from main.models import Country, Ip, Date, File, Voip, Url, Cred

def index(request):

	country_all = Country.objects.all().count()
	date_all = Date.objects.all().count()
	ip_all = Ip.objects.all().count()
	cred_all = Cred.objects.all().count()
	file_all = File.objects.all().count()
	voip_all = Voip.objects.all().count()
	url_all = Url.objects.all().count()

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
	file_list = File.objects.all()
	voip_list = Voip.objects.all()
	url_list = Url.objects.all()
	date = Date.objects.get(date=date)

	context = {

	'country_list':country_list,
	'date_list':date_list,
	'ip_list':ip_list,
	'cred_list':cred_list,
	'file_list':file_list,
	'voip_list':voip_list,
	'url_list':url_list,
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
	'source':source,
	'ip':ip,
	'date':date,

	}

	return render(request,'data.html',context=context)
