from django.shortcuts import render
from userlogin.forms import  userform
from django.contrib.sitemaps import Sitemap

# Create your views here.
def landing(request):
    user = userform(request.POST or None)
    context = {
        "form":user,
    }

    return render(request, 'landingpage/home.html', context)

def aboutus(request):


    return render(request, 'landingpage/aboutus.html')

def contactus(request):


    return render(request, 'landingpage/contactus.html')
