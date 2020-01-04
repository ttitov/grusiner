from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'index.html')

def travel(request):
	return render(request, 'travel.html')

def books(request):
	return render(request, 'books.html')


def guitars(request):
	return render(request, 'guitars.html')