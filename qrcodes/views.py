from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from .models import Game
from PIL import Image
import os

def upload_qr_codes(request):
    if request.method == 'POST':
        height = int(request.POST['height'])
        width = int(request.POST['width'])

        # Handling folder upload
        if 'image_folder' in request.FILES:
            for file in request.FILES.getlist('image_folder'):
                process_file(file, height, width)

        # Handling individual file uploads
        if 'image_files' in request.FILES:
            for file in request.FILES.getlist('image_files'):
                process_file(file, height, width)

        return render(request, 'upload_success.html')

    return render(request, 'upload_qr_codes.html')

def process_file(file, height, width):
    # Open and resize the image
    with Image.open(file) as img:
        img = img.resize((width, height), Image.Resampling.LANCZOS)
        
        # Create the directory if it does not exist
        img_dir = os.path.join(settings.MEDIA_ROOT, 'qrcodes')
        os.makedirs(img_dir, exist_ok=True)
        
        # Save the image
        img_path = os.path.join(img_dir, file.name)
        img.save(img_path)

        # Save the name and path to the database
        game = Game(name=file.name)
        game.image.name = os.path.join('qrcodes', file.name)
        game.save()
