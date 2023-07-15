from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base

from sqlalchemy.orm import relationship


class Customer(Base):
    __tablename__ = 'customers'

    customer_id = Column(Integer, primary_key=True, autoincrement=True)
    cust_name = Column(String)
    cust_city = Column(String)
    salesman_id = Column(Integer, ForeignKey('salesmen.salesman_id'))
    sales_id = relationship('Sale', backref='customers')

    def __init__(self, customer_id: int, cust_name: str, cust_city: str, salesman_id: int):
        self.customer_id = customer_id
        self.cust_name = cust_name
        self.cust_city = cust_city
        self.salesman_id = salesman_id

    def __str__(self):
        return f'Покупатель: {self.cust_name}, ' \
               f'Город: {self.cust_city}, ' \
               f'ID продавца: {self.salesman_id}'
