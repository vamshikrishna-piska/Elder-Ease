# ElderEase

ElderEase is a backend-focused project built with **Django and Django REST Framework (DRF)** that helps elderly people manage daily tasks by connecting them with helpers. All APIs are tested via Postman — no frontend yet. This project demonstrates **role-based authentication, and secure CRUD operations**.

---

## Features

- **Custom User Roles:** Elder and Helper
- **Token-based Authentication:** Secure login and API access
- **Task Management:** 
  - Elders can create tasks
  - Helpers can claim tasks
  - Task status updates: `open → assigned → completed`
- **Backend-first:** APIs fully functional and tested via Postman
- **Mobile field included:** Track elder/helper contact

---

## Tech Stack

- Django
- Django REST Framework
- SQLite
- Token Authentication
- Postman (for testing APIs)

---

## API Workflow

1. **Register Elder/Helper:** `POST /api/register/`
2. **Login and obtain Token:** `POST /api-token-auth/`
3. **Create Task (Elder):** `POST /api/tasks/`
4. **List Tasks (Helper):** `GET /api/tasks/`
5. **Claim Task (Helper):** `PATCH /api/tasks/<task_id>/` → `assigned_to`
6. **Complete Task (Helper):** `PATCH /api/tasks/<task_id>/` → `status=completed`

---

## How to Run Locally

```bash
# Clone repo
git clone https://github.com/vamshikrishna-piska/Elder-Ease.git
cd Elderease

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Make migrations and migrate
python manage.py makemigrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Run server
python manage.py runserver
