"""Unit tests for the notes app.

These tests exercise both the ``Note`` model and the five CRUD views
(list, detail, create, update, delete) using Django's built‑in
``TestCase`` class. Each ``TestCase`` runs inside its own transaction
against a temporary test database, so the tests never touch real data.

Run from the project root with::

    python manage.py test notes
"""

from django.test import TestCase
from django.urls import reverse

from .forms import NoteForm
from .models import Note


# ---------------------------------------------------------------------------
# Model tests
# ---------------------------------------------------------------------------
class NoteModelTest(TestCase):
    """Tests covering the ``Note`` model itself."""

    def setUp(self):
        """Create a single ``Note`` instance available to every test."""
        self.note = Note.objects.create(
            title="Test Note",
            content="This is a test note.",
        )

    def test_note_has_title(self):
        """The stored title should match what was passed in on creation."""
        note = Note.objects.get(id=self.note.id)
        self.assertEqual(note.title, "Test Note")

    def test_note_has_content(self):
        """The stored content should match what was passed in on creation."""
        note = Note.objects.get(id=self.note.id)
        self.assertEqual(note.content, "This is a test note.")

    def test_note_created_at_auto_set(self):
        """``created_at`` should be auto‑populated by Django on save."""
        self.assertIsNotNone(self.note.created_at)

    def test_note_str_returns_title(self):
        """``__str__`` should return the note's title for admin / shell display."""
        self.assertEqual(str(self.note), "Test Note")


# ---------------------------------------------------------------------------
# Form tests
# ---------------------------------------------------------------------------
class NoteFormTest(TestCase):
    """Tests covering the ``NoteForm`` ModelForm."""

    def test_form_valid_with_title_and_content(self):
        """A form with both title and content should validate."""
        form = NoteForm(data={"title": "Hello", "content": "World"})
        self.assertTrue(form.is_valid())

    def test_form_invalid_without_title(self):
        """Missing the required title field should fail validation."""
        form = NoteForm(data={"title": "", "content": "World"})
        self.assertFalse(form.is_valid())
        self.assertIn("title", form.errors)


# ---------------------------------------------------------------------------
# View tests
# ---------------------------------------------------------------------------
class NoteViewTest(TestCase):
    """Tests covering the five CRUD views in ``notes.views``."""

    def setUp(self):
        """Create a baseline note so list/detail/update/delete have something to act on."""
        self.note = Note.objects.create(
            title="Test Note",
            content="This is a test note.",
        )

    # -- Read ---------------------------------------------------------------
    def test_note_list_view(self):
        """The list view should return 200 and contain the test note's title."""
        response = self.client.get(reverse("note_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Note")

    def test_note_detail_view(self):
        """The detail view should return 200 and show both title and content."""
        response = self.client.get(
            reverse("note_detail", args=[str(self.note.id)])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Note")
        self.assertContains(response, "This is a test note.")

    # -- Create -------------------------------------------------------------
    def test_note_create_view_get(self):
        """GET on the create view should return a blank form (status 200)."""
        response = self.client.get(reverse("note_create"))
        self.assertEqual(response.status_code, 200)

    def test_note_create_view_post_creates_note(self):
        """POST with valid data should create a new note and redirect to the list."""
        response = self.client.post(
            reverse("note_create"),
            data={"title": "Brand New", "content": "Created via test."},
        )
        # 302 = redirect after successful save.
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Note.objects.filter(title="Brand New").exists())

    # -- Update -------------------------------------------------------------
    def test_note_update_view_get(self):
        """GET on the update view should pre‑fill the form (status 200)."""
        response = self.client.get(
            reverse("note_update", args=[str(self.note.id)])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Note")

    def test_note_update_view_post_updates_note(self):
        """POST with new data should overwrite the existing note's fields."""
        response = self.client.post(
            reverse("note_update", args=[str(self.note.id)]),
            data={"title": "Updated Title", "content": "Updated content."},
        )
        self.assertEqual(response.status_code, 302)
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, "Updated Title")
        self.assertEqual(self.note.content, "Updated content.")

    # -- Delete -------------------------------------------------------------
    def test_note_delete_view_get_shows_confirmation(self):
        """GET on the delete view should render the confirmation page (status 200)."""
        response = self.client.get(
            reverse("note_delete", args=[str(self.note.id)])
        )
        self.assertEqual(response.status_code, 200)

    def test_note_delete_view_post_deletes_note(self):
        """POST on the delete view should remove the note and redirect."""
        response = self.client.post(
            reverse("note_delete", args=[str(self.note.id)])
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Note.objects.filter(id=self.note.id).exists())
