from django.conf.urls import url
from .views import RequirLoginView, HomeView, RegisterUser, NuestraMisionView
from django.urls import path

urlpatterns = [
	path('registrar/', RegisterUser.as_view(), name="register"),
	path('requerimientos/', RequirLoginView.as_view()),
	path('mision/', NuestraMisionView.as_view()),
]
