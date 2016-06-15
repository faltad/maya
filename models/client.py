from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship

from request import Request

from . import Base


class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True)
    ip = Column(String(45))

    requests = relationship("Request", order_by=Request.id, back_populates="client")