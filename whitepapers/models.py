from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from core.utils import clean_filename
import os, uuid , re


class Topic(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    def __str__(self):
        return self.title
    
class FileValidationMixin:
    def get_unique_filename(self, filename):
        cleaned_filename = clean_filename(filename)
        ext = os.path.splitext(filename)[1]
        unique_filename = f"{uuid.uuid4().hex}{ext}"
        return unique_filename
    
    def validate_file(self, file):
        file = self.get_unique_filename(file.name)
        max_size = 10
        max_size_in_bytes = max_size * 1024 * 1024
        allowed_types = ['application/pdf']

        if file.size > max_size_in_bytes:
            raise ValueError('File size must be under 10 MB.')

        if file.content_type.split('/')[0] not in allowed_types:
            raise ValueError('File type not supported.')

        return file

    def validate_image(self, image):
        max_size = 3
        max_size_in_bytes = max_size * 1024 * 1024
        allowed_types = ['image/jpeg', 'image/png']  

        if self.image.size > max_size_in_bytes:
            raise ValueError('Image size must be under 3 MB.')

        if image.file.content_type not in allowed_types:
            raise ValueError('Image type not supported.')
        
        return image
    
class WhitePapers(models.Model, FileValidationMixin):
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
    image = models.ImageField(upload_to='whitepapers/images/')
    file = models.FileField(upload_to='whitepapers/files/')
    
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
        self.file = self.validate_file(self.file)
        self.image = self.validate_image(self.image)
        
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.title
