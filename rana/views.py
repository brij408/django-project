from django.shortcuts import render

def fun(request):
    return render(request, 'home.html' )

# Create your views here.
