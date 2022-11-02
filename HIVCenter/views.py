from django.shortcuts import render

# Create your views here.
def show_homepage(request):
    context = {
        "is_authenticated": request.user.is_authenticated
    }

    return render(request, 'homepage.html', context)
