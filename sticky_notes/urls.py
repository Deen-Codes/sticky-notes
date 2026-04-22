"""Project-level URL configuration for the sticky_notes project.

This is the entry point Django uses to dispatch any incoming request.
It delegates to two routes:

    - /admin/ ........ Django's built-in admin site.
    - /         ...... All notes-app URLs (defined in notes/urls.py).
"""

from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('notes.urls')),
]
