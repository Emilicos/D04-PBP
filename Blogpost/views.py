from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from Blogpost.forms import BlogpostForm
from Blogpost.models import BlogpostModel
from django.core import serializers
from datetime import date
import json

# Create your views here.
def show_blogpost(request):
    context = {
        "user": request.user
    }
    return render(request, 'blogpost.html', context)

def show_blogpost_json(request):
    importance = request.GET.get("importance")

    if(importance == "DT"):
        blogposts = BlogpostModel.objects.all()
    else:
        blogposts = BlogpostModel.objects.filter(importance = importance)
        
    return HttpResponse(serializers.serialize("json", blogposts), content_type="application/json")

def show_blogpost_json_by_id(request, id):
    blogpost = BlogpostModel.objects.filter(pk = id)
    return HttpResponse(serializers.serialize("json", blogpost), content_type="application/json")

def show_blogpost_by_id(request, id):
    context = {
        "user": request.user,
        "id": id,
    }
    return render(request, 'blogpost_item.html', context)

def create_blogpost(request):
    if(request.method == "POST"):
        form = BlogpostForm(request.POST)
        if(form.is_valid()):
            # form.instance.user = request.user
            form_id = form.save()
            return JsonResponse({
                "data": form.data,
                "date": date.today(),
                "id": form_id.id,
            })

def update_blogpost(request, id):
   if(request.method == "PUT"):
        blogpost = BlogpostModel.objects.get(pk = id)
        items = request.body.decode("utf-8").split("&")
        for item in items:
            item = item.split("=")
            s = ""
            item[1] = item[1].replace("+", " ")
            item[1] = item[1].replace("%2C", ",")
            item[1] = item[1].replace("%C3%B8", "ø")
            item[1] = item[1].replace("%3B", ";")
            item[1] = item[1].replace("%0A", " ")
            item[1] = item[1].replace('%2F', "/")
            item[1] = item[1].replace("%E2%80%94", "-")
            item[1] = item[1].replace("%22", '"')
            print(item[1])
            if(item[0] == "title"):
                blogpost.title = item[1]
            elif(item[0] == "opening"):
                blogpost.opening = item[1]
            elif(item[0] == 'main'):
                blogpost.main = item[1]
            elif(item[0] == 'closing'):
                blogpost.closing = item[1]
            elif(item[0] == 'importance'):
                blogpost.importance = item[1]

        blogpost.save()

        return JsonResponse({
            "message": "Update berhasil"
        })


def delete_blogpost(request, id):
   if(request.method == "DELETE"):
        BlogpostModel.objects.get(pk = id).delete()

        return JsonResponse({
            "message": "Delete berhasil"
        })

