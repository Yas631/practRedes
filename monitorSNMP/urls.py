from django.conf.urls import include, url
from  django.urls import path
from . import views

urlpatterns = [
    path('devices/', views.devices_list),
    path('devices/<int:device_id>/', views.device_watcher),
    path('addDevice/', views.add_device)
]
