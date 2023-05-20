class Shoe:
    def __init__(self, shoe_type, shoe_style, color, price, manufacturer, size):
        self.shoe_type = shoe_type
        self.shoe_style = shoe_style
        self.color = color
        self.price = price
        self.manufacturer = manufacturer
        self.size = size
        self.shoe_id = None

    def __str__(self):
        return f"ID: {self.shoe_id}\nТип обуви: {self.shoe_type}\nВид обуви: {self.shoe_style}\nЦвет: {self.color}" \
               f"\nЦена: {self.price}\nПроизводитель: {self.manufacturer}\nРазмер: {self.size}"

    @staticmethod
    def save_shoes_to_file(shoes, filename):
        with open(filename, "a") as file:
            for shoe in shoes:
                file.write(f"{shoe.shoe_id}\t{shoe.shoe_type}\t{shoe.shoe_style}\t{shoe.color}\t{shoe.price}\t"
                           f"{shoe.manufacturer}\t{shoe.size}\n")

    @staticmethod
    def load_shoes_from_file(filename):
        shoes = []
        with open(filename, "r") as file:
            for line in file:
                data = line.strip().split("\t")
                if len(data) == 7:
                    shoe_id, shoe_type, shoe_style, color, price, manufacturer, size = data
                    shoe = Shoe(shoe_type, shoe_style, color, price, manufacturer, size)
                    shoe.shoe_id = int(shoe_id)
                    shoes.append(shoe)
        return shoes
