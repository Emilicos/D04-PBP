from django.urls import path
from HIVCenter.views import show_homepage

app_name = "homepage"

urlpatterns = [
    path("", show_homepage, name = "show_homepage")
]