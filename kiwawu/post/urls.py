from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth.models import User


urlpatterns = [


url(r'^post/$', views.post_create, name = 'post'),
#post DEtail
url(r'^postdetail/(?P<slug>[\w-]+)$', views.post_detail, name = 'postdetail'),
#this updates the post
url(r'^postdetailupdate(?P<slug>[\w-]+)/$', views.post_update, name = 'postdetailupdate'),
#this is DeleteView
url(r'^postdetaildelete(?P<slug>[\w-]+)/$', views.post_delete, name = 'postdetaildelete'),


#this is the newsfeed
url(r'^newsfeed/$', views.newsfeed, name = 'newsfeed'),
#this is a search url
url(r'^search-form/$', views.post_list, name= 'search'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
