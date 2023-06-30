from django.urls import path
from . import views

urlpatterns = [
    path('base',views.base,name='base'),
    path('allskills',views.allskills,name='allskills'),
    path('allprojects',views.allprojects,name='allprojects'),
    path('home',views.home,name='home'),
]
