from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from Feedback.forms import FeedbackForm
from Feedback.models import FeedbackModel
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def show_feedback(request):
    context = {
        "user": request.user
    }
    return render(request, 'feedback.html', context)

@csrf_exempt
def create_feedback(request): # submit feedback
    # if(request.method == "POST" and request.user.isPasien == true):
    if(request.method == "POST" ):
        form = FeedbackForm(request.POST)
        if(form.is_valid):
            # form.instance.user = request.user
            formSave = form.save()
            return JsonResponse({
                "data": form.data,
                "id": formSave.id,
            })

        return JsonResponse({"data": {
            # "user": request.user,
            # "username": request.user.name
        }})
    else:       
        raise PermissionDenied("Anda bukan pasien!")

def show_feedback_json(request):
    feedbacks = FeedbackModel.objects.all()
    return HttpResponse(serializers.serialize("json", feedbacks), content_type="application/json")

def delete(request, pk):
    FeedbackModel.objects.filter(id=pk).delete()
    return redirect('feedback:show_feedback')
