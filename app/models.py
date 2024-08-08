from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, PickleType
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.types import UserDefinedType
from .database import Base


class TSVector(UserDefinedType):
    def get_col_spec(self):
        return "TSVECTOR"
    

class EngineResults(Base):
    __tablename__ = "supersift_engine"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    url = Column(String, nullable=False)
    content = Column(String, nullable=False)
    ts = Column(TSVector)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False, server_default=text('now()'))