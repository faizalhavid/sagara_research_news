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

   