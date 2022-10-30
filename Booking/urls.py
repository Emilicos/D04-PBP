from django.urls import path
from Booking.views import add_booking, create_booking, delete_booking, forms_ajax, get_dokter_json, show_booking, show_json

app_name = 'Booking'

urlpatterns = [
    path('', create_booking, name='create_booking'),
    path('json/', show_json, name='show_json'),
    path('add/', add_booking, name='add_booking'),
    path('delete/<int:id>/', delete_booking, name='delete_booking'),
    path('all/', get_dokter_json, name="get_dokter_json"),
    path('forms-ajax/', forms_ajax, name='forms_ajax')
]