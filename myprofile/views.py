from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	return render(request, 'myprofile/index.html')

def about(request):
	return render(request, 'myprofile/about.html')

def resume(request):
	return render(request, 'myprofile/resume.html')

def services(request):
	return render(request,'myprofile/services.html')

def contact (request):
	return render(request, 'myprofile/contact.html')
