from django.contrib import admin
from django.urls import path
from . import views
from user.views import product_create_view


urlpatterns = [
    path('', views.home, name="roster-home"),
    path('about/', views.about, name="roster-about"),
    path('test/', views.testView, name="roster-test"),
    path('management/', views.management, name="management"),
    path('notifications/', views.notifications, name="notifications"),
    path('create/', product_create_view),

    
]
