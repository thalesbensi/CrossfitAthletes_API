from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from src.api.core.database.core import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

    athletes = relationship("Athlete", back_populates="category")