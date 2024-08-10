from celery import shared_task
import requests
from .models import Image

# @shared_task
# def generate_image(prompt):
#     api_url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"
#     headers = {
#         "Authorization" : f"Bearer{"sk-PtxJE3soGRGjV27QSwG4BTIxQupZSF0RrFUydYxOaoPFukbX"}",
#         "Content-Type" : "application/json"
#     }
#     payload = {
#         "prompt" : prompt,
#         "width" : 1024,
#         "height" : 1024
#     }
#     response = requests.post(api_url, headers=headers, json=payload)
#     if response.status_code == 200:
#         response_data = response.json()
#         image_url = response_data.get("image_url")
#         if image_url:
#             Image.objects.create(prompt=prompt, url = image_url)
#             return image_url
#         else:
#             raise ValueError("No image URL returned from API")
#     else:
#         raise ValueError(f"API request failed with status code {response.status_code}:{response.text}")
    
# tasks.py

import requests
from celery import shared_task

@shared_task
def generate_image(prompt):
    api_url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"
    api_key = "sk-PtxJE3soGRGjV27QSwG4BTIxQupZSF0RrFUydYxOaoPFukbX"  # Replace with your Stability AI API key

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "text_prompts": [{"text": prompt}],
        "cfg_scale": 7,
        "clip_guidance_preset": "FAST_BLUE",
        "height": 1024,
        "width": 1024,
        "samples": 1,
        "steps": 50
    }

    response = requests.post(api_url, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()["artifacts"][0]["base64"]
    else:
        return {"error": response.json()}
