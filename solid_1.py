from abc import ABC,abstractmethod

class PizzaComponent(ABC):
    @abstractmethod
    def cost(self):
        pass

class PizzaBase(PizzaComponent):
    def __init__(self,size):
        self.size = size

    @property
    def cost(self):
        if self.size == 25:
            return 1
        elif self.size == 30:
            return 1.44

    def __str__(self):
        return f'Основа для пиццы {self.size} cм.'

class Topping(PizzaComponent):
    def __init__(self,price):
        self.price = price

    @property
    def cost(self):
        return self.price

class Pepperoni(Topping):
    def __init__(self):
        super().__init__(price=20)

class PizzaBuilder:
    def __init__(self):
        self.base = None
        self.toppings = []

    def set_base(self, size):
        self.base = PizzaBase(size)

    def add_toppings(self, topping):
        self.toppings.append(topping)

    def get_cost(self):
        if not self.base:
            return 0
        cost = self.base.cost
        for topping in self.toppings:
            cost += topping.cost
        return cost

    def get_description(self):
        if self.base:
            description = str(self.base)
            if self.toppings:
                description += ', ' + ', '.join([str(topping) for topping in self.toppings])
            return description
        else:
            return 'Не выбрана основа!'



class Pizzeria:
    def __init__(self):
        self.pizza_builder = PizzaBuilder()
        self.order = []

    def add_pizza(self):
        size = input('Выберите размер основы 25 или 30 см.')
        while size != '25' and size != '30':
            size = input('Выберите правильный размер основы 25 или 30 см.')
            self.pizza_builder.set_base(int(size))

            while True:
                topping = input('Выберите начининку:\n'
                                '1.Пеперони\n'
                                '0.Выход\n')
                if topping == '1':
                    self.pizza_builder.add_toppings(Pepperoni())
                elif topping == '0':
                    break
        self.order.append(self.pizza_builder)
        self.pizza_builder = PizzaBuilder()
        print('Пицца добавлена в зазказ')

    def remove_pizza(self):
        if not self.order:
            print('Ваш заказ пуст')
            return
        for i,pizza in enumerate(self.order):
            print(f'{i+1}.{pizza.get_description()}')
        pizza_num = input('Введите номер пиццы, которую хотите удалить:\n')
        while not pizza_num.isdigit() or int(pizza_num) > 1 or int(pizza_num) > len(self.order):
            pizza_num = input('Введите корректный номер: \n')
        del self.order[int(pizza_num)-1]
        print('Пицца удалена из заказа')

    def view_order(self):
        print('Ваш заказ: ')
        if not self.order:
            print('Пусто')
            return

        total_cost = 0
        for i,pizza in enumerate(self.order):
            cost = pizza.get_cost()
            total_cost += cost
            print(f'{i+1}.{pizza.get_description()}-{cost} руб.')
        print(f'ИТОГО: {total_cost} руб.')

    def clear_order(self):
        self.order = []
        print('Заказ очищен')

    def pay_order(self):
        if not self.order:
            print('Ваш заказ пуст')
            return

        total_cost = 0
        for pizza in self.order:
            total_cost += pizza.get_cost()
        print(f'Ваш зака на сумму {total_cost} руб. оплачен.Спасибо за покупку!')
        self.order = []

    def run(self):
        while True:
            print('Введите команду: \n'
                  '1.Добавить пиццу в заказ \n'
                  '2.Удалить пиццу из заказа \n'
                  '3.Просмотреть ваш заказа \n'
                  '4.Очистить заказ \n'
                  '5.Оплатить заказа \n'
                  '0.Выход\n')
            choice = input('>>>>>>>>>')

            if choice == '1':
                self.add_pizza()
            elif choice == '2':
                self.remove_pizza()
            elif choice == '3':
                self.view_order()
            elif choice == '4':
                self.clear_order()
            elif choice == '5':
                self.pay_order()
            elif choice == '0':
                break
            else:
                print('Некорректный ввод')
if __name__ == '__main__':
    Pizzeria().run()

