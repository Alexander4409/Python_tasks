from abc import ABC, abstractmethod


class PizzaBase(ABC):
    @abstractmethod
    def cost(self):
        pass


class PizzaBase25cm(PizzaBase):
    @property
    def cost(self):
        return 1

    def __str__(self):
        return f'Основа для пиццы 25 см'


class PizzaBase30cm(PizzaBase):
    @property
    def cost(self):
        return 1.44

    def __str__(self):
        return f'Основа для пиццы 30 см'


class Topping:
    def __init__(self):
        self.name = self.__class__.__name__.lower()

    def __str__(self):
        return self.name


class Toppings:
    data = {'Cheese': 15, 'Tomatoes': 15, 'Pepperoni': 20,
            'Bacon': 25, 'Mushrooms': 20, 'Olives': 25,
            'Chicken': 20, 'Pineapple': 20}

    toppings = {}

    @staticmethod
    def init_toppings():
        for key, value in Toppings.data.items():
            Toppings.toppings[key] = type(key, (Topping,), {'cost': value})


class Pizza:
    def __init__(self, base, *toppings):
        self.base = base
        self.toppings = toppings

    @property
    def cost(self):
        return sum((top.cost for top in self.toppings)) * self.base.cost

    def __str__(self):
        base_str = str(self.base)
        toppings_str = ', '.join(str(top) for top in self.toppings)
        return f'{base_str} - {toppings_str}'


class PizzaTemplates:
    @staticmethod
    def Margarita(base=PizzaBase25cm()):
        return Pizza(base,
                     Toppings.toppings['Cheese'],
                     Toppings.toppings['Tomatoes'])

    @staticmethod
    def Pepperoni(base=PizzaBase25cm()):
        return Pizza(base,
                     Toppings.toppings['Cheese'],
                     Toppings.toppings['Pepperoni'])

    @staticmethod
    def BaconAndMushrooms(base=PizzaBase25cm()):
        return Pizza(base,
                     Toppings.toppings['Cheese'],
                     Toppings.toppings['Bacon'],
                     Toppings.toppings['Mushrooms'],
                     Toppings.toppings['Tomatoes'])


