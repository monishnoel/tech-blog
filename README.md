# Tech Blog & CMS - Complete Project Setup

A production-ready **Personal Tech Blog & CMS** built with Python Flask, MySQL, HTML/CSS, GitHub, and CI/CD automation for live deployment on Render.

## ✨ Features

### 🔧 Core Features
- **Blog Engine**: Create, edit, and publish blog posts with Markdown support
- **CMS Dashboard**: Admin panel for managing posts and comments
- **User Management**: Registration, authentication, and role-based access
- **Comment System**: Readers can leave comments (moderation required)
- **Search Functionality**: Full-text search across blog posts
- **Categories & Tags**: Organize posts with categories and tags
- **View Counter**: Track post popularity

### 🚀 Deployment & DevOps
- **Docker Containerization**: Multi-stage Dockerfile for optimal image size
- **GitHub Actions CI/CD**: Automated testing and deployment pipeline
- **Render Integration**: One-click deployment to Render
- **MySQL Database**: Cloud-ready MySQL configuration
- **Environment Management**: Secure configuration with .env files

### 🎨 Frontend
- **Responsive Design**: Mobile-first CSS framework
- **Modern UI**: Professional design with smooth animations
- **Live Search**: Real-time post search with results dropdown
- **Dark-optimized Colors**: Eye-friendly color palette

---

## 📋 Project Structure

```
tech-blog-cms/
├── app/
│   ├── __init__.py              # Flask app factory
│   ├── models.py                # Database models (User, Post, Comment)
│   ├── routes.py                # All route handlers
│   ├── templates/               # HTML templates
│   │   ├── base.html            # Base template
│   │   ├── index.html           # Home page
│   │   ├── post.html            # Single post view
│   │   ├── login.html           # Login page
│   │   ├── register.html        # Registration page
│   │   ├── about.html           # About page
│   │   ├── category.html        # Category view
│   │   └── admin/               # Admin templates
│   │       ├── dashboard.html
│   │       ├── manage_posts.html
│   │       ├── new_post.html
│   │       ├── edit_post.html
│   │       └── manage_comments.html
│   └── static/
│       ├── css/                 # Stylesheets
│       │   └── style.css
│       ├── js/                  # JavaScript
│       │   └── main.js
│       └── img/                 # Images
├── migrations/                  # Database migrations
├── .github/
│   └── workflows/               # GitHub Actions
│       ├── deploy.yml           # Deployment pipeline
│       └── tests.yml            # Test pipeline
├── .env.example                 # Environment variables template
├── .gitignore                   # Git ignore file
├── Dockerfile                   # Docker configuration
├── Procfile                     # Render deployment config
├── render.yaml                  # Render YAML config
├── requirements.txt             # Python dependencies
├── run.py                       # Application entry point
└── README.md                    # This file
```

---

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.11+
- MySQL 8.0+
- Git
- Docker (optional, for containerized deployment)

### Local Development Setup

#### 1. Clone the Repository
```bash
cd tech-blog-cms
```

#### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Configure Environment Variables

