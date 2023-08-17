from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
def home(request):
    response = HttpResponse()
    response.content = " I'm learning Django. I'm enjoying it"
    return response




def index(request):
    return render(request, template_name="myapp/index.html")


def nisa(request):
    return render(request, template_name="myapp/nisa.html")