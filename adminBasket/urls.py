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

from apps.main.views import HomeView, AboutView, RegisterUser, LoginView, LogOut, HomeView

urlpatterns = [
    url(r'^$', LoginView.as_view(), name="main"),
    url(r'^salir/', LogOut.as_view()),
    url(r'^registrar/', RegisterUser.as_view(), name="reg"),
    url(r'^about/', AboutView.as_view()),
    url(r'^admin/', admin.site.urls),
    
    url(r'^main/', include('apps.main.urls')),
    url(r'^torneo/', include('apps.torneo.urls')),
    url(r'^partido/', include('apps.partido.urls')),
    url(r'^jugador/', include('apps.jugador.urls')),
    url(r'^equipo/', include('apps.equipo.urls'))
]