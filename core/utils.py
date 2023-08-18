import os, uuid, re

def clean_filename(filename):
    cleaned_filename = os.path.basename(filename)
    cleaned_filename = cleaned_filename.replace(' ', '_')
    cleaned_filename = re.sub(r'[^\w\s.-]', '', cleaned_filename) 
    return cleaned_filename