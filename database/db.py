from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# #connect to DB postgreSQL
# SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:123456@localhost:1432/rest_app"

#connect to DB SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
