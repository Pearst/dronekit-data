from database import Base
from sqlalchemy import Column, Integer, String, Boolean, ColumnDefault

class Todos(Base):
    __tablename__='todos'


    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)


class data(Base):
    __tablename__='datas'

    function = Column(String)
    value = Column(ColumnDefault)
