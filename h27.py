# HW28
class BankUser:
    def __init__(self, name, surname, age, C_N, balance, password):
        if not (self._is_valid_name(name) and self._is_valid_surname(surname) and self._is_valid_age(
                age) and self._is_valid_C_N(C_N) and self._is_valid_balance(balance) and self._is_valid_password(
            password)):
            raise ValueError("Invalid parameters !")
        self.name = name
        self.surname = surname
        self.age = age
        self.C_N = C_N
        self.balance = balance
        self.password = password

    @staticmethod
    def _is_valid_name(name):
        return type(name) == str and name.isalpha()

    @staticmethod
    def _is_valid_surname(surname):
        return type(surname) == str and surname.isalpha()

    @staticmethod
    def _is_valid_age(age):
        return type(age) == int

    @staticmethod
    def _is_valid_C_N(C_N):
        if type(C_N) == str:
            if len(C_N) == 16:
                return C_N.isdigit()
            elif len(C_N) == 19:
                return (C_N[:4] + C_N[5:9] + C_N[10:14] + C_N[15:]).isdigit() and C_N[4::5] == "   "
        return False

    @staticmethod
    def _is_valid_balance(balance):
        return isinstance(balance, int | float) and balance >= 0

    @staticmethod
    def _is_valid_password(password):
        return type(password) is str and len(password) >= 8

    def password_x(self):
        stop = 0
        while True:
            if stop == 3:
                print('Blok Credit cart !!! ')
                break
            p = input("Write your password !!! - ")
            if p != self.password:
                print("Imvalid password,,chance !. Write true password!")
                stop += 1
                continue
            if p == self.password:
                print(BankUser.__dict__)

            print("Information C_N !")
            break


user1 = BankUser("Ani", "Danelian", 25, '5020 6587 6585 7710', 50000, 'qwerty123456')
print(user1.password_x())

# class CAR:
#     def __init__(self, car_id):
#         self.car_id = car_id
#
#
# # car=CAR("75GV700","Mercedes")
# # print(car.car_id)
#
# class ParkingLot:
#     def __init__(self, total_spots, buy_spots):
#         self.total_spots = total_spots
#         self.buy_spots = buy_spots
#         self.hour_value = 500
#         self.wallet = 0
#
#     def park_car(self, car):
#         if self.total_spots - self.buy_spots > 0:
#             self.buy_spots += 1
#             return f'Parking {car}-numbers  car!!!'
#         else:
#             return f'Parking lot is full !.SORYY !'
#
#     def release_car(self, car):
#         self.buy_spots -= 1
#         return f'Have a nice trip ~~~ {car}-numbers car !!!'
#
#     def buy_park(self, car):
#         P1H_M = int(input("How long have you parked ? -  "))
#         if P1H_M >= 1:
#             self.wallet += 500 * P1H_M
#             return f"Your fee is {500 * P1H_M}AMD !"
#         else:
#             return f"your fee is 0 AMD,Have a nice trip !"
#
#     def spots_lef(self):
#         f = input("Write X ! - ")
#         if f == "X":
#             return f'So {self.total_spots - self.buy_spots} parking spaces left'
#         else:
#             'Invalid input !!!'
#
#
# car1 = CAR("75GV700")
# car2 = CAR("55SS777")
# car3 = CAR("77ZI507")
# car4 = CAR("32KW999")
# car5 = CAR("53JG305")
# parking = ParkingLot(15, 12)
# print(parking.park_car(car1.car_id))
# print(parking.park_car(car2.car_id))
# print(parking.park_car(car3.car_id))
# print(parking.park_car(car4.car_id))
# print(parking.park_car(car5.car_id))
# print(parking.buy_park(car2.car_id))
# print(parking.release_car(car2.car_id))
# print(parking.park_car(car5.car_id))
# print(parking.buy_park(car3.car_id))
# print(parking.release_car(car3.car_id))
# print(parking.park_car(car4.car_id))
# print(parking.wallet)
# print(parking.spots_lef())
