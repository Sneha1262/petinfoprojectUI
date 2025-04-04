from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Pet

def home(request):
    pets = Pet.objects.all()
    return render(request, 'blog/home.html', {'pets': pets})
