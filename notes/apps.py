"""Application configuration for the notes app.

Django auto-discovers this AppConfig class to register the app and
apply any app-specific settings (such as the default auto-incrementing
primary key field type).
"""

from django.apps import AppConfig


class NotesConfig(AppConfig):
    """Configuration object for the notes Django app."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notes'
