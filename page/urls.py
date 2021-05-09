from . import views
from django.urls import path

urlpatterns = [
    #path('home', views.home),
    #path('', views.index, name='homepage'),
    path('', views.index, {'pagename': ''}, name = 'home'),
    path('<str:pagename>', views.index, name='index'),
]