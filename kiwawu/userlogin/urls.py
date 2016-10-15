from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth.models import User
from django.contrib.auth.views import logout

urlpatterns = [

    url(r'^home/$', views.home, name = 'home'),
    url(r'^$', views.userformview.as_view(), name = 'registernow'),
    url(r'^logout/$', views.logoutview, name='logout' ),
    url(r'^login/$', views.loginview, name = 'login' ),
#    url(r'^listview/$', views.index.as_view(), name="index1"),
#    url(r'^detailview(?P<pk>\d+)/$', views.postdetail.as_view()),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
