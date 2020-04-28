from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'prueba2/index.html', {})