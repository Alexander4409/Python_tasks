from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("template"))
tm = env.get_template("main.html")
content_h1 = "Page with homework"
content_p = "Homework is done!"
msg = tm.render(content_h1 = content_h1, content_p = content_p)
print(msg)