from django.contrib import admin
from django.urls import path

from .views import index, index_map
from .views import tdslist, listdetail
from .views import type
from .views import menu


urlpatterns = [
    path('', index, name='index'),
    #path('index/', index, name='index'),
    path('list/', tdslist, name='list'),
    path('list/detail/', listdetail, name='list-detail'),
    path('index_map/', index_map, name='index_map'),
    path('type/', type, name='select-type'),
    path('type/list/', tdslist, name='list_1'),
    path('type/list/detail/', listdetail, name='list-detail'),
    path('menu/', menu, name='menu'), 
]
