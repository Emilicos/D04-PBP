from django.shortcuts import render

from Booking.models import Appointment

from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def show_booking(request):
    context = {
        "username": request.user,
        "daftar_dokter": Dokter.objects.all()
    }
    return render(request, "booking.html", context)

def show_json(request):
    data = Appointment.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def add_booking(request):
    if request.method == "POST":
        user = request.user
        doctor = request.POST.get('doctor')
        date = request.POST.get('date')
        time = request.POST.get('time')
        booking = Appointment(user=user, doctor=doctor, date=date, time=time)
        booking.save()
        return JsonResponse({ "Message": "Appointment Successfully Booked" }, status=200)

@csrf_exempt
def delete_booking(request, id):
    booking = Appointment.objects.get(user=request.user, id=id)
    booking.delete()
    return JsonResponse({ "Message": "Appointment Cancelled" }, status=200)

