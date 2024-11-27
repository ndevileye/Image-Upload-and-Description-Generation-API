# imageapi/serializers.py

from rest_framework import serializers
from .models import UploadedImage

class UploadedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedImage
        fields = ['id', 'image', 'uploaded_at']

    def validate_image(self, value):

        if value.size > 5 * 1024 * 1024:  # Limit file size to 5MB
            raise serializers.ValidationError("Image file size must be less than 5MB.")
        return value
