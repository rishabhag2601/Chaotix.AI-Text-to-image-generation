# chaotix_ai/urls.py

from django.contrib import admin
from django.urls import path, include
from image_generator.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('img-gen/', include('image_generator.urls')),
    path('', home_view),  # Add this line to handle the root URL
]
