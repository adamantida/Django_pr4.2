from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def homePageView(request):
    return HttpResponse('Hello, World!')


def about(req):
    return render(req, 'about.html')
