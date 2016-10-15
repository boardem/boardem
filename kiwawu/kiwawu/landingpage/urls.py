from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from . import views





urlpatterns = [

        url(r'^$', views.landing, name = 'landing'),
        url(r'^aboutus$', views.aboutus, name = 'about'),
        url(r'^contactus$', views.contactus, name = 'contact'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
