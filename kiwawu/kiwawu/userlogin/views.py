from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response, render, HttpResponseRedirect, HttpResponse, get_object_or_404, redirect
from django.template import context
from .forms import  userform #create_post_form
from django.template import RequestContext
from django.views.generic.edit import *
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import View, TemplateView
from django.views import generic
from django.contrib.auth.models import Group
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth import logout


class userformview(View):
    form_class = userform
    template_name = 'post.html'


    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        normaluser = Group.objects.get(name='normaluser')
        if form.is_valid():

            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user.groups.add(normaluser)
            user = authenticate(username=username, password=password)

            if user is not None:
                    if user.is_active:
                        login(request, user)
                    return redirect('/profile')


        return render(request, self.template_name, {'form':form})




def logoutview(request):

    logout(request)
    return HttpResponseRedirect('/')

def home(request):
    user = userform(request.POST or None)
    context = {
        "form":user,
    }
    return render(request, 'landingpage/home.html', context)



def loginview(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/profile/')
    else:
        return render(request, 'userlogin/login.html')
