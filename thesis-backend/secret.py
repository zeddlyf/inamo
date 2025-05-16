import secrets

flask_secret = secrets.token_urlsafe(32)
print(f"FLASK_SECRET_KEY={flask_secret}")
