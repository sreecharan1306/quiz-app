from django.shortcuts import redirect
from django.urls import resolve, Resolver404

class RedirectToHomeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            # Check if the requested URL is defined in urls.py
            resolve(request.path_info)
        except Resolver404:
            # If not defined, redirect to the home page
            return redirect('home')

        response = self.get_response(request)
        return response