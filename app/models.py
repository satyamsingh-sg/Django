from django.db import models

# Create your models here.
class historial(models.Model):
     description = models.TextField('Description', blank=True)
     Photo= models.FileField(upload_to='img')