from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response, render, HttpResponseRedirect, HttpResponse, get_object_or_404, redirect
from django.template import context, RequestContext
from .models import textpost
from .forms import PostForm
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
from django.utils.http import urlquote_plus
from django.utils import timezone
from userlogin.views import userform
from django.forms import modelformset_factory
from .models import textpost, Images
from django.contrib.sitemaps import Sitemap
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required
def post_create(request):

	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		# message success
		messages.success(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form": form,

	}
	return render(request, "post.html", context)

@login_required
def post_detail(request, slug=None):
	instance = get_object_or_404(textpost, slug=slug)
	share_string = 0
	if instance.publish > timezone.now().date() or instance.draft:
		share_string = urlquote_plus(instance.text_post_content)
	context = {
		"title": instance.text_post_title,
		"post": instance,
		"share_string": share_string,

	}
	return render(request, "postdetail.html", context)

@login_required
def post_list(request):
	today = timezone.now().date()
	#queryset_list = textpost.objects.active() #.order_by("-timestamp")
	queryset_list = textpost.objects.all()
	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(
				Q(text_post_title__icontains=query)
				# Q(content__icontains=query)|
				# Q(user__first_name__icontains=query) |
				# Q(user__last_name__icontains=query)
				).distinct()
	paginator = Paginator(queryset_list, 8) # Show 25 contacts per page
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)


	context = {
		"object_list": queryset,
		"title": "List",
		"page_request_var": page_request_var,
		"today": today,

	}
	return render(request, "search_results.html", context)




@login_required
def post_update(request, slug=None):
	instance = get_object_or_404(textpost, slug=slug)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title": instance.text_post_title,
		"instance": instance,
		"form":form,

	}
	return render(request, "textpost_update_form.html", context)


@login_required
def post_delete(request, slug=None):
	instance = get_object_or_404(textpost, slug=slug)
	instance.delete()
	messages.success(request, "Successfully deleted")
	return redirect("post:newsfeed")

@login_required
def search(request):
	error = 0
	post=0
	queryset_list = textpost.objects.all()
	query = request.GET.get("q")
	if query in request.GET and request.GET[q]:
		query = request.GET[q]
		#post = textpost.objects.filter(text_post_title__icontains=query, text_post_content__icontains=query)
		queryset_list = queryset_list.filter(
				Q(text_post_title__icontains=query)|
				Q(content__icontains=query)|
				Q(user__first_name__icontains=query) |
				Q(user__last_name__icontains=query)
				).distinct()
		return render(request, 'search_results.html', context)
	else:
	    context = {
	        "query": query,
	        #"post": post,
	            }
	    return render( request, 'search_results.html', context)

@login_required
def newsfeed(request):
    all_post = textpost.objects.all().order_by("-time_stamp")

    context = {
        "all_post":all_post,

        }
    return render(request, 'newsfeed.html',context)


class postsitemap(Sitemap):
		changefreq = "always"
		priority = 1.0

		def items(self):
			return textpost.objects.all()
		def lastmod(self, obj):
			return obj.publish
