from rest_framework import serializers
from .models import WhitePapers, Topic
import os, uuid , re
from django.utils import timezone
from core.utils import clean_filename




class WhitePaperSerializers(serializers.ModelSerializer):
    class Meta :
        model = WhitePapers
        fields = [
            'title',
            'description',
            'detail',
            'about',
            'status',
            'published_at',
            'count_of_downloads',
            'topic',
            'author',
            'image',
            'file'
        ]

    def get_unique_filename(self, filename):
        """
        Generate a unique filename using UUID.
        """
        cleaned_filename = clean_filename(filename)
        ext = os.path.splitext(filename)[1]
        unique_filename = f"{uuid.uuid4().hex}{ext}"
        return unique_filename
    
    def validate_file(self, file):
        max_size = 3
        max_size_in_bytes = max_size * 1024 * 1024
        allowed_types = ['application/pdf']  

        if file.size > max_size_in_bytes:
            raise serializers.ValidationError('File size must be under 3 MB.')

        if file.content_type not in allowed_types:
            raise serializers.ValidationError('File type not supported.')

        return file
    
    def validate_image(self, image):
        max_size = 1
        max_size_in_bytes = max_size * 1024 * 1024
        allowed_types = ['image/jpeg', 'image/png']  

        if image.size > max_size_in_bytes:
            raise serializers.ValidationError('Image size must be under 3 MB.')

        if image.content_type not in allowed_types:
            raise serializers.ValidationError('Image type not supported.')
        return image
    
    def create(self, validated_data):
        file_uploaded = validated_data.get('file')
        image_uploaded = validated_data.get('image')
        status = validated_data.get('status')
        
        filename = self.get_unique_filename(file_uploaded.name)
        image_name = self.get_unique_filename(image_uploaded.name)
        validated_data['file'].name = filename
        validated_data['image'].name = image_name
        if status == 'Published':
            validated_data['published_at'] = timezone.now()
        
        return WhitePapers.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        status = validated_data.get('status')
        if status == 'Published':
            validated_data['published_at'] = timezone.now()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        return instance