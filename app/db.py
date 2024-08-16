from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from typing import Generator
import os

# URL підключення до бази даних
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:567234@localhost:5438/postgres")

# Створення двигуна для підключення до бази даних
engine = create_engine(DATABASE_URL, echo=True)

# Створення локального сеансу для роботи з базою даних
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовий клас для оголошення моделей
Base = declarative_base()

# Dependency для отримання сеансу бази даних
def get_db() -> Generator[SessionLocal, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
