from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from src.api.core.database.core import Base


class TrainingCenter(Base):
    __tablename__ = "training_centers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    owner = Column(String(20), nullable=False)

    athletes = relationship("Athlete", back_populates="category")