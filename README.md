# 🏡 UrbanNest – Full‑Stack Property Listing Platform (Flask)

UrbanNest is a **modern, full‑stack real estate web application** built using **Python, Flask, SQLAlchemy, Jinja2, HTML, CSS, and JavaScript**. The platform enables users to **buy, sell, and rent properties**, with role‑based access control, authentication, admin approval workflows, and a clean UI suitable for **2026‑level portfolio showcasing**.

This project is designed with **production‑grade architecture** and deployed live on **Render** using **Gunicorn**.

🔗 **Live Demo**: 
[![Live Website](https://img.shields.io/badge/Live%20Website-UrbanNest-success?style=for-the-badge&logo=google-chrome&logoColor=white)](https://urbannest-m1ix.onrender.com)

<br> [https://urbannest-m1ix.onrender.com](https://urbannest-m1ix.onrender.com)
---

## 🚀 Key Features

### 🔐 Authentication & Authorization

* User registration and login
* Secure password hashing
* Session‑based authentication using **Flask‑Login**
* Role‑based access (User / Admin)

### 🏘️ Property Management

* Add, edit, delete property listings
* Upload and manage property images
* Property categories: Buy / Sell / Rent
* Admin approval system before public visibility
* Latest approved properties on home page

### 🧑‍💼 Admin Dashboard

* View all users
* Approve or reject properties
* Manage platform content securely

### 🎨 UI / UX

* Modern, clean, responsive layout
* Jinja2 templating with reusable components
* User‑friendly navigation and forms
* Optimized for recruiters and portfolio viewers

### ⚙️ Backend Architecture

* Flask **Application Factory Pattern**
* Blueprint‑based modular routing
* SQLAlchemy ORM
* WTForms with validation
* Secure configuration management

### ☁️ Deployment

* Production server: **Gunicorn**
* Hosting: **Render (Free Tier)**
* Environment‑based configuration

---

## 🗂️ Project Folder Structure

```text
UrbanNest_Flask/
│
├── app/
│   ├── __init__.py          # App factory & extension initialization
│   ├── models.py            # Database models
│   ├── runtime.txt          # Python runtime for deployment
│   │
│   ├── auth/                # Authentication blueprint
│   │   ├── routes.py
│   │   └── forms.py
│   │
│   ├── main/                # Main site routes
│   │   └── routes.py
│   │
│   ├── admin/               # Admin dashboard
│   │   └── routes.py
│   │
│   ├── property/            # Property management
│   │   ├── routes.py
│   │   └── forms.py
│   │
│   ├── templates/           # Jinja2 templates
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── property/
│   │   └── admin/
│   │
│   ├── static/              # Static assets
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│
├── instance/
│   └── urbannest.db         # SQLite database (local/demo)
│
├── config.py                # App configuration
├── requirements.txt         # Dependencies
├── run.py                   # Entry point
├── .gitignore
└── README.md
```

---

## 🧠 Core Files & Their Responsibilities

### 🔹 `run.py`

```python
from app import create_app
app = create_app()
```

* Entry point for Gunicorn and local development
* Ensures compatibility with production WSGI servers

---

### 🔹 `app/__init__.py`

**Responsibilities:**

* Application factory pattern
* Initialize extensions (SQLAlchemy, LoginManager)
* Register blueprints

**Key Method:**

* `create_app()` → returns Flask app instance

---

### 🔹 `config.py`

Manages environment‑specific configuration:

* SECRET_KEY
* DATABASE_URI
* DEBUG flag
* Upload folder paths

---

### 🔹 `models.py`

Defines database schema using SQLAlchemy ORM.

**Main Models:**

* `User`

  * id
  * username
  * email
  * password_hash
  * role

* `Property`

  * id
  * title
  * description
  * price
  * category
  * image
  * approved
  * user_id (FK)

---

## 🔐 Authentication Module (`auth/`)

### `auth/routes.py`

Handles:

* User registration
* User login
* Logout

Uses:

* Flask‑Login
* Secure redirects

### `auth/forms.py`

WTForms for:

* LoginForm
* RegisterForm

Includes:

* Field validation
* Email verification

---

## 🏠 Main Module (`main/`)

### `main/routes.py`

* Home page
* Displays latest **approved properties only**

```python
Property.query.filter_by(approved=True).limit(5)
```

---

## 🏘️ Property Module (`property/`)

### `property/routes.py`

Features:

* Add property
* Edit property
* Delete property
* Property detail page

Security:

* Login required
* Ownership checks

### `property/forms.py`

* PropertyForm
* Image validation

---

## 🧑‍💼 Admin Module (`admin/`)

### `admin/routes.py`

Admin‑only features:

* View all properties
* Approve / reject listings
* View users

Access restricted via role checks

---

## 🎨 Templates & UI

* `base.html` → global layout
* Block inheritance using Jinja2
* Modular components for navbar & footer

---

## ⚙️ Tech Stack

| Layer    | Technology    |
| -------- | ------------- |
| Backend  | Python, Flask |
| ORM      | SQLAlchemy    |
| Auth     | Flask‑Login   |
| Forms    | Flask‑WTF     |
| Frontend | HTML, CSS, JS |
| Server   | Gunicorn      |
| Hosting  | Render        |
| Database | SQLite (demo) |

---

## 📦 Deployment Notes

* Free‑tier Render deployment
* Cold start delay expected
* Environment variables used for security

---

## 🎯 Why This Project Matters

This project demonstrates:

* Real‑world Flask architecture
* Secure authentication flows
* Full CRUD lifecycle
* Deployment readiness
* UI/UX sensibility
* Scalable design principles

Ideal for:

* Backend / Full‑Stack roles
* Python / Flask developer positions

---

## 📌 Future Enhancements

* PostgreSQL migration
* Advanced search & filters
* Map integration
* Payment gateway
* API versioning

---

## 👨‍💻 Author

**Sunil Prajapati**
M.Tech Graduate | Python & Flask Developer <br>
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Follow%20Me-blue?logo=linkedin&style=for-the-badge)](https://www.linkedin.com/in/sunil-prajapati832)

---

⭐ If you find this project valuable, feel free to star the repository and connect!
