from sqlalchemy import Column, Integer, String, MetaData, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from . import Base

class Request(Base):
    __tablename__ = "requests"

    id = Column(Integer, primary_key=True)
    route = Column(Text)
    time = Column(DateTime)
    post_data = Column(Text)
    headers = Column(Text)
    client_id = Column(Integer, ForeignKey('clients.id'))

    client = relationship("Client", back_populates="requests")
