from model import Shoe
from view import ShoeView


class ShoeController:
    def __init__(self, shoe_model, shoe_view):
        self.shoe_model = shoe_model
        self.shoe_view = shoe_view

    def add_shoe(self):
        shoe_type = self.shoe_view.get_input("Введите тип обуви (мужская/женская): ")
        shoe_style = self.shoe_view.get_input("Введите вид обуви: ")
        color = self.shoe_view.get_input("Введите цвет: ")
        price = self.shoe_view.get_input("Введите цену: ")
        manufacturer = self.shoe_view.get_input("Введите производителя: ")
        size = self.shoe_view.get_input("Введите размер: ")

        shoe = Shoe(shoe_type, shoe_style, color, price, manufacturer, size)
        self.shoe_model.add_shoe(shoe)
        self.shoe_view.display_message("Обувь успешно добавлена.")

    def delete_shoe(self):
        shoe_id = self.shoe_view.get_input("Введите ID обуви для удаления: ")
        if self.shoe_model.delete_shoe(shoe_id):
            self.shoe_view.display_message("Обувь успешно удалена.")
        else:
            self.shoe_view.display_message("Ошибка при удалении обуви.")

    def search_shoe(self):
        shoe_id = self.shoe_view.get_input("Введите ID обуви для поиска: ")
        shoe = self.shoe_model.search_shoe(shoe_id)
        if shoe:
            self.shoe_view.display_shoe(shoe)
        else:
            self.shoe_view.display_message("Обувь не найдена.")

    def run(self):
        while True:
            choice = self.shoe_view.get_input("Выберите действие: "
                                              "1 - добавить обувь, "
                                              "2 - удалить обувь, "
                                              "3 - найти обувь, "
                                              "0 - выйти: ")

            if choice == "1":
                self.add_shoe()
            elif choice == "2":
                self.delete_shoe()
            elif choice == "3":
                self.search_shoe()
            elif choice == "0":
                break
            else:
                self.shoe_view.display_message("Некорректный выбор.")

        Shoe.save_shoes_to_file(self.shoe_model.shoes, "shoes.txt")


