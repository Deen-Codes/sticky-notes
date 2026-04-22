"""Django admin configuration for the notes app.

Registering the Note model here exposes it in Django's built-in admin
site (at /admin/) so a superuser can create, edit, and delete notes
through a ready-made interface without writing extra views.
"""

from django.contrib import admin

from .models import Note


# Make the Note model available in the admin site.
admin.site.register(Note)
