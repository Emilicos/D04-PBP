
from django.forms import model_to_dict
from Booking.forms import AppointmentForm

from Booking.models import Appointment

from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from Authentication.models import User

# Create your views here.

# Show HTML based on role, either booking.html (if patient) or doctor.html (if doctor) will show up
@login_required(login_url='/authentication/login/')
def show_booking(request):

    if request.user.role == 1:
        list_dokter = User.objects.filter(role = 1)
        lst = []
        for i in range (len(list_dokter)):
            lst.append(model_to_dict(list_dokter[i]).get("username"))
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

# Show ALL appointments booked by logged in user
@login_required(login_url='/authentication/login/')
def show_json(request):
    data = Appointment.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# Show appointments based on string on the 'search' input AND currently logged in user
@login_required(login_url='/authentication/login/')
def get_dokter_json(request):
    dokter = request.GET.get('search')
    if not dokter:
        dokter = ''
    list_dokter = Appointment.objects.filter(user=request.user, doctor__icontains=dokter)
    return HttpResponse(serializers.serialize('json', list_dokter), content_type="application/json")

# Add an appointmnet
@login_required(login_url='/authentication/login/')
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

# Delete an appointment
@login_required(login_url='/authentication/login/')
@csrf_exempt
def delete_booking(request, id):
    if request.method == 'DELETE':
        booking = Appointment.objects.get(user=request.user, id=id)
        booking.delete()
        return JsonResponse({ "Message": "Appointment Cancelled" }, status=200)