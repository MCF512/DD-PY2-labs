import doctest


class Car:
    def __init__(self, wheels_quantity, doors_quantity, car_type):
        """
        ������� ������ "������" ��� ����-������������ ����

        :param wheels_quantity: ���������� ����� ������
        :param doors_quantity: ���������� ������ ������
        :param doors_quantity: ��� ������

        ������:
        >>>> car = Car(4,4,"��������") #������������� ����������
        """

        if not isinstance(wheels_quantity, int):
            raise TypeError("���������� ����� ������ ���� ���� int")
        if wheels_quantity < 0:
            raise ValueError("���������� ����� �� ����� ���� �������������")
        self.wheels_quantity = wheels_quantity

        if not isinstance(doors_quantity, int):
            raise TypeError("���������� ������ ������ ���� ���� int")
        if doors_quantity <= 0:
            raise ValueError("���������� ������ �� ����� ���� �������������")
        self.doors = doors_quantity

        if not isinstance(car_type, str):
            raise TypeError("��� ������ ������ ���� ���� str")
        self.car_type = car_type

    def add_wheels(self, wheel: int):
        """
        �������� ������ � ������

        :param wheel: ���������� �����, ����������� � ������
        :return: ���������� ���������� �����

        ������:
        >>> car = Car(4,4, "��������")
        >>> car.add_wheels(1) #wheels_quantity = 4 + 1 = 5
        """
        if not isinstance(wheel, int):
            raise TypeError("wheel ������ ���� ���� int")
        if wheel < 0:
            raise ValueError("wheel �� ������ ���� �������������")
        ...

    def add_doors(self, door: int):
        """
        ��������� �����

        :param door: ���������� ����������� ������
        :return: ���������� ���������� ������

        ������:
        >>> car = Car(4,4, "��������")
        >>> car.add_doors(1) #doors_quantity = 4 + 1 = 5
        """

        if not isinstance(door, (int)):
            raise TypeError("door ������ ���� ���� int")
        if door < 0:
            raise ValueError("door �� ������ ���� �������������")
        ...

    def change_car_type(self, new_car_type: str):
        """
        �������� ��� ������

        :param new_car_type: ����� ��� ������
        :return: ���������� ��� ������

        ������:
        >>> car = Car(4, 4, "��������")
        >>> car.change_car_type("����������") #car_type = "����������"
        """
        if not isinstance(new_car_type, str):
            raise TypeError("new_car_type ������ ���� ���� str")
        ...


class Person:
    def __init__(self, age: int, name: str, job: str):
        """
        ����������� �������� :)
        :param age: �������
        :param name: ���
        :param job: ������

        ������:
        >>> person = Person(22, "����", "�������-�����������")
        """

        if not isinstance(age, int):
            raise TypeError("age ������ ���� ���� int")
        if age < 0:
            raise ValueError("age �� ����� ���� ������������")
        self.age = age

        if not isinstance(name, str):
            raise TypeError("name ������ ���� ���� str")
        self.name = name

        if not isinstance(job, str):
            raise TypeError("job ������ ���� ���� str")
        self.job = job

    def change_age(self, new_age: int):
        """
        ������� ��������� �������� ������
        :param new_age:
        :return: ���������� �������

        ������:
        >>> person = Person(22, "����", "�������-�����������")
        >>> person.change_age(23) #age = 23
        """
        if not isinstance(new_age, int):
            raise TypeError("new_age ������ ���� ���� int")
        ...

    def change_name(self, new_name):
        """
        ������� ��������� �������� ���
        :param new_name: ����� ���
        :return: ���������� ���

        ������:
        >>> person = Person(22, "����", "�������-�����������")
        >>> person.change_name("����") # name = '����'
        """
        if not isinstance(new_name, str):
            raise TypeError("new_name ������ ���� ���� str")
        ...

    def change_job(self, new_job: str):
        """
        ������� ��������� �������� ������
        :param new_job: ����� ������
        :return: ���������� ������

        ������:
        >>> person = Person(22, "����", "�������-�����������")
        >>> person.change_job("Python-�����������") #job = "Python-�����������"
        """
        if not isinstance(new_job, str):
            raise TypeError("new_job ������ ���� ���� str")
        ...

class Video:
    def __init__(self, length_minutes: float, current_minute: float):
        """
        ����� ��� �����������

        :param length_minutes: ����� �����
        :param current_minute: ������� ������

        ������:
        >>> video = Video(5, 1)
        """
        if not isinstance(length_minutes, (int, float)):
            raise TypeError("length_minutes ������ ���� ���� int ��� float")
        if length_minutes < 0:
            raise ValueError("length_minutes �� ����� ���� �������������")
        self.length_minutes = length_minutes

        if not isinstance(current_minute, (int, float)):
            raise TypeError("current_minute ������ ���� ���� int ��� float")
        if current_minute < 0:
            raise ValueError("current_minute �� ������ ���� �������������")
        self.current_minute = current_minute

    def change_length(self, new_length: float):
        """
        ������� ����� �����
        :param new_length: ����� ����� �����
        :return: ����� ����� �����

        ������:
        >>> video = Video(5, 1)
        >>> video.change_length(6) #length_minutes = 6
        """
        if not isinstance(new_length, (int, float)):
            raise TypeError("new_length ������ ���� ���� int ��� float")
        if new_length < 0:
            raise ValueError("new_length �� ����� ���� �������������")
        ...

    def rewind_minutes(self, change_minute: float):
        """
        ������� ��������� ��������� �����
        :param change_minute: �� ������� ����������
        :return: self.current_minute

        ������:
        >>> video = Video(5, 1)
        >>> video.rewind_minutes(3) #current_minutes = 1 + 3 = 4
        >>> video.rewind_minutes(-1) # current_minutes = 4 - 1 = 3
        """
        if not isinstance(change_minute, (int, float)):
            raise TypeError("add_minute ������ ���� ���� int ��� float")
        ...


if __name__ == "__main__":
    doctest.testmod()
