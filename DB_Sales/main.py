
from models.customers import Customer
from models.sales import Sale
from models.salesmen import Salesman
from models.database import engine, Session
from models.database import Base

Base.metadata.create_all(engine)
session = Session()



def insert_sale():
    sale_date = input("Введите дату продажи (гггг-мм-дд): ")
    salesman_id = input("Введите ID продавца: ")
    customer_id = input("Введите ID покупателя: ")
    amount = input("Введите сумму продажи: ")

    sale = Sale(sale_date=sale_date, salesman_id=salesman_id, customer_id=customer_id, amount=amount)
    session.add(sale)
    session.commit()
    print("Данные успешно добавлены.")


def update_sale():
    sale_id = input("Введите ID сделки, которую необходимо обновить: ")
    new_amount = input("Введите новую сумму продажи: ")

    sale = session.query(Sale).get(sale_id)
    if sale:
        sale.amount = new_amount
        session.commit()
        print("Данные успешно обновлены.")
    else:
        print("Сделка с указанным ID не найдена.")


def delete_sale():
    sale_id = input("Введите ID сделки, которую необходимо удалить: ")

    sale = session.query(Sale).get(sale_id)
    if sale:
        session.delete(sale)
        session.commit()
        print("Данные успешно удалены.")
    else:
        print("Сделка с указанным ID не найдена.")


def display_results(query, params=None):
    if params:
        result = session.execute(query, params).fetchall()
    else:
        result = session.execute(query).fetchall()

    if result:
        for row in result:
            print(row)
    else:
        print("Нет данных.")


def menu():
    menu_options = [
        "Отображение всех сделок",
        "Отображение сделок конкретного продавца",
        "Отображение максимальной по сумме сделки",
        "Отображение минимальной по сумме сделки",
        "Отображение максимальной по сумме сделки для конкретного продавца",
        "Отображение минимальной по сумме сделки для конкретного продавца",
        "Отображение максимальной по сумме сделки для конкретного покупателя",
        "Отображение минимальной по сумме сделки для конкретного покупателя",
        "Отображение продавца с максимальной суммой продаж",
        "Отображение продавца с минимальной суммой продаж",
        "Отображение покупателя с максимальной суммой покупок",
        "Отображение средней суммы покупки для конкретного покупателя",
        "Отображение средней суммы покупки для конкретного продавца",
        "Добавить сделку",
        "Обновить сделку",
        "Удалить сделку",
        "Выход"
    ]

    while True:
        print("Меню:")
        for i, option in enumerate(menu_options):
            print(f"{i + 1}. {option}")

        choice = input("Введите номер отчета или операции (или 0 для выхода): ")

        if choice == "1":
            query = '''SELECT * FROM Sales'''
            display_results(query)
        elif choice == "2":
            salesman_id = input("Введите ID продавца: ")
            query = '''SELECT * FROM Sales WHERE salesman_id = ?'''
            params = (salesman_id,)
            display_results(query, params)
        elif choice == "3":
            query = '''SELECT MAX(amount) FROM Sales'''
            display_results(query)
        elif choice == "4":
            query = '''SELECT MIN(amount) FROM Sales'''
            display_results(query)
        elif choice == "5":
            salesman_id = input("Введите ID продавца: ")
            query = '''SELECT MAX(amount) FROM Sales WHERE salesman_id = ?'''
            params = (salesman_id,)
            display_results(query, params)
        elif choice == "6":
            salesman_id = input("Введите ID продавца: ")
            query = '''SELECT MIN(amount) FROM Sales WHERE salesman_id = ?'''
            params = (salesman_id,)
            display_results(query, params)
        elif choice == "7":
            customer_id = input("Введите ID покупателя: ")
            query = '''SELECT MAX(amount) FROM Sales WHERE customer_id = ?'''
            params = (customer_id,)
            display_results(query, params)
        elif choice == "8":
            customer_id = input("Введите ID покупателя: ")
            query = '''SELECT MIN(amount) FROM Sales WHERE customer_id = ?'''
            params = (customer_id,)
            display_results(query, params)
        elif choice == "9":
            query = '''SELECT Salesmen.id, Salesmen.name, SUM(Sales.amount) AS total_sales
                       FROM Salesmen
                       INNER JOIN Sales ON Salesmen.id = Sales.salesman_id
                       GROUP BY Salesmen.id, Salesmen.name
                       ORDER BY total_sales DESC
                       LIMIT 1'''
            display_results(query)
        elif choice == "10":
            query = '''SELECT Salesmen.id, Salesmen.name, SUM(Sales.amount) AS total_sales
                       FROM Salesmen
                       INNER JOIN Sales ON Salesmen.id = Sales.salesman_id
                       GROUP BY Salesmen.id, Salesmen.name
                       ORDER BY total_sales ASC
                       LIMIT 1'''
            display_results(query)
        elif choice == "11":
            query = '''SELECT Customers.id, Customers.name, SUM(Sales.amount) AS total_purchases
                       FROM Customers
                       INNER JOIN Sales ON Customers.id = Sales.customer_id
                       GROUP BY Customers.id, Customers.name
                       ORDER BY total_purchases DESC
                       LIMIT 1'''
            display_results(query)
        elif choice == "12":
            customer_id = input("Введите ID покупателя: ")
            query = '''SELECT AVG(amount) FROM Sales WHERE customer_id = ?'''
            params = (customer_id,)
            display_results(query, params)
        elif choice == "13":
            salesman_id = input("Введите ID продавца: ")
            query = '''SELECT AVG(amount) FROM Sales WHERE salesman_id = ?'''
            params = (salesman_id,)
            display_results(query, params)
        elif choice == "14":
            insert_sale()
        elif choice == "15":
            update_sale()
        elif choice == "16":
            delete_sale()
        elif choice == "0":
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите номер отчета или операции из меню.")

    session.close()


menu()
