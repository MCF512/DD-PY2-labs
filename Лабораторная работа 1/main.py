import doctest


class Car:
    def __init__(self, wheels_quantity, doors_quantity, car_type):
        """
        Создаем объект "Машина" для игры-конструктора авто

        :param wheels_quantity: количество колес машины
        :param doors_quantity: количество дверей машины
        :param car_type: тип машины

        Пример:
        >>>> car = Car(4,4,"Семейная") #инициализация экземпляра
        """

        if not isinstance(wheels_quantity, int):
            raise TypeError("Количество колес должно быть типа int")
        if wheels_quantity < 0:
            raise ValueError("Количество колес не может быть отрицательным")
        self.wheels_quantity = wheels_quantity

        if not isinstance(doors_quantity, int):
            raise TypeError("Количество дверей должно быть типа int")
        if doors_quantity <= 0:
            raise ValueError("Количество дверей не может быть отрицательным")
        self.doors = doors_quantity

        if not isinstance(car_type, str):
            raise TypeError("Тип машины должен быть типа str")
        self.car_type = car_type

    def add_wheels(self, wheel: int):
        """
        Добавить колесо к машине

        :param wheel: количество колес, добавляемых к машине
        :return: измененное количество колес

        Пример:
        >>> car = Car(4,4, "Семейная")
        >>> car.add_wheels(1) #wheels_quantity = 4 + 1 = 5
        """
        if not isinstance(wheel, int):
            raise TypeError("wheel должно быть типа int")
        if wheel < 0:
            raise ValueError("wheel не должно быть отрицательным")
        ...

    def add_doors(self, door: int):
        """
        Добавляем двери

        :param door: количество добавляемых дверей
        :return: измененное количество дверей

        Пример:
        >>> car = Car(4,4, "Семейная")
        >>> car.add_doors(1) #doors_quantity = 4 + 1 = 5
        """

        if not isinstance(door, (int)):
            raise TypeError("door должно быть типа int")
        if door < 0:
            raise ValueError("door не должно быть отрицательным")
        ...

    def change_car_type(self, new_car_type: str):
        """
        Изменяем тип машины

        :param new_car_type: Новый тип машины
        :return: Измененный тип машины

        Пример:
        >>> car = Car(4, 4, "Семейная")
        >>> car.change_car_type("Спортивная") #car_type = "Спортивная"
        """
        if not isinstance(new_car_type, str):
            raise TypeError("new_car_type должно быть типа str")
        ...


class Person:
    def __init__(self, age: int, name: str, job: str):
        """
        Конструктор человека :)
        :param age: возраст
        :param name: имя
        :param job: работа

        Пример:
        >>> person = Person(22, "Егор", "Инженер-конструктор")
        """

        if not isinstance(age, int):
            raise TypeError("age должно быть типа int")
        if age < 0:
            raise ValueError("age не может быть отицательным")
        self.age = age

        if not isinstance(name, str):
            raise TypeError("name должно быть типа str")
        self.name = name

        if not isinstance(job, str):
            raise TypeError("job должно быть типа str")
        self.job = job

    def change_age(self, new_age: int):
        """
        Функция позволяет изменить возрат
        :param new_age:
        :return: Измененный возраст

        Пример:
        >>> person = Person(22, "Егор", "Инженер-конструктор")
        >>> person.change_age(23) #age = 23
        """
        if not isinstance(new_age, int):
            raise TypeError("new_age должно быть типа int")
        ...

    def change_name(self, new_name):
        """
        Функция позволяет изменить имя
        :param new_name: новое имя
        :return: Измененное имя

        Пример:
        >>> person = Person(22, "Егор", "Инженер-конструктор")
        >>> person.change_name("Иван") # name = 'Иван'
        """
        if not isinstance(new_name, str):
            raise TypeError("new_name должно быть типа str")
        ...

    def change_job(self, new_job: str):
        """
        Функция позволяет изменить работу
        :param new_job: новая работа
        :return: Измененная работа

        Пример:
        >>> person = Person(22, "Егор", "Инженер-конструктор")
        >>> person.change_job("Python-разработчик") #job = "Python-разработчик"
        """
        if not isinstance(new_job, str):
            raise TypeError("new_job должно быть типа str")
        ...

class Video:
    def __init__(self, length_minutes: float, current_minute: float):
        """
        Класс для видеоплеера

        :param length_minutes: Длина видео
        :param current_minute: Текущая минута

        Пример:
        >>> video = Video(5, 1)
        """
        if not isinstance(length_minutes, (int, float)):
            raise TypeError("length_minutes должно быть типа int или float")
        if length_minutes < 0:
            raise ValueError("length_minutes не может быть отрицательным")
        self.length_minutes = length_minutes

        if not isinstance(current_minute, (int, float)):
            raise TypeError("current_minute должно быть типа int или float")
        if current_minute < 0:
            raise ValueError("current_minute не можеть быть отрицательным")
        self.current_minute = current_minute

    def change_length(self, new_length: float):
        """
        изменям длину видео
        :param new_length: новая длина видео
        :return: новая длина видео

        пример:
        >>> video = Video(5, 1)
        >>> video.change_length(6) #length_minutes = 6
        """
        if not isinstance(new_length, (int, float)):
            raise TypeError("new_length должно быть типа int или float")
        if new_length < 0:
            raise ValueError("new_length не может быть отрицательным")
        ...

    def rewind_minutes(self, change_minute: float):
        """
        Функция реализует перемотку видео
        :param change_minute: На сколько перемотать
        :return: self.current_minute

        пример:
        >>> video = Video(5, 1)
        >>> video.rewind_minutes(3) #current_minutes = 1 + 3 = 4
        >>> video.rewind_minutes(-1) # current_minutes = 4 - 1 = 3
        """
        if not isinstance(change_minute, (int, float)):
            raise TypeError("add_minute должно быть типа int или float")
        ...


if __name__ == "__main__":
    doctest.testmod()
