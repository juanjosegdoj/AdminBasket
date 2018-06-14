"""adminBasket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

from apps.main.views import HomeView, AboutView, RegisterUser, LoginView, LogOut, HomeView

urlpatterns = [
    path('', LoginView.as_view(), name="main"),
    path('salir/', LogOut.as_view()),
    path('registrar/', RegisterUser.as_view(), name="reg"),
    path('about/', AboutView.as_view(), name = 'cut'),
    path('admin/', admin.site.urls, name= 'admin'),
    path('main/', include('apps.main.urls')),
    path('equipo/', include('apps.equipo.urls')),
    path('torneo/', include('apps.torneo.urls')),
    path('partido/', include('apps.partido.urls')),
    path('jugador/', include('apps.jugador.urls')),
]
