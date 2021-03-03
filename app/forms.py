from django import forms 
from .models import historial
  
class HotelForm(forms.ModelForm): 
  
    class Meta: 
        model = historial 
        fields=["description","Photo"]
       