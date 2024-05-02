from django.urls import path, include
from iuaapp.views import *

urlpatterns = [
    #=======================UPB_page===================
    path('', iua_page, name="iuaHome"),

    #=======================EndUPB_page===================
]
