"""kiwawu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.auth import views
from django.contrib.auth import views as auth_views
from django.contrib.sitemaps.views import sitemap
from post.views import postsitemap


sitemaps = {
            'post':postsitemap,

            }

urlpatterns = [
    url(r'^', include ('landingpage.urls', namespace='landingpage')),
    url(r'^userlogin/', include ('userlogin.urls', namespace='userlogin')),
    url(r'^profile/', include('userprofile.urls', namespace='userprofile')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/login/$', auth_views.login),
    url(r'^post/', include('post.urls', namespace='post')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')

]
