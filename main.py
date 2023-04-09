

EMPLOYEES_FILE = 'employees.txt'
# Функция для получения списка сотрудников из файла
def load_employees():
    employees = []
    with open(EMPLOYEES_FILE, mode='r') as file:
        for line in file:
            last_name, first_name, age, position, salary = line.strip().split(',')
            employees.append({
                'last_name': last_name,
                'first_name': first_name,
                'age': age,
                'position': position,
                'salary': salary
            })
    return employees
# Функция для сохранения списка сотрудников в файл
def save_employees(employees):
    with open(EMPLOYEES_FILE, mode='w') as file:
        for employee in employees:
            file.write(f"{employee['last_name']}, {employee['first_name']}, {employee['age']}, {employee['position']}, {employee['salary']}\n")
# Функция для добавления нового сотрудника в список
def add_employee(employees):
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    age = int(input('Введите возраст: '))
    position = input('Введите должность: ')
    salary = float(input('Введите зарплату: '))
    employee = {
        'last_name': last_name,
        'first_name': first_name,
        'age': age,
        'position': position,
        'salary': salary
    }
    employees.append(employee)
    return employees
# Функция для редактирования данных сотрудника
def edit_employee(employees):
    index = int(input('Введите номер сотрудника для редактирования: '))
    if index < len(employees):
        last_name = input('Введите фамилию: ')
        first_name = input('Введите имя: ')
        age = int(input('Введите возраст: '))
        position = input('Введите должность: ')
        salary = float(input('Введите зарплату: '))
        employee = {
            'last_name': last_name,
            'first_name': first_name,
            'age': age,
            'position': position,
            'salary': salary
        }
        employees[index] = employee
        return employees
    else:
        print('Введенный номер сотрудника некорректен')
        return employees
# Функция для удаления сотрудника из списка
def delete_employee(employees):
    index = int(input('Введите номер сотрудника для удаления: '))
    if index < len(employees):
        del employees[index]
    else:
        print('Некорректный номер сотрудника')
    return employees
# Функция для поиска сотрудника по фамилии
def search_by_last_name(employees):
    last_name = input('Введите фамилию для поиска: ')
    results = []
    for employee in employees:
        if employee['last_name'] == last_name:
            results.append(employee)
    return results
# Функция для поиска сотрудника по возрасту
def search_by_age(employees):
    age = int(input('Введите возраст для поиска: '))
    results = []
    for employee in employees:
        if employee['age'] == age:
            results.append(employee)
    return results
# Функция для поиска сотрудника по первой букве фамилии
def search_by_first_letter(employees):
    letter = input('Введите первую букву фамилии для поиска: ')
    results = []
    for employee in employees:
        if employee['last_name'].startswith(letter):
            results.append(employee)
    return results
# Главная функция

def main():
    employees = load_employees()
    while True:
        print('1. Вывести список сотрудников')
        print('2. Добавить сотрудника')
        print('3. Редактировать сотрудника')
        print('4. Удалить сотрудника')
        print('5. Поиск по фамилии')
        print('6. Поиск по возрасту')
        print('7. Поиск по первой букве фамилии')
        print('8. Сохранить список сотрудников в файл')
        print('9. Выйти из программы')
        choice = input('Введите номер команды: ')
        if choice == '1':
            for employee in employees:
                print(f"{employee['last_name']} {employee['first_name']}, {employee['age']} лет, {employee['position']}, {employee['salary']} руб.")
        elif choice == '2':
            employees = add_employee(employees)
        elif choice == '3':
            employees = edit_employee(employees)
        elif choice == '4':
            employees = delete_employee(employees)
        elif choice == '5':
            results = search_by_last_name(employees)
            for employee in results:
                print(f"{employee['last_name']} {employee['first_name']}, {employee['age']} лет, {employee['position']}, {employee['salary']} руб.")
        elif choice == '6':
            results = search_by_age(employees)
            for employee in results:
                print(f"{employee['last_name']} {employee['first_name']}, {employee['age']} лет, {employee['position']}, {employee['salary']} руб.")
        elif choice == '7':
            results = search_by_first_letter(employees)
            for employee in results:
                print(f"{employee['last_name']} {employee['first_name']}, {employee['age']} лет, {employee['position']}, {employee['salary']} руб.")
        elif choice == '8':
            save_employees(employees)
        elif choice == '9':
            break
        else:
            print('Неверный номер команды')

if __name__ == '__main__':
    main()