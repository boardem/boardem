from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth.models import User
import post
from .views import *
from django.core.urlresolvers import reverse
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth.models import User
from django.contrib.auth.views import logout



urlpatterns = [

         url(r'^$', views.userprofile, name = 'profile'),
         url(r'^edit/$', views.EditUserProfileForm.as_view(), name = 'edit'),
         url(r'^picdelete/$', views.profileimage_delete, name = 'picdelete'),
         url(r'^my_posts/$', views.my_posts, name = 'mypost'),

         url(r'^stuff/$', views.profile_formedit, name = '2profile'),




]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
