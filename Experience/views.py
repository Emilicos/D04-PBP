from django.shortcuts import render
from django.contrib.auth.models import User
from Experience.models import Experience
from .forms import *
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect
from django.core import serializers
import datetime  

# Create your views here.


def show_experience(request):
    posts = Experience.objects.all()
    if request.user.is_authenticated:
        print(request.user.role)
        if request.user.role == 1:
            return render(request, 'experience.html', {'posts': posts,'form':ExperienceForm()})
        else:
            return render(request, 'experience-umum.html', {'posts': posts})
    else:
        return render(request, 'experience-umum.html', {'posts': posts,})
        
    

def show_experience_detail(request, id):
    post= Experience.objects.get(id=id)
    if request.user.is_authenticated:
        return render(request, 'experience_detail.html', {'posts': post})
    else:
        return render(request, 'experience-detail-umum.html', {'posts': post})
       

# def create_experience(request):
#     form = ExperienceForm()
#     new_task = None
#     if request.method == 'POST':
#         form = ExperienceForm(request.POST)
#         if form.is_valid():
#             new_task = form.save(commit=False)
#             new_task.user = request.user
#             new_task.username=request.user.username
#             new_task.save()
#         return HttpResponseRedirect(reverse("Experience:show_experience"))
#         # return HttpResponseRedirect(reverse("todolist:show_todolist"))
#     context = {'form': form}
#     return render(request, 'experience-form.html', context)

def create_experience_ajax(request):
    if request.method == 'POST' and request.user.is_authenticated:
        title = request.POST.get('title')
        experience = request.POST.get('experience')
        user = request.user
        date= datetime.datetime.now()
        item = Experience(user = user, username=user.username, posted=date, title=title,preview="", experience=experience)
        item.save()
        return JsonResponse({"Message": "Task Success"},status=200)
    else:
        response = JsonResponse({"error": "Anda belum terautentikasi atau tidak melakukan method POST"})
        response.status_code = 403 # To announce that the user isn't allowed to publish
        return response

def show_experience_json(request):
    experience = Experience.objects.all()
    return HttpResponse(serializers.serialize("json", experience), content_type="application/json")