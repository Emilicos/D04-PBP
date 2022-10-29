from django.urls import path
from Blogpost.views import create_blogpost, delete_blogpost, show_blogpost, show_blogpost_by_id, show_blogpost_json, show_blogpost_json_by_id, update_blogpost
app_name = "Blogpost"

urlpatterns = [
    path("", show_blogpost, name = "show_blogpost"),
    path("create/", create_blogpost, name = "create_blogpost"),
    path("<int:id>/", show_blogpost_by_id, name = "show_blogpost_by_id"),
    path("json/", show_blogpost_json, name = "show_blogpost_json"),
    path("json/<int:id>/", show_blogpost_json_by_id, name = "show_blogpost_json_by_id"),
    path("update/<int:id>/", update_blogpost, name = "update_blogpost"),
    path("delete/<int:id>/", delete_blogpost, name = "delete_blogpost"),
]