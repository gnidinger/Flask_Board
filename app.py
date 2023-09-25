from flask import Flask
from .controllers.auth_controller import auth_app
from .config.db_config import engine, Base
from .models.user_model import User

Base.metadata.create_all(engine)

app = Flask(__name__)

app.register_blueprint(auth_app, url_prefix="/api/auth")


@app.route("/")
def home():
    return "Hello, World!"


if __name__ == "__main__":
    app.run()
