from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def homepage(request):
    return render(request,template_name='main/index.html')
