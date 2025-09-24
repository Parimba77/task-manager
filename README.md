# Task Manager (Project of Veloz selective)

## 📌 Descrição
Task Management application made with Django, as part of the challenge of the Veloz selective. 
Allows you to create **Users**, **Projects** and **Tasks**, with authentication and simple interface in Bootstrap.

## 🛠️ Tecnologias
- Python 3.10+
- Django 5.x
- SQLite (Django default database)
- Bootstrap 5 (frontend)

## ⚙️ Instalação
```bash
git clone https://github.com/seu-usuario/taskmanager.git
cd taskmanager
python -m venv venv
source venv/bin/activate  # Linux
venv\Scripts\activate     # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
