from django.urls import path
from .views import ImageDescriptionAPIView

urlpatterns = [
    path('upload/', ImageDescriptionAPIView.as_view(), name='image-upload')
]
