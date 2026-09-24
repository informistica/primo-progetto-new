# primo-progetto-new

Django 5 greenfield rebuild of the course.

## Requisiti

- Python 3.10+
- pip

## Setup locale

```bash
# 1. Crea e attiva un virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 2. Installa le dipendenze
pip install --upgrade pip
pip install -r requirements.txt

# 3. Applica le migrazioni del database
python manage.py migrate

# 4. Avvia il server di sviluppo
python manage.py runserver
```

Apri poi http://localhost:8000/ nel browser.

## Comandi utili

```bash
python manage.py check            # controlli di sistema
python manage.py createsuperuser  # crea un utente amministratore
python manage.py makemigrations   # genera nuove migrazioni
```

## Stack

- Django 5.2.17
- SQLite (database di sviluppo)
- Pillow, django-crispy-forms, whitenoise
