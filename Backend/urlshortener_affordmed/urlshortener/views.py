from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseNotFound
from .models import ShortURL
from django.utils import timezone

#this file contains views for the URL shortener application
#this function handles the shortening of URLs
def shorten_url(request):
    if request.method == 'POST':
        data = request.POST
        original_url = data.get('url')
        custom_code = data.get('custom_code')
        expires_in = data.get('expires_in')  # in days (optional)

        short_code = custom_code if custom_code else None
        if short_code:
            if ShortURL.objects.filter(short_code=short_code).exists():
                return JsonResponse({'error': 'Custom code already exists'}, status=400)
        else:
            short_code = None  # will be generated automatically

        expires_at = timezone.now() + timezone.timedelta(days=int(expires_in)) if expires_in else None

        short_url = ShortURL.objects.create(
            original_url=original_url,
            short_code=short_code or '',  # triggers default generator
            expires_at=expires_at
        )
        return JsonResponse({'short_url': request.build_absolute_uri(f'/{short_url.short_code}')})

    return JsonResponse({'error': 'POST required'}, status=405)

#this function handles the redirection from short URL to original URL1
def redirect_url(request, code):
    try:
        short_url = ShortURL.objects.get(short_code=code)
        if short_url.is_expired():
            return HttpResponseNotFound("This link has expired.")
        return redirect(short_url.original_url)
    except ShortURL.DoesNotExist:
        return HttpResponseNotFound("Short URL not found.")


# Create your views here.
