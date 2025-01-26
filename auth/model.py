from sqlalchemy import Column, Integer, String, Boolean, create_engine, ARRAY
from sqlalchemy.orm import sessionmaker, declarative_base
import os

DATABASE_URL = f"postgresql://{os.getenv('POSTGRES_USERNAME', 'dockeruser')}:{os.getenv('POSTGRES_PASSWORD', 'password')}@{os.getenv('POSTGRES_IP', 'localhost')}:{os.getenv('POSTGRES_PORT', '5432')}/{os.getenv('POSTGRES_DB_NAME', 'auth_service')}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    roles = Column(ARRAY(String), nullable=False)

# Roles not implemented for now. Using config file
# class Role(Base):
#     __tablename__ = "roles"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, unique=True, nullable=False)
#     description = Column(String)
#
#     users = relationship("User", back_populates="role")