from argparse import Namespace
from django.urls import path,include
from HIVCenter.views import show_homepage

app_name = "HIVCenter"

urlpatterns = [
    path("", show_homepage, name = "show_homepage"),
    # path("experience/", include("Experience.urls" , namespace="Experience")),
]