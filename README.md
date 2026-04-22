# Sticky Notes – Django Web Application (Part 2)

A simple Django web application that lets a user create, view, update and delete personal sticky notes. Built for HyperionDev module **M06T05 – Django – Sticky Notes Application Part 2**, which extends the Part 1 project with a full unit‑test suite.

---

## 1. Project Overview

Each sticky note has a **title**, a **content** body and an automatic **created‑at** timestamp. The application provides full CRUD functionality through a Django front‑end:

| URL | View | Purpose |
|---|---|---|
| `/` | `note_list` | List every note, newest first |
| `/note/<pk>/` | `note_detail` | Show a single note in full |
| `/note/new/` | `note_create` | Create a new note |
| `/note/<pk>/edit/` | `note_update` | Edit an existing note |
| `/note/<pk>/delete/` | `note_delete` | Delete a note (with confirmation) |
| `/admin/` | – | Django admin (after creating a superuser) |

The project follows the standard Django MVT (Model‑View‑Template) architecture, uses a `ModelForm` for input validation, ships with a small stylesheet served from `notes/static/`, and is fully covered by a unit‑test suite in `notes/tests.py`.

---

## 2. Folder Structure

```
M06T05_sticky_notes/             # ← outer wrapper folder (run commands here)
├── manage.py
├── requirements.txt
├── README.md
├── sticky_github.txt            # Link to the public GitHub repo
├── diagrams/                    # Use case, class and sequence diagrams (PNG)
│   ├── use_case_diagram.png
│   ├── class_diagram.png
│   └── sequence_diagram.png
├── sticky_notes/                # Django project package (settings, root URLs, WSGI/ASGI)
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── notes/                       # The actual notes app
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── models.py
    ├── tests.py                 # Unit tests (model + form + views)
    ├── urls.py
    ├── views.py
    ├── migrations/
    ├── static/notes/            # CSS / images
    └── templates/notes/         # HTML templates
```

---

## 3. Requirements

* Python **3.10+**
* pip
* Everything else is listed in `requirements.txt`:
  * `Django==4.2.29`

---

## 4. Setup & Installation

The instructions below assume a Unix‑like shell (macOS / Linux / WSL). Replace `python3`/`pip3` with `python`/`pip` on Windows.

### 4.1 Clone / unzip the project

```bash
unzip M06T05_sticky_notes.zip
cd M06T05_sticky_notes
```

> **Note on folder layout.** Inside `M06T05_sticky_notes/` there is also an inner folder called `sticky_notes/`. This is normal — it's the Django *project package* (settings, root URLs, WSGI/ASGI). Run every command in this README from the **outer** `M06T05_sticky_notes/` folder — the one that contains `manage.py` and `requirements.txt`. If a command complains about `requirements.txt` or `manage.py` not being found, you are one folder too deep; `cd ..` back up.

### 4.2 Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate          # macOS / Linux
# venv\Scripts\activate            # Windows
```

### 4.3 Install the dependencies

```bash
pip install -r requirements.txt
```

### 4.4 Apply the database migrations

This creates the SQLite database (`db.sqlite3`) and the `notes_note` table:

```bash
python manage.py migrate
```

### 4.5 (Optional) Create a superuser for the admin site

```bash
python manage.py createsuperuser
```

### 4.6 Run the development server

```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in a browser. The notes admin (if a superuser was created) lives at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).

---

## 5. Using the Application

1. Visit `/` – you will see the empty list and an **"Add Note"** button.
2. Click **Add Note**, fill in a title and some content, and click **Save**.
3. Click any note in the list to see its detail page.
4. From the detail page you can **Edit** or **Delete** the note. Deletion shows a confirmation page first.
5. Repeat as needed – every note is timestamped automatically.

---

## 6. Running the Unit Tests

The unit tests live in `notes/tests.py` and cover the `Note` model, the `NoteForm` ModelForm and all five CRUD views (list, detail, create, update, delete). Run them with:

```bash
python manage.py test notes
```

You should see something like::

```
Found 12 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
............
----------------------------------------------------------------------
Ran 12 tests in 0.1XXs

OK
Destroying test database for alias 'default'...
```

What the suite covers:

| Class | Tests | What it checks |
|---|---|---|
| `NoteModelTest` | 4 | Title, content and `created_at` are stored correctly; `__str__` returns the title. |
| `NoteFormTest` | 2 | Form validates with correct data and rejects a missing title. |
| `NoteViewTest` | 6 | All five CRUD views respond correctly (list, detail, create GET/POST, update GET/POST, delete GET/POST), including DB side‑effects. |

You can also do a quick sanity check at any time:

```bash
python manage.py check          # configuration check
python manage.py makemigrations # should report "No changes detected"
```

---

## 7. Diagrams

Three UML diagrams are included in the `diagrams/` folder:

| File | Purpose |
|---|---|
| `use_case_diagram.png` | Shows the User actor and the five CRUD use cases inside the Sticky Notes system boundary. |
| `class_diagram.png` | Shows `Note`, `NoteForm`, the `views` module, the URL configuration and the templates, plus their relationships. |
| `sequence_diagram.png` | Walks through the **Create Note** scenario from the user click to the `INSERT` statement and the `302` redirect. |

---

## 8. GitHub Link

The public GitHub repository for this project is recorded in `sticky_github.txt` at the project root, as required by the task brief.

---

## 9. Author

Submitted by **Deen Ali** for HyperionDev – Introduction to Software Engineering, module **M06T05**.
