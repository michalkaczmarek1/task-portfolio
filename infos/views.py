from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homepage(request):
	c = {"title": "Home"}
	return render(
		request=request,
		template_name="infos/homepage.html",
        context=c
	)

def about_me(request):
	c = {"title": "O mnie"}
	return render(
		request=request,
		template_name="infos/about_me.html",
		context=c
	)

def contact(request):
	c = {"title": "Kontakt"}
	return render(
		request=request,
		template_name="infos/contact.html",
		context=c
	)
