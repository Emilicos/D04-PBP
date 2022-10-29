import re
from django.shortcuts import render
from Authentication.models import User
from Experience.models import Experience
from .forms import *
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect
from django.core import serializers

# Create your views here.
def show_experience(request):
    print(request.user)
    posts = Experience.objects.all()
    if request.user.get("role") == 1:
        return render(request, 'experience.html', {'posts': posts})
    else:
        return render(request, 'experience-umum.html', {'posts': posts})


def show_experience_detail(request, id):
    post= Experience.objects.get(id=id)
    return render(request, 'experience_detail.html', {'posts': post})

def create_experience(request):
    form = ExperienceForm()
    new_task = None
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.username=request.user.username
            new_task.save()
        return HttpResponseRedirect(reverse("Experience:show_experience"))
        # return HttpResponseRedirect(reverse("todolist:show_todolist"))
    context = {'form': form}
    return render(request, 'experience-form.html', context)

def show_experience_json(request):
    experience = Experience.objects.all()
    return HttpResponse(serializers.serialize("json", experience), content_type="application/json")