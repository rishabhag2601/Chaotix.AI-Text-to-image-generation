# image_generator/urls.py

from django.urls import path
from .views import generate_image_view, home_view

urlpatterns = [
    path('generate-images/', generate_image_view, name='generate_image'),
    path('', home_view, name='home'),  # Add this line to handle 'img-gen/' path
]
