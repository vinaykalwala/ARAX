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

def technology(request):
    return render(request, 'technology.html')


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


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import GalleryImage
from .forms import GalleryImageForm

def upload_gallery_image(request):
    # Handle DELETE
    if request.method == 'POST' and 'delete_id' in request.POST:
        image_to_delete = get_object_or_404(GalleryImage, id=request.POST.get('delete_id'))
        image_to_delete.delete()
        messages.success(request, 'Image deleted successfully.')
        return redirect('upload_gallery_image')

    # Handle EDIT
    elif request.method == 'POST' and 'edit_id' in request.POST:
        image_to_edit = get_object_or_404(GalleryImage, id=request.POST.get('edit_id'))
        image_to_edit.title = request.POST.get('edit_title')
        image_to_edit.description = request.POST.get('edit_description')
        if 'edit_image' in request.FILES:
            image_to_edit.image = request.FILES['edit_image']
        image_to_edit.save()
        messages.success(request, 'Image updated successfully.')
        return redirect('upload_gallery_image')

    # Handle NEW UPLOAD
    elif request.method == 'POST':
        form = GalleryImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Image uploaded successfully.')
            return redirect('upload_gallery_image')
    else:
        form = GalleryImageForm()

    images = GalleryImage.objects.all().order_by('-uploaded_at')
    return render(request, 'upload_gallery.html', {'form': form, 'images': images})
