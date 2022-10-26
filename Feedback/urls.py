from django.urls import path

from Feedback.views import create_feedback, show_feedback, show_feedback_json

app_name = "feedback"
urlpatterns = [
    path("", show_feedback, name = "show_feedback"),
    path("create/", create_feedback, name = "create_feedback"),
    path("json/", show_feedback_json, name = "show_feedback_json"),
]