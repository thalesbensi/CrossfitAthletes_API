from sqlalchemy import Integer, Column, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from src.api.core.database.core import Base


class Athlete(Base):
    __tablename__ = "athletes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False,)
    cpf = Column(String(11), nullable=False)
    age = Column(Integer, nullable=False)
    weight = Column(Float, nullable=False)
    height = Column(Float, nullable=False)
    gender = Column(String(1), nullable=False)
    created_at = Column(DateTime, nullable=False)
    category_id = Column(ForeignKey("categories.id", onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    training_center_id = Column(ForeignKey("training_centers.id", onupdate="CASCADE", ondelete="CASCADE"))

    training_center = relationship("TrainingCenter", back_populates="athletes")
    category = relationship("Category", back_populates="athletes")