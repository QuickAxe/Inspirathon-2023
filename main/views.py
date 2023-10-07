from rest_framework.response import Response 
from rest_framework.decorators import api_view 
from main.models import *
# from api.serializer import *
# Create your views here.
import os
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.models import Image
# from main.serializers import ImageSerializer  # If you have a serializer for Image

@api_view(['GET'])
def result(request, image_id):
    try:
        image = Image.objects.get(id=image_id)
    except Image.DoesNotExist:
        return Response({'message': 'Image not found'}, status=404)

    # You can serialize the image data if needed
    # serializer = ImageSerializer(image)

    return Response({'url': image.url, 'text': image.text

})  # Return image data

@api_view(['POST'])
def upload(request):
    # Assuming you're sending the file as 'image' in the POST request
    uploaded_file = request.FILES.get('image')
    if uploaded_file:
        # Save the uploaded file to a temporary location
        file_name = default_storage.save(os.path.join(settings.MEDIA_ROOT, 'temp', uploaded_file.name), ContentFile(uploaded_file.read()))

        # Generate the URL for the uploaded file
        file_url = os.path.join(settings.MEDIA_URL, 'temp', uploaded_file.name)

        # Create a new Image object and save it to the database
        image = Image(url=file_url, user=request.user, text='')  # Assuming request.user is authenticated
        image.save()

        return Response({'message': 'Image uploaded successfully!', 'url': file_url})
    else:
        return Response({'message': 'No file uploaded!'}, status=400)
