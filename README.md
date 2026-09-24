# primo-progetto-new

Django 5 greenfield rebuild of the course.

## Stack

- Python 3.12
- Django 5.2 (`config` project, `core` app)
- SQLite (development database)

## Local development

```bash
# 1. Create a virtual environment and install dependencies
python3 -m venv .venv
./.venv/bin/pip install --upgrade pip
./.venv/bin/pip install -r requirements.txt

# 2. Apply database migrations
./.venv/bin/python manage.py migrate

# 3. Run the development server
./.venv/bin/python manage.py runserver 0.0.0.0:8000
```

Then open http://localhost:8000/ for the task board, or http://localhost:8000/admin/ for the Django admin.

## Useful commands

```bash
./.venv/bin/python manage.py test          # run the test suite
./.venv/bin/python manage.py createsuperuser  # create an admin user
./.venv/bin/python manage.py makemigrations   # create new migrations
```

## Configuration

Settings read the following environment variables (with development-friendly defaults):

| Variable | Default | Purpose |
| --- | --- | --- |
| `DJANGO_SECRET_KEY` | insecure dev key | Cryptographic signing key |
| `DJANGO_DEBUG` | `True` | Toggle debug mode |
| `DJANGO_ALLOWED_HOSTS` | `localhost,127.0.0.1,0.0.0.0` | Comma-separated allowed hosts |

## Cloud Agent environment

This repository is configured for Cursor Cloud Agents via `.cursor/environment.json`:

- **install** — installs `python3-venv`, creates `.venv`, and installs `requirements.txt`
- **start** — applies database migrations
- **terminals** — runs the Django development server on port 8000
