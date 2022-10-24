from django.urls import path
from Experience.views import show_experience, create_experience, show_experience_detail, show_experience_json

app_name = "Experience"

urlpatterns = [
    path('', show_experience, name='show_experience'),
    path('experience-form/', create_experience, name='create_experience'),
    path('experience-detail/<int:id>/', show_experience_detail, name='show_experience_detail'),
    path('json/', show_experience_json, name='show_experience_json'),
]