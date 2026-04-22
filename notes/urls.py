"""URL routing for the notes app.

Each entry in ``urlpatterns`` maps a URL fragment to a view function.
The ``name`` argument lets templates and views refer to a URL by name
(e.g. ``{% url 'note_detail' pk=note.pk %}``) rather than hard-coding
the path, which keeps things flexible if the URL ever changes.
"""

from django.urls import path

from .views import (
    note_create,
    note_delete,
    note_detail,
    note_list,
    note_update,
)


urlpatterns = [
    # Home page: list of every note.
    path('', note_list, name='note_list'),

    # Detail page for a single note (pk is its database primary key).
    path('note/<int:pk>/', note_detail, name='note_detail'),

    # Form to create a new note.
    path('note/new/', note_create, name='note_create'),

    # Form to edit an existing note.
    path('note/<int:pk>/edit/', note_update, name='note_update'),

    # Endpoint to delete a note.
    path('note/<int:pk>/delete/', note_delete, name='note_delete'),
]
