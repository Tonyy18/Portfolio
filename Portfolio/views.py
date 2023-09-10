from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def robot(request):
    f = open("resources/robot.txt")
    text = f.read()
    return HttpResponse(text, content_type="text/plain")

def sitemap(request):
    f = open("resources/sitemap.xml")
    text = f.read()
    return HttpResponse(text, content_type='text/xml')
