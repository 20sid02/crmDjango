
# Django CRM with PostgreSQL

A simple **CRM web application** built using **Django**, **PostgreSQL**, and **Bootstrap**.  
The app supports user authentication and full CRUD (Create, Read, Update, Delete) functionality for managing customer records.  

---

## 🚀 Features
- User authentication (Login, Logout, Register)
- PostgreSQL database integration
- Manage customer records:
  - Add new records
  - View all records in a Bootstrap table
  - View individual records
  - Update existing records
  - Delete records
- Responsive Bootstrap frontend
- Version control with Git & GitHub

---

## 🛠️ Tech Stack
- **Backend:** Django 5.x
- **Database:** PostgreSQL
- **Frontend:** HTML, CSS, Bootstrap
- **Version Control:** Git, GitHub
- **Deployment Ready:** Docker support planned

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/django-crm.git
cd django-crm
```

### 2. Create & activate virtual environment
```bash
python -m venv venv
source venv/bin/activate     # On Linux/Mac
venv\Scripts\activate        # On Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure PostgreSQL
- Create a PostgreSQL database and update `settings.py` with your credentials:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'crm_db',
        'USER': 'postgres',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a superuser
```bash
python manage.py createsuperuser
```

### 7. Start the server
```bash
python manage.py runserver
```

Now open `http://127.0.0.1:8000/` in your browser 🚀

---

## 📸 Screenshots
- Dashboard with records
- Login/Register pages
- Bootstrap-styled tables & cards

---

## 📌 Future Enhancements
- Dockerize the app for deployment
- Add search & filter functionality
- Role-based access (admin/user)
- Deploy on AWS/DigitalOcean/Heroku

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first.

---