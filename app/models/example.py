from sqlalchemy import Column, String, func, DateTime

from app.models.base import Base


class Example(Base):
    __tablename__ = "examples"

    id = Column(String(36), primary_key=True, nullable=False)
    test = Column(String(191), nullable=False)

    created_at = Column(DateTime, server_default=func.now(), nullable=True)
    updated_at = Column(DateTime, server_onupdate=func.now(), nullable=True)
    deleted_at = Column(DateTime, nullable=True)