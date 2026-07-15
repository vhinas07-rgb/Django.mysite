from django.http import HttpResponse,JsonResponse 

def http_test(request):
    return HttpResponse('<h1>Hiiii,Im Anahita and its a test </h1>')

def json_test(request):
     return JsonResponse({'name':'anahita'})