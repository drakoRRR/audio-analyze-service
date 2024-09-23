from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from src.database import Base


call_categories = Table(
    'call_categories', Base.metadata,
    Column('call_id', ForeignKey('calls.id'), primary_key=True),
    Column('category_id', ForeignKey('categories.id'), primary_key=True)
)


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    points = Column(String)  # comma-separated points
    calls = relationship("Call", secondary=call_categories, back_populates="categories")


class Call(Base):
    __tablename__ = 'calls'

    id = Column(Integer, primary_key=True, index=True)
    audio_url = Column(String, unique=True)
    transcription = Column(String)
    name = Column(String, nullable=True)
    location = Column(String, nullable=True)
    emotional_tone = Column(String, nullable=True)
    categories = relationship("Category", secondary=call_categories, back_populates="calls")
