from django.contrib import admin
from django.urls import path
from AraxMSS.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('aboutus/',about_us, name='about_us'),
    path('services/',services, name='services'),
    path('securityservices/',securityservices, name='securityservices'),
    path('housekeeping/',housekeeping, name='housekeeping'),
    path('outsourcing/',outsourcing, name='outsourcing'),
    path('video/',video, name='video'),
    path('qrt/',qrt, name='qrt'),
    path('ert/',ert, name='ert'),
    path('gallery/', gallery, name='gallery'),
    path('contactus/',contact_us, name='contact_us'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('contactlist/', contact_list, name='contact_list'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)