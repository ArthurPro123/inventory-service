import os

class Config:

    DB_NAME = os.getenv("DB_NAME", "app.db")
    DB_USER = os.getenv("DB_USER", "")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "")

    if DB_HOST in ["db"]:
        SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    else:

        # Use SQLite:
        SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.abspath(DB_NAME)}"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
