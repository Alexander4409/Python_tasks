from jinja2 import Environment, FileSystemLoader

products = [
    {"name": "Avocado", "price": 15},
    {"name": "Banana", "price": 8},
    {"name": "Lemon", "price": 5},
    {"name": "Apples", "price": 10},
    {"name": "Shrimps", "price": 30},
    {"name": "Pineapple", "price": 20},
]

env = Environment(loader=FileSystemLoader("template"))
tm = env.get_template("List_products.html")
msg = tm.render(products=products)
print(msg)