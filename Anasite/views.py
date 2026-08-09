from django.shortcuts import render

from django.http import HttpResponse,JsonResponse 

def index_view(request):
    return render(request,'Anasite/index.html')

def about_view(request):
    return render(request,'Anasite/about.html')

def contact_view(request):
    return render(request,'Anasite/contact.html')

#def blog_view(request):