from django.urls import path
from . import views

urlpatterns = [

    		path('', views.index, name='index'),
    		path('<source>/', views.date, name='date'),
    		path('<source>/<date>/ip', views.ip, name='ip'),
    		path('<source>/<date>/<ip>/data/', views.data, name='data'),
    		path('<source>/<date>/<ip>/<file_id>', views.file_viewer, name='file_viewer'),
    		path('<source>/<date>/<ip>/<voip_id>/<src>', views.voip_viewer, name='voip_viewer'),
]  

