
from django.forms import model_to_dict
from django.shortcuts import redirect, render
from Booking.forms import AppointmentForm

from Booking.models import Appointment

from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from Authentication.models import User

# Create your views here.

# apus ni func kl g perlu
@login_required(login_url='/authentication/login/')
def show_booking(request):

    if request.user.role == 1:

        list_dokter = User.objects.filter(role = 1)

        lst = []

        for i in range (len(list_dokter)):
            lst.append(model_to_dict(list_dokter[i]).get("username"))
        
        print(lst)

        context = {
            "form": AppointmentForm(),
            "username": request.user,
            "listDokter": lst
        }
        
        return render(request, "booking.html", context)

    else:
        
        context = {
            "username": request.user,
            "appointmentList": Appointment.objects.filter(doctor=request.user)
        }

        return render(request, "doctor.html", context)

def show_json(request):
    data = Appointment.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# apus
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
def forms_ajax(request):
    if request.method == 'POST' and AppointmentForm(request.POST).is_valid():
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


def get_all(request):
    list_dokter = User.objects.filter(role = 2)
    return HttpResponse(serializers.serialize('json', list_dokter)) 