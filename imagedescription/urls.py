from django.urls import path

from . import views

urlpatterns = [
	path('', views.getImage),
	path('sendemail', views.contact)
]