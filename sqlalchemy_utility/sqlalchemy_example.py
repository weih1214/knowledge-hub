from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, text, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('mysql://root:Fosmu_19921214@localhost/staff', echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()



class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    fullname = Column(String(100))
    password = Column(String(100), default='password')

    # relationship should be established when defining class, though latter declaration is also valid
    # addresses = relationship('Address', order_by='Address.id', back_populates='user')

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)


class Address(Base):

    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    email_address = Column(String(100), server_default='server_default@gmail.com', nullable=False)

    # relationship can be established with no foreign-key constraints
    user = relationship('User', foreign_keys=[id], primaryjoin='User.id == Address.id')

    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address



def create_table_func():

    Base.metadata.create_all()


def operate_session(ORM_obj, ORM_obj_list):

    session = Session()
    session.autoflush = False # Default: True
    session.add(ORM_obj)
    session.add_all(ORM_obj_list)
    session.flush()
    # After flush(), auto-generated identifier and server-default will be available on ORM_obj
    session.commit()

