import os

class Config:

    if os.getenv('DB_HOST') == "db":

        # Use MariaDB
        SQLALCHEMY_DATABASE_URI = (
            f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@"
            f"{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
        )
    else:
        # Use SQLite
        SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.getenv('DB_NAME')}"


    SQLALCHEMY_TRACK_MODIFICATIONS = False
