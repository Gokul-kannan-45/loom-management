from database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

class Loom(Base):
    __tablename__ = 'loom'
    id = Column(Integer, primary_key = True, index = True)
    loomNo = Column(Integer)
    loomType = Column(String)
    tieUp = Column(String)
    productionType = Column(String)