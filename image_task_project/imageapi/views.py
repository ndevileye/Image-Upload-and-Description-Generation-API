from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework import status
from .serializers import UploadedImageSerializer
from openai import OpenAI
from django.conf import settings
import logging
import os

# Configure logging
logger = logging.getLogger(__name__)

# Set up OpenAI API key from settings

client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])
#openai.api_key = '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'  # Ensure this is configured in your settings.py

class ImageDescriptionAPIView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request):
        try:
            # Validate and save the image
            serializer = UploadedImageSerializer(data=request.data)
            if serializer.is_valid():
                image_obj = serializer.save()
                image_url = request.build_absolute_uri(image_obj.image.url)

                # Analyze image
                try:
                    image_info = self.analyze_image(image_url)
                except Exception as e:
                    logger.error(f"Image analysis failed: {e}")
                    return Response(
                        {"error": "Failed to analyze image", "description": str(e)},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR
                    )

                # Generate descriptions
                try:
                    descriptions = self.generate_descriptions(image_info)
                except Exception as e:
                    error_response = e.args[0]
                    return Response(
                        error_response,
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR
                    )

                return Response({
                    "image_url": image_url,
                    "descriptions": descriptions
                }, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return Response(
                {"error": "An unexpected error occurred", "description": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def analyze_image(self, image_url):
        """
        Simulates image analysis. Replace this method with an actual image analysis API
        (e.g., Google Vision API, AWS Rekognition, etc.).
        """
        try:
            # For now, return a static analysis result
            return "A beautiful sunset over the ocean with clouds"
        except Exception as e:
            logger.error(f"Error during image analysis: {e}")
            raise

    def generate_descriptions(self, image_info):
        """
        Generates descriptions in formal, humorous, and critical tones using OpenAI GPT.
        """
        try:
            # Define prompts for different tones
            prompts = {
                "formal": f"Describe this image in a formal and neutral tone: {image_info}",
                "humorous": f"Describe this image in a funny tone: {image_info}",
                "critical": f"Describe this image in a critical and sarcastic tone: {image_info}",
            }

            # Generate responses using ChatCompletion
            descriptions = {}
            for tone, prompt in prompts.items():
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",  # Use "gpt-3.5-turbo" if GPT-4 isn't available
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=150,
                    temperature=0.7  # Adjust as needed for creativity
                )


                descriptions[tone] = response['choices'][0]['message']['content'].strip()

            return descriptions
        except Exception as e:

            logger.error(f"Error during description generation: {e}")
            raise Exception({"error": "Failed to generate descriptions", "description": str(e)})
