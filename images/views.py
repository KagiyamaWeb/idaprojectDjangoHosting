from django.shortcuts import get_object_or_404, render, redirect

from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from .models import ImageForm
from .forms import *
from django.http import Http404

def index(request):
    latest_image_list = ImageForm.objects.order_by('-pub_date')
    context = {'latest_image_list': latest_image_list}
    return render(request, 'images/index.html', context)

def image_upload_view(request):  
    if request.method == 'POST': 
        form = UploadForm(request.POST or None, request.FILES or None) 

        if form.is_valid(): 
            form.save() 
            img_obj = form.instance
            return HttpResponseRedirect('../detail/{}'.format(img_obj.id))
    else: 
        form = UploadForm() 
        return render(request, 'images/upload.html', {'form' : form})   


def detail(request, image_id):
    if request.method == 'POST':
        image_detail = ImageForm.objects.all()[image_id - 1]
        image_detail.image_height = request.POST['image_height']
        image_detail.image_width = request.POST['image_width']
        image_detail.save()
        return redirect('.')

    else:
        image_detail =  ImageForm.objects.all()[image_id - 1]
        return render(request, 'images/detail.html', {'image' : image_detail})    

