from django.urls import path
from . import views

urlpatterns = [

    		path('', views.index, name='index'),
    		path('<source>/', views.date, name='date'),
    		path('<source>/<date>/ip', views.ip, name='ip'),
    		path('<source>/<date>/<ip>/data/', views.data, name='data'),
    		#path('authors/', views.AuthorListView.as_view(), name='authors'),
    		#path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
]  
