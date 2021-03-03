from django.contrib import admin
from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static 
from app.views import *
urlpatterns = [ 
    path('/data', hotel_image_view, name = 'image_upload'), 
    
    
] 
  
if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT)
