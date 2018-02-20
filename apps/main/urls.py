from django.conf.urls import url
from .views import RequirLoginView, HomeView, RegisterUser


urlpatterns = [
	url(r'^registrar$', RegisterUser.as_view(), name="register"),
	url(r'^requerimientos$', RequirLoginView.as_view()),
]