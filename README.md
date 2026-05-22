# RBlog REST API

A clean, robust REST API for a simple blogging platform built using Python, Django, and Django REST Framework (DRF). Features stateless JWT authentication, automated OpenAPI documentation, and granular object-level access controls.

## Features
- **JWT Authentication:** Secure login and token refreshing using `djangorestframework-simplejwt`.
- **Granular Permissions:** Public read-only access for guests; modification rights strictly limited to content authors.
- **Automated API Docs:** Interactive endpoints visualization using Swagger UI and ReDoc via `drf-spectacular`.

---

## Getting Started

### Prerequisites
- Python 3.10+
- pip

### Installation & Setup

1. **Clone the repository:**
   git clone [https://github.com/Nonashi37/RBlog.git(https://github.com/Nonashi37/RBlog.git)
   cd RBlog

2. **Set up a virtual environment:**
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. **Install dependencies:**
pip install django djangorestframework djangorestframework-simplejwt drf-spectacular

4. **Run migrations:**
python manage.py migrate

5. **Create a superuser (Admin account):**
python manage.py createsuperuser

6. **Fire up the development server:**
python manage.py runserver