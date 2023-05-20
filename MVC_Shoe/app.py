from model import Shoe
from view import ShoeView
from controller import ShoeController


class ShoeModel:
    def __init__(self):
        self.shoes = []
        self.load_shoes()

    def load_shoes(self):
        self.shoes = Shoe.load_shoes_from_file("shoes.txt")

    def add_shoe(self, shoe):
        if self.shoes:
            shoe_id = self.shoes[-1].shoe_id + 1
        else:
            shoe_id = 1
        shoe.shoe_id = shoe_id
        self.shoes.append(shoe)

    def delete_shoe(self, shoe_id):
        for shoe in self.shoes:
            if shoe.shoe_id == int(shoe_id):
                self.shoes.remove(shoe)
                self.save_shoes_to_file()  # Сохранение обновленного списка обуви в файл
                return True
        return False

    def search_shoe(self, shoe_id):
        for shoe in self.shoes:
            if shoe.shoe_id == int(shoe_id):
                return shoe
        return None

    def save_shoes_to_file(self):
        with open("shoes.txt", "w") as file:
            for shoe in self.shoes:
                file.write(str(shoe) + "\n")


if __name__ == "__main__":
    shoe_model = ShoeModel()
    shoe_view = ShoeView()
    shoe_controller = ShoeController(shoe_model, shoe_view)

    shoe_controller.run()
