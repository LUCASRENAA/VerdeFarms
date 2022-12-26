from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_user),
    path("registro", views.registro),
    path("submit", views.submit_login),
    path("submit/registro", views.submit_registro),

]
