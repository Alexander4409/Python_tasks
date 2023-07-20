from jinja2 import Environment, FileSystemLoader


persons = [
    {"name": "John Doe", "email": "johndoe@gmail.com"},
    {"name": "Jane Smith", "email": "janesmith@yahoo.com"},
    {"name": "Mike Johnson", "email": "mikejohnson@gmail.com"}
]


env = Environment(loader=FileSystemLoader("template"))
tm = env.get_template("List_persons.html")
msg = tm.render(persons=persons)
print(msg)


