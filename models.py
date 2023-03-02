from loader import Base
from loader import Integer,varchar,ForeignKey,Column,DateTime


#2-usul(declarative way)

class Category(Base):
    __tablename__ = 'category'
    
    category_id = Column(Integer,primary_key=True,nullable=0)
    name = Column(varchar(25),nullable=0)
    last_update = Column(DateTime,nullable=0)

    def __repr__(self):
        return f'{self.category_id}||{self.name}||{self.last_update}'