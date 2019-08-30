from django.contrib import admin

# Register your models here.
from main.models import Country , Ip , Date , File , Voip , Url , Cred

admin.site.register(Country)
admin.site.register(Ip)
admin.site.register(Date)
admin.site.register(File)
admin.site.register(Voip)
admin.site.register(Url)
admin.site.register(Cred)