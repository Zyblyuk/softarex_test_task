from django.urls import path

from . import views

urlpatterns = [
    path('register', views.register_request, name="register"),
    path('', views.home, name='home'),
    path('history', views.history, name='history'),
 ]
