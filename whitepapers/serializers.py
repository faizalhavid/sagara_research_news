from rest_framework import serializers
from .models import WhitePapers, Topic
import os, uuid , re
from django.utils import timezone
from core.utils import clean_filename




class WhitePaperListSerializers(serializers.ModelSerializer):
    class Meta :
        model = WhitePapers
        fields = ['title', 'description', 'published_at', 'image']

   