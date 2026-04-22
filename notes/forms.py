"""Form definitions for the Sticky Notes application.

ModelForms tie the HTML form layer to the database model layer so the
view code does not have to manually validate or copy field values.
"""

from django import forms

from .models import Note


class NoteForm(forms.ModelForm):
    """ModelForm for creating and editing Note objects.

    The Meta inner class tells Django which model to bind to and which
    fields to expose to the user. Using a ModelForm keeps validation
    logic (max length on title, required fields, etc.) in sync with the
    model definition automatically.
    """

    class Meta:
        """Configuration linking the form to the Note model."""

        model = Note
        fields = ['title', 'content']
