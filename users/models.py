from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=125)
    code = models.CharField(max_length=125)
    def __str__(self):
        return self.name
    
# Create your models here.
class UserDownload(models.Model):
    name = models.CharField(max_length=125)
    company = models.CharField(max_length=255)
    position = models.CharField(max_length=125)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    country = models.ForeignKey(Country,  on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    