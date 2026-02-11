# 📝 Lewins' Django Blog Project

![Django](https://img.shields.io/badge/Django-4.2-green)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blueviolet)
![License](https://img.shields.io/badge/License-MIT-yellow)

A modern, responsive blog application built with Django featuring image uploads, PostgreSQL database, and a beautiful UI with interactive blog cards.

## ✨ Features

### 🌟 Core Features
- **📝 Blog Posts** - Create, read, and manage blog posts with rich content
- **🖼️ Image Uploads** - Upload and display blog images with automatic resizing
- **🎨 Responsive Design** - Mobile-friendly interface with modern styling
- **🔍 Interactive UI** - Toggle blog content visibility with smooth animations
- **⏰ Timestamps** - Automatic date and time tracking for posts

### 🛠️ Technical Features
- **🐘 PostgreSQL Database** - Robust database backend
- **📁 Media Management** - Efficient file upload and storage system
- **🔐 Admin Interface** - Full-featured Django admin panel
- **⚡ Fast Performance** - Optimized database queries and template rendering

## 🚀 Quick Start

### Prerequisites
- 🐍 Python 3.8+
- 🐘 PostgreSQL (or SQLite for development)
- 📦 pip (Python package manager)

### Installation Steps

1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/myBlog.git
cd myBlog
```

2. **Create Virtual Environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install Dependencies**
```bash
pip install django pillow psycopg2-binary
```

4. **Database Setup**
```bash
# Create PostgreSQL database (if using PostgreSQL)
createdb lewins_blog_db

# Or use SQLite (edit settings.py to use SQLite)
# Update DATABASES configuration in settings.py
```

5. **Configure Environment**
```bash
# Copy and edit settings if needed
cp blog/settings.py blog/local_settings.py
# Update DATABASES, SECRET_KEY, etc.
```

6. **Run Migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

7. **Create Superuser**
```bash
python manage.py createsuperuser
```

8. **Create Media Directory**
```bash
mkdir media
mkdir media/blog_images
```

9. **Run Development Server**
```bash
python manage.py runserver
```

10. **Access the Application**
- 🌐 Blog: http://localhost:8000
- ⚙️ Admin: http://localhost:8000/admin

## 📁 Project Structure

```
myBlog/
├── 📁 blog/                    # Project main directory
│   ├── 📄 settings.py         # Project configuration
│   ├── 📄 urls.py            # Main URL routing
│   └── 📄 wsgi.py            # WSGI configuration
├── 📁 posts/                  # Blog app directory
│   ├── 📁 migrations/        # Database migrations
│   ├── 📄 models.py          # Post model definition
│   ├── 📄 views.py           # View logic
│   ├── 📄 urls.py            # App URL routing
│   └── 📄 admin.py           # Admin configuration
├── 📁 templates/              # HTML templates
│   └── 📄 index.html         # Main blog page
├── 📁 media/                  # Uploaded media files
│   └── 📁 blog_images/       # Blog post images
├── 📄 manage.py              # Django management script
├── 📄 requirements.txt       # Python dependencies
└── 📄 README.md              # This file
```

## 🗄️ Database Models

### 📋 Post Model
```python
class Post(models.Model):
    title = models.CharField(max_length=200)      # Blog title
    content = models.TextField()                  # Blog content
    image = models.ImageField(upload_to='blog_images/')  # Featured image
    created_at = models.DateTimeField(auto_now_add=True) # Creation timestamp
```

## 🎨 UI Features

### 💅 Design Elements
- **Modern Card Layout** - Each blog post in a stylish card
- **Circular Images** - Rounded blog images with borders
- **Interactive Buttons** - Smooth toggle animations
- **Responsive Grid** - Adapts to all screen sizes
- **Custom Fonts** - Poppins font family for better readability

### 🎯 User Interface
```
┌─────────────────────────────────────────────┐
│  📸 [Circular Image]                        │
│                                             │
│  🏷️ Blog Title                             │
│  📅 Posted on Date at Time                  │
│  🔘 [View Blog Button]                      │
│                                             │
│  📝 (Toggled Content Here)                  │
└─────────────────────────────────────────────┘
```

## 🔧 Configuration

### Database Configuration
Choose either PostgreSQL or SQLite:

**PostgreSQL (Production)**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'lewins_blog_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

**SQLite (Development)**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### Media Settings
```python
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

## 🧪 Testing

Run the development server:
```bash
python manage.py runserver
```

Check for errors:
```bash
python manage.py check
```

Test database:
```bash
python manage.py test
```

## 📊 Admin Features

Access the admin panel at `/admin` to:
- 👥 Manage users and permissions
- 📝 Create/edit/delete blog posts
- 🖼️ Upload and manage images
- 🔍 Search and filter posts
- 📅 Sort by creation date

## 🐛 Troubleshooting

### Common Issues

1. **Database Connection Error**
   ```
   Solution: Check if PostgreSQL is running or switch to SQLite
   ```

2. **Pillow Not Installed**
   ```
   Solution: pip install pillow
   ```

3. **Media Files Not Displaying**
   ```
   Solution: Ensure DEBUG=True and MEDIA settings are correct
   ```

4. **Migration Errors**
   ```
   Solution: 
   python manage.py makemigrations posts
   python manage.py migrate
   ```

### Debug Commands
```bash
# Check project health
python manage.py check

# View URL patterns
python manage.py show_urls

# Create database backup
python manage.py dumpdata posts > backup.json

# Load database backup
python manage.py loaddata backup.json
```

## 🚀 Deployment

### Production Checklist
- [ ] Set `DEBUG = False`
- [ ] Update `ALLOWED_HOSTS`
- [ ] Set proper `SECRET_KEY`
- [ ] Configure database for production
- [ ] Set up static files collection
- [ ] Configure media file storage
- [ ] Set up SSL certificate
- [ ] Configure web server (Nginx/Apache)

### Deployment Commands
```bash
# Collect static files
python manage.py collectstatic

# Apply migrations
python manage.py migrate

# Start production server (example with gunicorn)
gunicorn blog.wsgi:application
```

## 🤝 Contributing

1. 🍴 Fork the repository
2. 🌿 Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit changes (`git commit -m 'Add AmazingFeature'`)
4. 📤 Push to branch (`git push origin feature/AmazingFeature`)
5. 🔀 Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Lewin**
- 🌐 GitHub: [@King-luiz](https://github.com/King-luiz)
- 📧 Email: mureithilewins@gmail.com 

## 🙏 Acknowledgments

- 🎨 Django Framework team
- 📖 Django documentation contributors
- 🎯 Community tutorials and resources
- 👥 All open-source contributors

---

### ⭐ Show Your Support
If you find this project helpful, please give it a star! ⭐

### 📈 Project Status
![Progress](https://img.shields.io/badge/Status-Active-brightgreen)
![Version](https://img.shields.io/badge/Version-1.0.0-orange)

---
<img width="1288" height="682" alt="image" src="https://github.com/user-attachments/assets/887b2c87-87c9-46e5-b4c9-f31cb6c771d7" />
<img width="1297" height="658" alt="image" src="https://github.com/user-attachments/assets/a79502fb-92c0-40bc-ac87-99bacecf59ad" />


**Happy Coding!** 🚀✨

---
*Last Updated: February 2026*
