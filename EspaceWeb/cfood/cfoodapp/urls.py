from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from cfoodapp import views

urlpatterns = [
    path('', views.home, name="home"),
    path('article/recherche',views.search, name="search" ),
    #authentification app
    path('auth/',include("auth_app.urls")),
    path('upbapp/', include('upbapp.urls')),
    path('iuaapp/', include('iuaapp.urls')),
]