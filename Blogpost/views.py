from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from Blogpost.models import Blogpost
from django.core import serializers

# Create your views here.
def show_blogpost(request):
    context = {
        "user": request.user
    }
    return render(request, 'blogpost.html', context)

def show_blogpost_json(request):
    blogposts = Blogpost.objects.all()
    return HttpResponse(serializers.serialize("json", blogposts), content_type="application/json")

def show_blogpost_json_by_id(request, id):
    blogpost = Blogpost.objects.filter(pk = id)
    return HttpResponse(serializers.serialize("json", blogpost), content_type="application/json")

def show_blogpost_by_id(request, id):
    context = {
        "user": request.user,
        "id": id,
    }
    return render(request, 'blogpost_item.html', context)

def update_blogpost(request, id):
    pass

def delete_blogpost(request, id):
    pass