"""View functions for the Sticky Notes application.

Each view handles one HTTP entry point. Together they implement the
full CRUD lifecycle (Create, Read, Update, Delete) for Note objects:

    - note_list:   list all notes (Read-many)
    - note_detail: show one note (Read-one)
    - note_create: create a new note (Create)
    - note_update: edit an existing note (Update)
    - note_delete: remove a note (Delete)

Views interact with the Note model and NoteForm form, then render an
HTML template (or redirect to another view) as the HTTP response.
"""

from django.shortcuts import get_object_or_404, redirect, render

from .forms import NoteForm
from .models import Note


def note_list(request):
    """Render the home page showing every note in the database.

    Args:
        request: The incoming HttpRequest object.

    Returns:
        HttpResponse rendered from the note_list.html template, with a
        context containing the queryset of notes and the page title.
    """
    notes = Note.objects.all()
    context = {
        'notes': notes,
        'page_title': 'List of Notes',
    }
    return render(request, 'notes/note_list.html', context)


def note_detail(request, pk):
    """Render the detail page for a single note.

    Args:
        request: The incoming HttpRequest object.
        pk: Primary key of the Note to display.

    Returns:
        HttpResponse rendered from note_detail.html, or a 404 response
        if no note with the given primary key exists.
    """
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'notes/note_detail.html', {'note': note})


def note_create(request):
    """Handle creation of a new note.

    On GET, displays a blank form. On POST, validates and saves the
    submitted form, then redirects back to the note list.

    Args:
        request: The incoming HttpRequest object.

    Returns:
        HttpResponse rendering the form template, or an HttpResponseRedirect
        to the note_list view on a successful save.
    """
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm()

    return render(request, 'notes/note_form.html', {'form': form})


def note_update(request, pk):
    """Handle editing of an existing note.

    On GET, displays the form pre-filled with the note's current values.
    On POST, validates and saves the changes, then redirects back to the
    note list.

    Args:
        request: The incoming HttpRequest object.
        pk: Primary key of the Note to update.

    Returns:
        HttpResponse rendering the form template, or an HttpResponseRedirect
        to the note_list view on a successful save. Returns 404 if the
        note does not exist.
    """
    note = get_object_or_404(Note, pk=pk)

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)

    return render(request, 'notes/note_form.html', {'form': form})


def note_delete(request, pk):
    """Delete the specified note and redirect to the note list.

    Args:
        request: The incoming HttpRequest object.
        pk: Primary key of the Note to delete.

    Returns:
        HttpResponseRedirect to the note_list view. Returns 404 if the
        note does not exist.
    """
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect('note_list')
