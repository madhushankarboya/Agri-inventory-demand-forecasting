from app import create_app
from app.models import db, User
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    existing = User.query.filter_by(role="Super Admin").first()

    if not existing:
        user = User(
            username="superadmin",
            email="admin@gov.in",
            password=generate_password_hash("admin123"),
            role="Super Admin",
            approved=True
        )
        db.session.add(user)
        db.session.commit()
        print("Super Admin created ✅")
    else:
        print("Super Admin already exists ⚠️")
