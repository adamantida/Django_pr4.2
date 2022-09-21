from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def homePageView(request):
    return render(request, 'home.html')


def about(req):
    return render(req, 'about.html')

def base(req):
    return render(req, 'base.html')