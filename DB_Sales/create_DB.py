from faker import Faker
from models.database import create_db, Session
from models.salesmen import Salesman
from models.sales import Sale
from models.customers import Customer

def create_database(load_fake_data=True):
    create_db()
    if load_fake_data:
        _load_fake_data(Session())

def _load_fake_data(session):
    fake = Faker()

    customer_id = [2001, 2002, 2003, 2004, 2006, 2007, 2008, 2009]
    cust_name = [fake.first_name() for _ in range(len(customer_id))]
    cust_city = [fake.city() for _ in range(len(customer_id))]
    salesman_id = [1001, 1003, 1002, 1002, 1001, 1004, 1007, 1000]

    for i in range(len(customer_id)):
        customer = Customer(customer_id=customer_id[i], cust_name=cust_name[i], cust_city=cust_city[i], salesman_id=salesman_id[i])
        session.add(customer)

    session.commit()

    sales_id = [3001, 3002, 3003, 3005, 3006, 3007, 3008, 3009, 3010, 3011, 3012]
    salesman_id = [1007, 1004, 1001, 1002, 1007, 1002, 1001, 1003, 1002, 1001, 1000]
    customer_id = [2008, 2007, 2001, 2003, 2008, 2004, 2006, 2002, 2004, 2006, 2009]
    amt = [fake.random_float(min=10, max=1000, precision=2) for _ in range(len(sales_id))]
    sales_date = [fake.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S') for _ in range(len(sales_id))]

    for i in range(len(sales_id)):
        sales = Sale(sales_id=sales_id[i], salesman_id=salesman_id[i], customer_id=customer_id[i], amt=amt[i], sales_date=sales_date[i])
        session.add(sales)

    session.commit()

    salesman_id = [1000, 1001, 1002, 1003, 1004, 1007]
    sls_name = [fake.first_name() for _ in range(len(salesman_id))]
    sls_city = [fake.city() for _ in range(len(salesman_id))]

    for i in range(len(salesman_id)):
        salesman = Salesman(salesman_id=salesman_id[i], sls_name=sls_name[i], sls_city=sls_city[i])
        session.add(salesman)

    session.commit()

if __name__ == '__main__':
    create_database()

