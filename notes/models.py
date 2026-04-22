"""Database models for the Sticky Notes application.

This module defines the data layer of the app. Each model class becomes
a table in the database via Django's ORM, and migrations keep the
database schema in sync with the model definitions.
"""

from django.db import models


class Note(models.Model):
    """A single sticky note created by a user.

    Fields:
        title: A short heading for the note (CharField, up to 255 chars).
        content: The body text of the note (TextField, unlimited length).
        created_at: Timestamp automatically set when the note is first
            saved (DateTimeField with auto_now_add=True).

    Methods:
        __str__: Returns the note's title so the object is shown by its
            title in the Django admin and any debug output.
    """

    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the note's title as its human-readable representation."""
        return self.title
