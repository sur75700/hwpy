class MyShows:
    def __init__(self, name, shows_user, year, the_actors):
        if type(name) == str:
            self.__name = name
        if type(shows_user) == str:
            self.__show_user = shows_user
        if type(year) == int:
            self.__year = year
        if isinstance(the_actors, list) and [i.isalpha() for i in the_actors]:
            self.__the_actors = the_actors
        else:
            raise ValueError("INVALID INFORMATION !!!")
        self.__rating = None
        self.__seria = 1

    @property
    def spr(self):
        return self.__seria

    @property
    def ypr(self):
        return self.__year

    @property
    def rpr(self):
        return self.__rating

    @property
    def npr(self):
        return self.__name

    @property
    def sh_upr(self):
        return self.__show_user

    @property
    def t_apr(self):
        return self.__the_actors

    @spr.setter
    def spr(self, seria):
        if type(seria) == int:
            self.__seria = seria
        else:
            raise ValueError("Invalid N-seria !!!")

    @ypr.setter
    def ypr(self, year):
        if type(year) == int:
            self.__year = year
        else:
            raise ValueError("Invalid year !!!")

    @rpr.setter
    def rpr(self, rating):
        if isinstance(rating, int | float) and 0 < rating < 10.1:
            self.__rating = rating
        else:
            raise ValueError("Invalid rating !!!")

    def new_actors(self, lst):
        if isinstance(lst, list) and [i.isalpha() for i in lst]:
            self.__the_actors.clear()
            return self.__the_actors + lst
        else:
            raise ValueError("Invalid actors_names !!!")

    def plus_minus_actors(self, x, y):
        if x.isalpha():
            self.__the_actors.append(x), self.__the_actors.remove(y)
            return self.__the_actors
        else:
            raise ValueError("EroR !!!")

    def information(self):
        return f' Name is film {self.__name},seria-{self.__seria}, year-{self.__year},actors-{self.__the_actors+lst} and can you watch this movie Media-{self.__show_user}'


film_1 = MyShows("Rembo", 'NetFlix', 1982, ["Сильвестр Сталлоне", "Иветт Монреаль", "Базз Фейтшанс",
                                            "Ричард Кренна", "Джули Бенз", "Джулия Никсон-Соул"])
film_1.spr += 1
film_1.ypr = 1985
film_1.rpr = 8.5
lst = ['Сильвестр Сталлоне', "Ричард Кренна", "Джулия Никсон-Соул", "Чарльз Напьер", "Мартин Коув", "Энди Вуд"]

print(film_1.npr, film_1.spr, film_1.ypr)
print(film_1.new_actors(lst))
print(film_1.information())
print(f'\033[93mI appreciate this movie -  *{film_1.rpr}*\033[0m')