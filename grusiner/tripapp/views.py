from django.shortcuts import render
from .models import Country

# Create your views here.
def index(request):
	return render(request, 'index.html')

def travel(request):
	country_list = Country.objects.order_by('id')
	return render(request, 'travel.html', {'countries':  country_list})

def books(request):
	return render(request, 'books.html')

def guitars(request):
	return render(request, 'guitars.html')