import imp
from django.shortcuts import render

from Booking.models import Appointment

from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from Authentication.models import User

# Create your views here.
@login_required(login_url='/authentication/login/')
def show_booking(request):
    if request.user.get_role() == 1:
        context = {
            "username": request.user,
            "listDokter": User.objects.filter(role=2),
        }
        return render(request, "booking.html", context)
    else:
        context = {
            "username": request.user,
            "appointmentList": Appointment.objects.filter(doctor="request.user")
        }
        return render(request, "doctor.html", context)

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

def get_dokter_json(request):
    dokter = request.GET.get('search')
    list_dokter = Appointment.objects.filter(doctor__icontains=dokter)
    return HttpResponse(serializers.serialize('json', list_dokter)) 