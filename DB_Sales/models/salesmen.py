from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base

from sqlalchemy.orm import relationship


class Salesman(Base):
    __tablename__ = 'salesmen'

    salesman_id = Column(Integer, primary_key=True, autoincrement=True)
    sls_name = Column(String)
    sls_city = Column(String)
    sales_id = relationship('Sale', backref='salesmen')
    cust_id = relationship('Customer', backref='salesmen')

    def __init__(self, salesman_id: int, sls_name: str, sls_city: str):
        self.salesman_id = salesman_id
        self.sls_name = sls_name
        self.sls_city = sls_city

    def __str__(self):
        return f'Продавец: {self.sls_name}, ' \
               f'Город: {self.sls_city}, ' \
               f'ID продавца: {self.salesman_id}'
