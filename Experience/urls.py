from django.urls import path
from Experience.views import create_experience_ajax, show_experience, show_experience_detail, show_experience_json,add_experience_flutter

app_name = "Experience"

urlpatterns = [
    path('', show_experience, name='show_experience'),
    path('create-experience/', create_experience_ajax, name='create_experience_ajax'),
    path('experience-detail/<int:id>/', show_experience_detail, name='show_experience_detail'),
    path('json/', show_experience_json, name='show_experience_json'),
    path('add-experience-flutter', add_experience_flutter, name='add_experience_flutter')
]