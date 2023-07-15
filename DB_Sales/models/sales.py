from sqlalchemy import Column, Integer, String, Float, ForeignKey
from .database import Base

# from sqlalchemy.orm import relationship


class Sale(Base):
    __tablename__ = 'sales'

    sales_id = Column(Integer, primary_key=True, autoincrement=True)
    salesman_id = Column(Integer, ForeignKey('salesmen.salesman_id'))
    customer_id = Column(Integer, ForeignKey('customers.customer_id'))
    amt = Column(Float)
    sales_date = Column(String)

    def __init__(self, sales_id: int, salesman_id: int, customer_id: int, amt: float, sales_date: str):
        self.sales_id = sales_id
        self.salesman_id = salesman_id
        self.customer_id = customer_id
        self.amt = amt
        self.sales_date = sales_date

    def __str__(self):
        return f'ID товара: {self.sales_id}, ' \
               f'ID покупателя: {self.customer_id}, ' \
               f'ID продавца: {self.salesman_id}, ' \
               f'Сумма заказа: {self.amt}, ' \
               f'Дата заказа: {self.sales_date}'
