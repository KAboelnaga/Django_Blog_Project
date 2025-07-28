# 📝 Django Blog Platform

A complete blogging platform built with Django and Docker. It supports user authentication, blog categories, posts with images, email subscriptions, and admin management.

---

## 🚀 Features

- User registration and login
- Blog post CRUD (Create, Read, Update, Delete)
- Image upload for posts (stored in `/media`)
- Subscriptions via email
- Admin dashboard
- Dockerized setup for easy deployment

---

## 📦 Requirements

- Docker 🐳
- Docker Compose
- Git

---

## ⚙️ Project Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
Build and run the containers:

bash
Copy
Edit
docker-compose up --build
Apply migrations inside the container:

bash
Copy
Edit
docker-compose exec web python manage.py migrate
Create a superuser:

bash
Copy
Edit
docker-compose exec web python manage.py createsuperuser
🖼 Media Files
Uploaded images (e.g., post images) are saved in the media/ directory.

If you're cloning this project and don't see media files:

Ask the team for the media/ folder or

Comment out image-related parts to test without them

🔐 Environment Variables
Create a .env file in the root directory and set your email configuration:

env
Copy
Edit
EMAIL_HOST=smtp.mailtrap.io
EMAIL_HOST_USER=your_mailtrap_username
EMAIL_HOST_PASSWORD=your_mailtrap_password
EMAIL_PORT=587
DEFAULT_FROM_EMAIL=your_email@example.com
💡 Note: Gmail is no longer recommended due to authentication restrictions (SMTP error 535). Use Mailtrap or similar services for easier testing.

🧪 Testing
Run tests (if available) inside the container:

bash
Copy
Edit
docker-compose exec web python manage.py test
🛠 Useful Commands
bash
Copy
Edit
# Run shell inside container
docker-compose exec web python manage.py shell

# Collect static files
docker-compose exec web python manage.py collectstatic
📎 Project Structure (Simplified)
cpp
Copy
Edit
├── docker-compose.yml
├── Dockerfile
├── .env
├── requirements.txt
├── media/           ← uploaded images
├── static/          ← static assets
├── blog/            ← Django app
│   ├── models.py
│   ├── views.py
│   └── ...
└── manage.py
🙋 Author
Developed by Mostafa Bahaa.
Feel free to contribute or raise issues.

