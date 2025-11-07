class Config:
    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://root:secretRootPwd@localhost:3307/inventory_db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