**Option A: Using Railway (Recommended for Production)**
1. Create a MySQL database on [Railway.app](https://railway.app)
2. Copy your database credentials from the Railway dashboard
3. Create `.env` file:
```bash
DB_HOST=your-railway-host.proxy.rlwy.net
DB_USER=root
DB_PASSWORD=your-password
DB_NAME=railway
DB_PORT=your-port
SECRET_KEY=generate-a-secure-random-key
```

**Option B: Using Local MySQL**
```bash
# Create .env file
cp .env.example .env

# Edit with your local MySQL settings:
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your-password
DB_NAME=tech_blog_db
DB_PORT=3306
SECRET_KEY=generate-a-secure-random-key
```

#### 5. Create & Initialize Database

**If using Railway (database already created):**
```bash
python seed_db.py  # Populate with sample data (optional)
```

**If using local MySQL:**
```bash
# Create database
mysql -u root -p
> CREATE DATABASE tech_blog_db;
> EXIT;

# Initialize tables
python seed_db.py
```

#### 6. Run Application
```bash
python run.py
```

Visit `http://localhost:5000` in your browser.

### Default Credentials (After Setup)
- **Username**: `admin` (set in .env as `ADMIN_USERNAME`)
- **Password**: (set in .env as `ADMIN_PASSWORD`)
- **Admin Dashboard**: http://localhost:5000/admin

---

## 📱 Using the Application

### As a Reader
1. Browse published blog posts on the home page
2. View full post content with Markdown rendering
3. Search for posts using the search bar
4. Filter posts by category
5. Leave comments on posts (requires registration & login)

### As an Admin
1. Login with admin credentials
2. Go to `/admin` to access the dashboard
3. **Create Posts**: Add new blog posts with Markdown support
4. **Manage Posts**: Edit or delete existing posts
5. **Manage Comments**: Approve or delete reader comments
6. **View Stats**: Monitor blog statistics

---

## 🗄️ Database Schema

### Users Table
```sql
- id (Primary Key)
- username (Unique)
- email (Unique)
- password_hash
- is_admin (Boolean)
- created_at
- updated_at
```

### Posts Table
```sql
- id (Primary Key)
- title
- slug (Unique)
- content (Text)
- excerpt
- author_id (Foreign Key -> Users)
- category
- tags
- featured_image
- is_published (Boolean)
- view_count
- created_at
- updated_at
```

### Comments Table
```sql
- id (Primary Key)
- content (Text)
- author_id (Foreign Key -> Users)
- post_id (Foreign Key -> Posts)
- is_approved (Boolean)
- created_at
- updated_at
```

---

## 🔐 Authentication & Authorization

- **User Registration**: Public registration available
- **Login**: Session-based authentication
- **Admin Access**: Role-based access control (is_admin flag)
- **Post Management**: Only admins can create/edit posts
- **Comments**: Only registered users can comment

---

## 🚀 Deployment to Render

### Step 1: Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit: Tech Blog CMS"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/tech-blog-cms.git
git push -u origin main
```

### Step 2: Set Up MySQL Database

**Option A: Use Railway (Recommended)**
1. Go to [https://railway.app](https://railway.app)
2. Create a new MySQL plugin
3. Copy connection details from Railway dashboard
4. Note: `DB_HOST`, `DB_USER`, `DB_PASSWORD`, `DB_NAME`, `DB_PORT`

**Option B: Use Other Services**
- AWS RDS, PlanetScale, Aiven, or another managed MySQL service
- Ensure public network access is enabled for cloud deployment

### Step 3: Create Render Service
1. Go to [https://render.com](https://render.com)
2. Sign up with GitHub account
3. Create a new web service
4. Connect your GitHub repository

### Step 4: Configure Render Service
1. **Name**: tech-blog-cms
2. **Repository**: Select your GitHub repository
3. **Branch**: main
4. **Docker**: Enable Docker
5. **Environment Variables** (add all from your `.env`):
   - `FLASK_ENV=production`
   - `SECRET_KEY=<your-secure-key>`
   - `DB_HOST=<railway-or-db-host>`
   - `DB_USER=<db-user>`
   - `DB_PASSWORD=<db-password>`
   - `DB_NAME=<database-name>`
   - `DB_PORT=<port>`
   - `ADMIN_USERNAME=admin`
   - `ADMIN_PASSWORD=<secure-password>`

### Step 5: Deploy
1. Click **Deploy** on Render
2. Wait for build and deployment to complete
3. Your app will be live at `https://your-service-name.onrender.com`

### Post-Deployment
1. Seed database with initial data (if not auto-populated):
   ```bash
   # Optionally run via SSH or manually create admin user in MySQL
   ```
2. Login with credentials from `ADMIN_USERNAME` and `ADMIN_PASSWORD`

---

## 🔄 CI/CD Pipeline

The project includes automated GitHub Actions workflows:

### `.github/workflows/deploy.yml`
- **Trigger**: Push to main branch
- **Steps**:
  1. Check out code
  2. Set up Python 3.11
  3. Install dependencies
  4. Run linting (flake8)
  5. Build Docker image
  6. Push to GitHub Container Registry
  7. Deploy to Render via webhook

### `.github/workflows/tests.yml`
- **Trigger**: Push to main/develop branches
- **Steps**:
  1. Set up test environment
  2. Start MySQL service
  3. Install dependencies
  4. Run pytest tests
  5. Generate coverage reports
  6. Upload to Codecov

---

## 📝 API Endpoints

### Public Endpoints
- `GET /` - Home page
- `GET /post/<slug>` - View single post
- `GET /category/<category>` - View posts by category
- `GET /about` - About page
- `GET /api/posts/search?q=<query>` - Search posts
- `GET /api/stats` - Blog statistics

### Authentication
- `POST /auth/register` - Register new user
- `POST /auth/login` - Login user
- `GET /auth/logout` - Logout user

### Admin (Requires Login + is_admin=True)
- `GET /admin` - Dashboard
- `GET /admin/posts` - Manage posts
- `GET /admin/post/new` - Create new post
- `POST /admin/post/new` - Submit new post
- `GET /admin/post/<id>/edit` - Edit post
- `POST /admin/post/<id>/edit` - Submit edit
- `POST /admin/post/<id>/delete` - Delete post
- `GET /admin/comments` - Manage comments
- `POST /admin/comment/<id>/approve` - Approve comment
- `POST /admin/comment/<id>/delete` - Delete comment

### Comments API
- `POST /api/post/<id>/comment` - Add comment (requires login)

---

## 🌐 Environment Variables

Create a `.env` file based on `.env.example`:

```env
# Flask Configuration
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your_secret_key_here_change_in_production

# Database Configuration
DB_HOST=localhost
DB_USER=blog_user
DB_PASSWORD=your_password_here
DB_NAME=tech_blog_db
DB_PORT=3306

# Admin User (initial setup)
ADMIN_USERNAME=admin
ADMIN_EMAIL=admin@techblog.com
ADMIN_PASSWORD=secure_password_here

# Application Settings
POSTS_PER_PAGE=10
MAX_CONTENT_LENGTH=16777216

# Render/Production
RENDER_EXTERNAL_URL=https://your-render-app.onrender.com
```

---

## 🐳 Docker Usage

### Build Image
```bash
docker build -t tech-blog-cms:latest .
```

### Run Container
```bash
docker run -p 5000:5000 \
  -e DB_HOST=mysql.example.com \
  -e DB_USER=blog_user \
  -e DB_PASSWORD=password \
  -e DB_NAME=tech_blog_db \
  -e SECRET_KEY=your_secret_key \
  tech-blog-cms:latest
```

---

## ✅ Testing

### Run Tests
```bash
pytest
```

### With Coverage
```bash
pytest --cov=app --cov-report=html
```

### Start MySQL Test Database
```bash
mysql -u root -p
> CREATE DATABASE test_tech_blog_db;
```

---

## 📊 Performance Optimization

### Database Optimization
- Indexes on `username`, `email`, `slug`, `created_at`
- Connection pooling with SQLAlchemy
- Pagination for post listings

### Caching
- Static file caching headers
- Browser caching for CSS/JS

### Frontend Optimization
- Minimal CSS (~15KB)
- Vanilla JavaScript (no dependencies)
- Responsive images

---

## 🔒 Security Features

- ✅ Password hashing with werkzeug
- ✅ CSRF protection with Flask-WTF
- ✅ Session-based authentication
- ✅ Admin role enforcement
- ✅ SQL injection prevention (using SQLAlchemy ORM)
- ✅ XSS protection with Jinja2 template escaping
- ✅ Secure cookies in production
- ✅ Environment variable protection

---

## 🐛 Troubleshooting

### Database Connection Error
```
Error: Can't connect to MySQL server
Solution: Check DB_HOST, DB_USER, DB_PASSWORD in .env
```

### Import Errors
```
ModuleNotFoundError: No module named 'flask'
Solution: Activate virtual environment and run: pip install -r requirements.txt
```

### Port Already in Use
```
Address already in use (:5000)
Solution: Change PORT in .env or use: python run.py --port 5001
```

### Template Not Found
```
jinja2.exceptions.TemplateNotFound: base.html
Solution: Make sure Flask is looking in the correct templates directory
```

---

## 📚 Useful Commands

```bash
# Activate virtual environment
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Initialize database
python run.py init-db

# Seed sample data
python run.py seed-db

# Run development server
python run.py

# Run tests
pytest

# Generate migration
flask db migrate -m "Description"

# Apply migration
flask db upgrade

# Interactive shell
flask shell
```

---

## 🚀 Deployment Checklist

- [ ] Create GitHub repository
- [ ] Push code to GitHub
- [ ] Sign up for Render account
- [ ] Create MySQL database (AWS RDS, PlanetScale, etc.)
- [ ] Create Render web service
- [ ] Configure environment variables
- [ ] Set up deployment webhook
- [ ] Test deployment pipeline
- [ ] Monitor application logs
- [ ] Set up custom domain (optional)
- [ ] Enable auto-deployments on push

---

## 📞 Support & Resources

### Documentation
- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Render Documentation](https://render.com/docs)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

### Useful Links
- [Markdown Guide](https://www.markdownguide.org/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)
- [Werkzeug Security](https://werkzeug.palletsprojects.com/en/2.3.x/security/)

---

## 📄 License

This project is open source and available under the MIT License.

---

## 🎯 Next Steps

1. **Customize** the design by modifying `app/static/css/style.css`
2. **Write** your first blog post in the admin panel
3. **Configure** your domain on Render
4. **Share** your blog with the world!

---

**Happy blogging! 🚀**

For issues or questions, refer to the troubleshooting section or check the documentation links above.
