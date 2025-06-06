from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about_us(request):
    return render(request, 'aboutus.html')

def services(request):
    return render(request, 'services.html')

def securityservices(request):
    return render(request, 'securityservices.html')
    
def outsourcing(request):
    return render(request, 'outsourcing.html')
    
def housekeeping(request):
    return render(request, 'housekeeping.html')

def video(request):
    return render(request, 'video.html')

def qrt(request):
    return render(request, 'qrt.html')

def ert(request):
    return render(request, 'ert.html')


from django.shortcuts import render, redirect
from .models import GalleryImage
from .forms import ContactForm
from django.contrib import messages

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact_us')
    else:
        form = ContactForm()
    return render(request, 'contactus.html', {'form': form})

def gallery(request):
    images = GalleryImage.objects.all().order_by('-uploaded_at')
    return render(request, 'gallary.html', {'images': images})

from django.contrib.auth.decorators import login_required
from .models import Contact

@login_required
def contact_list(request):
    contacts = Contact.objects.all().order_by('-created_at')
    return render(request, 'contact_list.html', {'contacts': contacts})
