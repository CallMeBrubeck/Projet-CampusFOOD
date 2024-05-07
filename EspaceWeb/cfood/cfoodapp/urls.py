from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from cfoodapp.views import *

urlpatterns = [
    path('', home, name="home"),
    path('article/recherche',search, name="search" ),
    #authentification app
    path('auth/',include("auth_app.urls")),
    path('upbapp/', include('upbapp.urls')),
    path('iuaapp/', include('iuaapp.urls')),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)