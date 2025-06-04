from django.contrib import admin
from django.urls import path
from AraxMSS.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('aboutus/',about_us, name='about_us'),
    path('services/',services, name='services'),
    path('gallery/', gallery, name='gallery'),
    path('contactus/',contact_us, name='contact_us'),
]
