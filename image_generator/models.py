from django.db import models

# Create your models here.
class Image(models.Model):
    prompt = models.CharField(max_length=255)
    url = models.URLField()
    generated_at = models.DateTimeField(auto_now_add=True)