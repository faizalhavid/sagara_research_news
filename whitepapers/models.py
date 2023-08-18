from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from core.utils import clean_filename
import os, uuid , re
from django.core.validators import FileExtensionValidator , MaxValueValidator
from core.utils import validate_file



class Topic(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    def __str__(self):
        return self.title
    
    



class WhitePapers(models.Model):
    class WhitePaperObject(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(published_at__isnull=False).order_by('-published_at')
        
    STATUS = (
        ('Arcives', 'Arcives'),
        ('Published', 'Published'),
        ('Draft', 'Draft'),
    )
    title = models.CharField(max_length=255)
    description = models.TextField(default="")
    detail = models.TextField(default="")
    about = models.TextField(default="")
    status = models.CharField(max_length=120, choices=STATUS, default="draft")
    published_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=100, unique_for_date = 'published_at', blank=True)
    count_of_downloads = models.IntegerField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    image = models.ImageField(upload_to='whitepapers/images/', validators=[FileExtensionValidator( ['png', 'jpg', 'jpeg'] ), validate_file], blank = True)
    pdf = models.FileField(upload_to='whitepapers/pdf/', validators=[FileExtensionValidator( ['pdf'] ), validate_file], blank=True)
    
    def update(self):
        if self.status == 'Published':
            self.published_at = timezone.now()
        if not self.slug:  
            self.slug = slugify(self.title)
        super().save()

    
    def clean(self):
        if self.pk is None:
            if self.status == 'Published':
                self.published_at = timezone.now()
        if not self.slug:  
            self.slug = slugify(self.title)
        
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.title
