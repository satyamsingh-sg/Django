from django.shortcuts import render,redirect
from django.http import HttpResponse
from.forms import HotelForm
from .models import historial

def hotel_image_view(request): 
  
    if request.method == 'POST': 
        form = HotelForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            form = HotelForm() 
    else: 
        form = HotelForm() 
    return render(request, 's1.html', {'fm' : form}) 
  



def Show(request):
    st=historial.objects.all()
    return render(request, 's2.html', {'hotel_images' : st}) 
  