from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from Blogpost.forms import BlogpostForm
from Blogpost.models import BlogpostModel
from django.core import serializers
from datetime import date
from Authentication.models import User

# Create your views here.
def show_blogpost(request):
    form = BlogpostForm()
    context = {
        "is_authenticated": request.user.is_authenticated,
        "user": request.user,
        "role": request.user.role if request.user.is_authenticated else None,
        "form": form
    }
    
    return render(request, 'blogpost.html', context)

def show_user(request, id):
    username = User.objects.filter(pk = id)
    hasil = ""
    for index, item in enumerate(username):
        data = item
        hasil = item.__str__()

    hasil = hasil[0:20]
    return JsonResponse({"user": hasil})

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
        "is_authenticated": request.user.is_authenticated,
        "user": request.user,
        "id": id,
    }
    return render(request, 'blogpost_item.html', context)

def create_blogpost(request):
    if(request.method == "POST" and request.user.is_authenticated):
        if(request.user.role == 2):
            form = BlogpostForm(request.POST)
            if(form.is_valid()):
                form.instance.user = request.user
                form_id = form.save()
                return JsonResponse({
                    "status_code": 200,
                    "data": form.data,
                    "date": date.today(),
                    "id": form_id.id,
                })
        else:
            response = JsonResponse({"error": "Anda bukan dokter, sehingga anda tidak dapat membuat Blog"})
            response.status_code = 403 # To announce that the user isn't allowed to publish
            return response
            #raise PermissionDenied()
    else:
        response = JsonResponse({"error": "Anda belum terautentikasi atau tidak melakukan method POST"})
        response.status_code = 403 # To announce that the user isn't allowed to publish
        return response

def update_blogpost(request, id):
    if(request.method == "PUT" and request.user.is_authenticated):
        if(request.user.role == 2):
            blogpost = BlogpostModel.objects.get(pk = id)
            items = request.body.decode("utf-8").split("&")
            if(blogpost.user == request.user):
                blogpost.user = request.user
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
            else:
                response = JsonResponse({"error": "Anda bukan user yang membuat blog"})
                response.status_code = 403 # To announce that the user isn't allowed to publish
                return response
                # raise PermissionDenied("Anda bukan user yang membuat blog")
        else:
            response = JsonResponse({"error": "Anda bukan dokter, sehingga anda tidak dapat mengubah Blog"})
            response.status_code = 403 # To announce that the user isn't allowed to publish
            return response
    else:
        response = JsonResponse({"error": "Anda belum terautentikasi atau tidak melakukan method PUT"})
        status_code = 403 # To announce that the user isn't allowed to publish
        return JsonResponse({'message':"Anda belum terautentikasi atau tidak melakukan method PUT" }, status=status_code)



def delete_blogpost(request, id):
    if(request.method == "DELETE" and request.user.is_authenticated):
        if(request.user.role == 2):
            blogpost = BlogpostModel.objects.get(pk = id)
            if(blogpost.user == request.user):
                blogpost.delete()
                return JsonResponse({
                    "message": "Delete berhasil"
                })
            else:
                response = JsonResponse({"error": "Anda bukan user yang membuat blog"})
                response.status_code = 403 # To announce that the user isn't allowed to publish
                return response
        else:
            response = JsonResponse({"error": "Anda bukan dokter, sehingga anda tidak dapat menghapus Blog"})
            response.status_code = 403 # To announce that the user isn't allowed to publish
            return response
    else:
        response = JsonResponse({"error": "Anda belum terautentikasi atau tidak melakukan method DELETE"})
        response.status_code = 403 # To announce that the user isn't allowed to publish
        return response
