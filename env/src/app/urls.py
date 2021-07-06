from django.urls import path

from .views import (
    home,
    hostusage,
    instances,
    networks,
    network,
    storages,
    storage,
    accesPage,
    logOut

)

app_name='app'
urlpatterns = [
    path('home',home,name='home'),
    path('',home,name='home'),
    path('vmachines',instances,name='vmachines'),
    path("hostusage", hostusage.as_view(), name="hostusage"),
    path("networks", networks, name="networks"),
    path("network/<str:pool>", network, name="network"),
    path("storages", storages, name="storages"),
    path("storage/<str:pool>", storage, name="storage"),
  
    path('acces/',accesPage,name="acces"),
    path('quitter/',logOut,name="quitter"),
]