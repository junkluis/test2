from django.shortcuts import render

# Create your views here.
def index(request):
    dict = {}
    dict["inicio"] = "inicio"
    return render(request, 'prueba2/index.html', dict)

def auth(request):
    dict = {}
    dict["inicio"] = "auth"
    return render(request, 'prueba2/index.html', dict)