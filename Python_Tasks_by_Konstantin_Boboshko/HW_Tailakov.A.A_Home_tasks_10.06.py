# Создание системы управления задачами
#
# 1) Создайте класс TaskManager с атрибутами для хранения задач и информации о пользователях.
#
# 2) Реализуйте методы в классе TaskManager, чтобы добавлять задачи, назначать задачи пользователям, помечать задачи
# как выполненные и отображать сведения о задачах.
#
# 3) Создайте класс User с атрибутами для информации о пользователе, такой как имя, адрес электронной почты и роль
# (например, администратор или обычный пользователь).
#
# 4) Реализуйте методы в классе User для создания учетных записей пользователей, обновления информации о пользователях
# и просмотра назначенных задач.
#
# 5) Примените соответствующие методы инкапсуляции для защиты конфиденциальной пользовательской информации и
# гарантируйте, что операции, связанные с задачами, могут выполняться только авторизованными пользователями.
#
# 6) Используйте наследование для создания специализированных пользовательских ролей с различными разрешениями и
# возможностями (например, администраторы могут назначать задачи, обычные пользователи могут только просматривать задачи).
#
# 7) Внедрите проверку данных, чтобы гарантировать, что назначения задач и пользовательские операции выполняются с
# допустимыми входными данными и ограничениями.

class Task:
    def __init__(self, task_id, title, description):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.is_completed = False

    def mark_as_completed(self):
        self.is_completed = True


class User:
    def __init__(self, username, email, role):
        self.username = username
        self.email = email
        self.role = role
        self.assigned_tasks = []

    def create_task(self, task_id, title, description):
        task = Task(task_id, title, description)
        return task

    def assign_task(self, task, user):
        if self.role == "admin":
            user.assigned_tasks.append(task)
            return True
        else:
            return False

    def view_assigned_tasks(self):
        return self.assigned_tasks


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.users = []

    def add_task(self, task):
        self.tasks.append(task)

    def create_user(self, username, email, role):
        user = User(username, email, role)
        self.users.append(user)
        return user

    def get_task_by_id(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None

    def get_user_by_username(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None


# Пример использования системы управления задачами

task_manager = TaskManager()

# Создание задач
task1 = Task(1, "Build a project plan", "Create a plan to complete the project")
task2 = Task(2, "Design the facade", "Create layouts and prototypes of the interface")
task_manager.add_task(task1)
task_manager.add_task(task2)

# Создание пользователей
admin_user = task_manager.create_user("admin", "admin@example.com", "admin")
user1 = task_manager.create_user("user1", "user1@example.com", "user")
user2 = task_manager.create_user("user2", "user2@example.com", "user")

# Назначение задачи пользователю
task_manager.get_user_by_username("admin").assign_task(task1, user1)
task_manager.get_user_by_username("admin").assign_task(task2, user2)

# Просмотр назначенных задач
assigned_tasks = task_manager.get_user_by_username("user1").view_assigned_tasks()
if assigned_tasks:
    print("Assigned tasks for user1:")
    for task in assigned_tasks:
        print(f"ID: {task.task_id}, Task: {task.title}")

# Пометка задачи как выполненной
task_manager.get_task_by_id(1).mark_as_completed()

# Вывод информации о задачах
for task in task_manager.tasks:
    print(f"ID: {task.task_id}, Task: {task.title}, Compleat: {task.is_completed}")
