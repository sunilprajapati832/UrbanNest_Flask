# 🏡 UrbanNest – Full‑Stack Property Listing Platform (Flask)

UrbanNest is a **modern, full‑stack real estate web application** built using **Python, Flask, SQLAlchemy, Jinja2, HTML, CSS, and JavaScript**. The platform enables users to **buy, sell, and rent properties**, with role‑based access control, authentication, admin approval workflows, and a clean UI suitable for **2026‑level portfolio showcasing**.
This project is designed with **production‑grade architecture** and deployed live on **Render** using **Gunicorn**.

🔗 **Live Demo**: <br>
[![Live Website](https://img.shields.io/badge/Live%20Website-UrbanNest-success?style=for-the-badge&logo=google-chrome&logoColor=white)](https://urbannest-m1ix.onrender.com)

## Application Preview
![Graph Preview](app/static/images/UrbanNestWebsite1.png)
![Graph Preview](app/static/images/UrbanNestWebsite2.png)
![Graph Preview](app/static/images/UrbanNestWebsite3.png)
![Graph Preview](app/static/images/UrbanNestWebsite4.png)

## 🚀 Key Features

| **🔐 Authentication & Authorization**      |**🏘️ Property Management**          |**🧑‍💼 Admin Dashboard**| **🎨 UI / UX**                  |**⚙️ Backend Architecture**         | **☁️ Deployment**       | 
|-------------------------------------------- | ---------------------------------- | -----------------------------------|----------------------|-----------------------------------|--------------------------|
|User registration and login |Add, edit, delete property listings |View all users(UnderProcess) |Modern, clean, responsive layout   |Flask **Application Factory Pattern**    | Production server: **Gunicorn** |
|Secure password hashing |Upload and manage property images |Approve or reject properties| Jinja2 templating with reusable components|Blueprint‑based modular routing|Hosting: **Render (Free Tier)**|
|Session‑based authentication using **Flask‑Login** |Property categories: Buy / Sell / Rent| Manage platform content securely |User‑friendly navigation and forms|SQLAlchemy ORM|Environment‑based configuration  |
|Role‑based access (User / Admin) |  Admin approval system before public visibility  |            |  Optimized for recruiters and portfolio viewers |   WTForms with validation| team_analysis_report.txt|
|                                 |   Latest approved properties on home page        |            |                                                 | Secure configuration management |             |


## 🗂️ Project Folder Structure

```text
UrbanNest_Flask/
│           
├───app
│   │   forms.py            
│   │   models.py           # Database models
│   │   __init__.py         # App factory & extension initialization
│   │   
│   ├───routes              
│   │   │───auth.py         # Authentication blueprint
│   │   │───main.py         # Main site routes
│   │   │───profile.py      # Admin dashboard
│   │   │───property.py     # Property management
│   │             
│   ├───static              # Static assets
│   │   ├───css
│   │   │       style.css
│   │   │       
│   │   ├───images
│   │   │       logo.png
│   │   │       
│   │   ├───js
│   │   │       location.js
│   │   │       
│   │   ├───profile_pics
│   │   │       default.png     
│   │   │       
│   │   └───uploads          
│   │           
│   ├───templates            # Jinja2 templates
│   │   ├───add_property.html
│   │   ├───base.html
│   │   ├───edit_profile.html
│   │   ├───home.html
│   │   ├───login.html
│   │   ├───profile.html
│   │   ├───property_detail.html
│   │   ├───property_list.html
│   │   ├───register.html
│   │   ├───unverified_properties.html
│   │   ├───update_property.html
│   │   ├───view_property.html
│   │   ├───errors
│   │   │   ├──403.html
│   │   │   ├──404.html
│   │   │   ├──405.html
│                      
│           
├───instance
│       ├───urbannest.db     # SQLite database (local/demo)
│ 
├── config.py                # App configuration
├── requirements.txt         # Dependencies
├── run.py                   # Entry point
├── runtime.txt              # Python runtime for deployment
├── .gitignore
└── README.md
```
---

## 🧠 Core Files & Their Responsibilities 

| **`run.py`** |**__init__.py`**   |**`config.py`**  | **`models.py`**  |**`auth.py`** | **`forms.py`**  |**`main.py`**   | **`property.py`**  |
|------------- | ---------------------- | ----------------|------------------|---------------------|----------------------|-----------------------|---------------------------|
|Entry point for Gunicorn and local development|Application factory pattern|Manages environment‑specific configuration:|Defines database schema using SQLAlchemy ORM.|Handles:User registration, User login, Logout|WTForms for: LoginForm, RegisterForm |Home page|Features: Add property, Edit property, Delete property, Property detail page|
|Ensures compatibility with production WSGI servers|Initialize extensions (SQLAlchemy, LoginManager)|* SECRET_KEY|* `User` :id, username, email, password_hash, role |Uses: Flask‑Login, Secure redirects|Includes: Field validation, Email verification |Displays latest **approved properties only**| Security: Login required, Ownership checks |
||Register blueprints|* DATABASE_URI|* `Property`: id, title, description, price, category, image, approved, user_id (FK)||* PropertyForm * Image validation|||
||`create_app()` → returns Flask app instance|* DEBUG flag||||||
|||* Upload folder paths||||||

### 🔹 `run.py`

```python
from app import create_app
app = create_app()
if __name__ == "__main__":
    app.run()
```

| **🎨 Templates & UI** |**📦 Deployment Notes**   |**🎯 Why This Project Matters**  | **📌 Future Enhancements**  |
|------------- | ---------------------- | ----------------|------------------|
|* `base.html` → global layout|* Free‑tier Render deployment|This project demonstrates:|* PostgreSQL migration|
|* Block inheritance using Jinja2|* Cold start delay expected|* Real‑world Flask architecture|* Advanced search & filters|
|* Modular components for navbar & footer|* Environment variables used for security|* Secure authentication flows|* Map integration|
|||* Full CRUD lifecycle|* Payment gateway|
|||* Deployment readiness|* API versioning|
|||* UI/UX sensibility||
|||* Scalable design principles||
|||Ideal for:||
|||* Backend / Full‑Stack roles||
|||* Python / Flask developer positions||

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

```text
📌 Important Note on Live Demo & Data Persistence

This project (UrbanNest) is deployed on Render Free Tier for demonstration purposes.

🔄 Why properties may not appear on the live site

The current live deployment uses:

Flask + SQLite

Render Free Web Service

Render’s free tier uses an ephemeral filesystem, which means:

Any locally stored files (including SQLite databases and uploaded images)

Are reset whenever the service sleeps, restarts, or redeploys

As a result:

Properties uploaded during one session may not persist

After inactivity or redeploy, the site may appear empty (fresh state)

⚠️ This is expected platform behavior, not a bug in the application.

🧩 Template & Reusability Statement

UrbanNest is intentionally designed as a clean, modular Flask template that can be reused and extended.

Anyone can:

Clone this repository

Configure their own database (SQLite with persistent disk or PostgreSQL)

Deploy it on any hosting platform

Customize UI, features, and workflows for personal or commercial use

This repository focuses on:

Architecture

Code quality

Feature completeness

UI/UX flow

rather than persistent demo data.

👀 How to Evaluate My Work

To properly review the project:

📸 Screenshots show the complete UI and workflows

🎥 Demo videos demonstrate:

Property upload

Authentication

Profile management

Property listing & detail views

🧠 Codebase demonstrates:

Flask app factory pattern

Blueprint-based routing

SQLAlchemy ORM usage

Authentication & authorization

Clean separation of concerns

👉 Please use the screenshots, videos, and source code in this repository as the primary evaluation material.

🚀 For Full Persistence (Optional)

To run this project as a fully persistent production app:

Attach a persistent disk on Render or

Configure a PostgreSQL database

Detailed setup steps are documented in the repository.
```

## 👨‍💻 Author

**Sunil Prajapati**<br>
M.E. Graduate | Python & Flask Developer <br>
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Follow%20Me-blue?logo=linkedin&style=for-the-badge)](https://www.linkedin.com/in/sunil-prajapati832)

---

⭐ If you find this project valuable, feel free to star the repository and connect!
