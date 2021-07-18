from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [

    path("",views.host,name='host'),
    path('',views.offer,name='offer')

]