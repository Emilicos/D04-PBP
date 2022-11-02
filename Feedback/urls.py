from django.urls import path
from Feedback.views import create_feedback
from Feedback.views import show_feedback
from Feedback.views import show_feedback_json
from Feedback.views import delete

app_name = "feedback"
urlpatterns = [
    path('', show_feedback, name = 'show_feedback'),
    path('create/', create_feedback, name = 'create_feedback'),
    path('json/', show_feedback_json, name = 'show_feedback_json'),
    path('delete/<int:pk>/', delete, name='delete'),
]