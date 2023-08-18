import os, uuid, re
from django.core.exceptions import ValidationError

def validate_file(uploaded_file):
        filename = get_unique_filename(uploaded_file.name)
        uploaded_file.name = filename
        max_size_in_bytes = 3 * 1024 * 1024
        if uploaded_file.size > max_size_in_bytes:
            raise ValidationError('File size must be under 10 MB.')
        return uploaded_file    
    

def get_unique_filename(filename):
        cleaned_filename = clean_filename(filename)
        ext = os.path.splitext(filename)[1]
        unique_filename = f"{uuid.uuid4().hex}{ext}"
        return unique_filename

def clean_filename(filename):
    cleaned_filename = os.path.basename(filename)
    cleaned_filename = cleaned_filename.replace(' ', '_')
    cleaned_filename = re.sub(r'[^\w\s.-]', '', cleaned_filename) 
    return cleaned_filename