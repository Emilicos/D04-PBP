from django.urls import path
from Booking.views import add_booking, add_booking_flutter, delete_booking, get_dokter_json, list_nama_dokter, show_booking, show_json, show_json_flutter

app_name = 'Booking'

urlpatterns = [
    path('', show_booking, name='show_booking'),
    path('json/', show_json, name='show_json'),
    path('add/', add_booking, name='add_booking'),
    path('delete/<int:id>/', delete_booking, name='delete_booking'),
    path('all/', get_dokter_json, name="get_dokter_json"),
    path('nama_dokter/', list_nama_dokter, name="list_nama_dokter"),
    
]