import jwt
import bcrypt
from datetime import datetime, timedelta
from email_validator import validate_email, EmailNotValidError
from ..models.user_model import User
from ..config.db_config import Session

SECRET_KEY = "thisisthesecretkeyforpracticingflask"


def register_user(email, password, pass_repeat, nickname):
    if password != pass_repeat:
        raise ValueError("Password and repeat password must match.")

    session = Session()

    existing_user = session.query(User).filter_by(email=email).first()
    if existing_user:
        raise ValueError("Email already registered.")

    try:
        validate_email(email)
    except EmailNotValidError as e:
        raise ValueError(str(e))

    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    new_user = User(email=email, password=hashed_password.decode("utf-8"), nickname=nickname)
    session.add(new_user)
    session.commit()


def login_user(email, password):
    session = Session()

    user = session.query(User).filter_by(email=email).first()

    if user:
        if bcrypt.checkpw(password.encode("utf-8"), user.password.encode("utf-8")):
            expiration_time = datetime.utcnow() + timedelta(days=1)
            payload = {"email": user.email, "exp": expiration_time}
            token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

            return {"email": user.email, "token": token}
        else:
            raise ValueError("Incorrect Password")
    else:
        raise ValueError("User Not Found")
