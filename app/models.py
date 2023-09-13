from .database import Base
from sqlalchemy import  Column, String
from sqlalchemy.sql import func
from fastapi_utils.guid_type import GUID, GUID_DEFAULT_SQLITE


class Person(Base):
    __tablename__ = "person"
    id = Column(GUID, primary_key=True, default=GUID_DEFAULT_SQLITE)
    name = Column(String, nullable=False)
    # surname = Column(String, nullable=False)
    # email = Column(String, nullable=True)
    
