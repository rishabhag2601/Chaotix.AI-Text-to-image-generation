# from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from image_generator.tasks import generate_image
from celery import group

def home_view(request):
    return HttpResponse("Welcome to the Image Generator App!")

def generate_image_view(request):
    prompts = ["A red flying dog", "A piano ninja", "A footballer kid"]
    result = group(generate_image.s(prompt) for prompt in prompts).apply_async()
    images = result.get()  # Wait for the group result and get it

    # Check for errors and prepare the response
    response_data = []
    for image in images:
        if isinstance(image, dict) and "error" in image:
            response_data.append({"error": image["error"]})
        else:
            response_data.append({"image": image})

    return JsonResponse(response_data, safe=False)

# # Create your views here.
# from django.http import JsonResponse
# from image_generator.tasks import generate_image
# from celery import group

# # def generate_image_view(request):
# #     prompts : ["A red flying dog", "A piano ninja", "A footballer kid"]
# #     result = group(generate_image.s(prompt) for prompt in prompts).apply_async()
# #     return JsonResponse(result.get(), safe=False)

# # views.py

# from django.shortcuts import render
# from django.http import JsonResponse
# from .tasks import generate_image
# from celery import group

# # def generate_image_view(request):
# #     prompts = ["A red flying dog", "A piano ninja", "A footballer kid"]
# #     result = group(generate_image.s(prompt) for prompt in prompts).apply_async()
# #     images = result.get()  # Wait for the group result and get it

# #     # Check for errors and prepare the response
# #     response_data = []
# #     for image in images:
# #         if isinstance(image, dict) and "error" in image:
# #             response_data.append({"error": image["error"]})
# #         else:
# #             response_data.append({"image": image})

# #     return JsonResponse(response_data, safe=False)

# def generate_image_view(request):
#     prompts = ["A red flying dog", "A piano ninja", "A footballer kid"]
#     result = group(generate_image.s(prompt) for prompt in prompts).apply_async()
#     images = result.get()  # Wait for the group result and get it

#     # Check for errors and prepare the response
#     response_data = []
#     for image in images:
#         if isinstance(image, dict) and "error" in image:
#             response_data.append({"error": image["error"]})
#         else:
#             response_data.append({"image": image})

#     return JsonResponse(response_data, safe=False)