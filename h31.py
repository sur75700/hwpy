# HW 32
class Restaurant:
    def __init__(self, name, tables):
        self.name = name
        self.tables = tables
        self.res = {}

    def make_reservation(self, name, table, date):
        if date not in self.res:
            if table <= self.tables:
                self.res[date] = self.tables - table
                print(f"Reservation made for {name} at {date}.")
            else:
                print('No seats available.')
        else:
            if table <= self.res[date]:
                self.res[date] -= table
                print(f"Reservation made for {name} at {date}.")
            else:
                print('No seats available.')

    def order_food(self, *args):
        print(f"Order with {', '.join(args)} placed!։")


class FastFoodRestaurant(Restaurant):
    def __init__(self, name):
        self.name = name

    def make_reservation(self, name, table, date):
        print('We do not take reservations.')


restaurant = Restaurant('Paradise', 5)
restaurant.make_reservation('Anna', 2, '2024-05-06-19')

restaurant.make_reservation('Ashot', 3, '2024-05-07-19') 
restaurant.make_reservation('Mary', 1, '2024-05-07-19')
restaurant.make_reservation('Lilit', 2, '2024-05-07-19')

fast_food = FastFoodRestaurant('Burger World')
fast_food.make_reservation('John', 2, '2023-10-24-19')
fast_food.order_food('Burger', 'Soda')