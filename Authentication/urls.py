from django.contrib import admin
from django.urls import path, include
from Authentication import views

app_name = "Authentication"

urlpatterns = [
    path('', views.chooseRegisterAs, name="chooseregisteras"),
    path('registerpasien/', views.registerPasien, name="registerpasien"),
    path('registerdokter/', views.registerDokter, name="registerdokter"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path("showjson/", views.show_json, name="show_json"),
]