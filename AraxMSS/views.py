from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about_us(request):
    return render(request, 'aboutus.html')

def services(request):
    return render(request, 'services.html')

def gallery(request):
    return render(request, 'gallery.html')

def contact_us(request):
    return render(request, 'contactus.html')
