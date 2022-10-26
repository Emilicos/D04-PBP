from django.urls import path
from Booking.views import add_booking, delete_booking, show_booking, show_json

app_name = 'Booking'

urlpatterns = [
    path('', show_booking, name='show_booking'),
    path('json/', show_json, name='show_json'),
    path('add/', add_booking, name='add_booking'),
    path('delete/<int:id>/', delete_booking, name='delete_booking'),
]