class Pizzeria:
    def __init__(self):
        self.sold_pizzas = 0
        self.revenue = 0
        self.profit = 0
        self.total_revenue = 0  # Add a total_revenue variable
        self.basket = []
        Toppings.init_toppings()

    def add_to_order(self, pizza):
        with open('orders.txt', 'a') as file:
            file.write(str(pizza))
            file.write('\n')

    def run(self):
        query = None
        self.make_an_order()
        while query != 'Exit':
            query = input('Введите команду:\n'
                          '1. Добавить пиццу в корзину\n'
                          '2. Удалить пиццу из корзины\n'
                          '3. Просмотреть ваш заказ\n'
                          '4. Очистить корзину\n'
                          '5. Оплатить товары в корзине:\n'
                          '6. Вывести данные о продажах\n'
                          '7. Exit\n')
            if query == '1':
                self.add_pizza()
            elif query == '2':
                self.remove_pizza()
            elif query == '3':
                self.view_order()
            elif query == '4':
                self.clear_basket()
            elif query == '5':
                self.checkout()
            elif query == '6':
                self.show_sales_data()
            elif query == '7':
                break

    def extract_price(self, line):
        if line.startswith('Total:'):
            return float(line.split(':')[1].strip())
        else:
            price_index = line.rfind(' - ') + 3
            return float(line[price_index:])

    def make_an_order(self):
        self.basket = []

    def add_pizza(self):
        query = input('Выберите опцию:\n'
                      '1. Выбрать одну из готовых пицц\n'
                      '2. Собрать пиццу самому!\n')
        pizza = None
        if query == '1':
            base = 'Введите номер пиццы, которую вы бы хотели заказать:\n'
            templates = list(PizzaTemplates.__dict__.items())
            for i, pizza in enumerate(templates):
                if isinstance(pizza[1], staticmethod):
                    base += f'{i}. {pizza[0]} - {", ".join(map(str, pizza[1]().toppings))}\n'
            choice = int(input(base))
            pizza_maker = templates[choice - 1][1]
            size = int(input('Введите размер пиццы (25 / 30): '))
            if size == 25:
                pizza = pizza_maker(PizzaBase25cm())
            else:
                pizza = pizza_maker(PizzaBase30cm())
        elif query == '2':
            base_size = int(input('Введите размер пиццы (25 / 30): '))
            if base_size == 25:
                base = PizzaBase25cm()
            else:
                base = PizzaBase30cm()
            toppings = []
            while True:
                topping_choice = input('Введите название топпинга (для завершения введите "Готово"): ')
                if topping_choice == 'Готово':
                    break
                if topping_choice in Toppings.toppings:
                    toppings.append(Toppings.toppings[topping_choice])
                else:
                    print('Некорректный топпинг.')
            pizza = Pizza(base, *toppings)
        else:
            print('Некорректный выбор опции.')

        if pizza:
            self.basket.append(pizza)
            print('Пицца добавлена в корзину.')

    def remove_pizza(self):
        if len(self.basket) > 0:
            index = int(input('Введите номер пиццы для удаления: '))
            if index >= 0 and index < len(self.basket):
                removed_pizza = self.basket.pop(index)
                print(f'Пицца "{removed_pizza}" удалена из корзины.')
            else:
                print('Ошибка: введен неверный номер пиццы.')
        else:
            print('Корзина пуста.')

    def view_order(self):
        if len(self.basket) > 0:
            print('Ваш заказ:')
            for i, pizza in enumerate(self.basket):
                print(f'{i}. {pizza} - {", ".join(map(str, pizza.toppings))}')
        else:
            print('Корзина пуста.')

    def clear_basket(self):
        if len(self.basket) > 0:
            self.basket = []
            print('Корзина очищена.')
        else:
            print('Корзина пуста.')

    def checkout(self):
        if len(self.basket) > 0:
            print('Оплата:')
            print('1. Наличные')
            print('2. Карта')
            payment_method = input('Выберите способ оплаты: ')
            if payment_method == '1':
                self.pay_cash()
            elif payment_method == '2':
                self.pay_card()
            else:
                print('Ошибка: неверный выбор способа оплаты.')
        else:
            print('Корзина пуста.')

    def pay_cash(self):
        total_cost = sum(pizza.cost for pizza in self.basket)
        print(f'Общая стоимость заказа: {total_cost} руб.')
        received_amount = float(input('Введите полученную сумму: '))
        if received_amount >= total_cost:
            change = received_amount - total_cost
            print(f'Спасибо за оплату! Сдача: {change} руб.')
            self.sold_pizzas += len(self.basket)
            self.revenue += total_cost
            self.profit += total_cost
            self.basket = []
            self.save_order_to_file(total_cost)  # Сохраняем заказ в файл
        else:
            print('Ошибка: недостаточно средств.')

    def pay_card(self):
        total_cost = sum(pizza.cost for pizza in self.basket)
        print(f'Общая стоимость заказа: {total_cost} руб.')
        self.sold_pizzas += len(self.basket)
        self.revenue += total_cost
        self.profit += total_cost
        self.basket = []
        self.save_order_to_file(total_cost)  # Сохраняем заказ в файл
        print('Оплата произведена успешно.')

    def save_order_to_file(self, total_cost):
        with open('orders.txt', 'a') as file:
            for pizza in self.basket:
                file.write(str(pizza) + '\n')
            file.write(f'Total: {total_cost}\n')

    def show_sales_data(self):
        total_revenue = 0
        with open('orders.txt', 'r') as file:
            print('Продажи:')
            for line in file:
                print(line, end='')
                if line.startswith('Total:'):
                    total_revenue += self.extract_price(line)
            print(f'Выручка: {total_revenue} руб.')

    # @staticmethod
    # def extract_price(line):
    #     price_index = line.rfind(' - ') + 3
    #     price = float(line[price_index:])
    #     return price

def main():
    app = Pizzeria()
    app.run()


if __name__ == '__main__':
    main()
