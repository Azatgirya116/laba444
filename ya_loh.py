class KettlebellСollection:
    def __init__(self, kettlebell_number: int, kettlebell_price: float):
        """
        Создание и подготовка к работе объекта "Коллекция гирь"
        :param kettlebell_number: Колличество гирь в коллекции
        :param kettlebell_price: Стоимость всех гирь
         Примеры:

        >>> kettlebell = KettlebellСollection(999, 189000)  # инициализация экземпляра класса
        """
        if not isinstance(kettlebell_number, int):
            raise TypeError("Число гирь в коллекции должно быть типа int")
        if kettlebell_number < 0:
            raise ValueError("Число гирь в коллекции должно быть положительным числом")
        self.kettlebell_number = kettlebell_number
        if not isinstance(kettlebell_price, (int, float)):
            raise TypeError("Цена гирь в коллекции должна быть типа int или float")
        if kettlebell_price < 0:
            raise ValueError("Цена гирь в коллекции должна быть положительным числом")
        self.kettlebell_price = kettlebell_price


    def __str__(self):
        """ Метод str, возвращающий колличество и стоимость гирь в коллекции"""
        return f"Колличество гирь {self.kettlebell_number}. Стоимость коллекции {self.kettlebell_price}."


    def __repr__(self):
        """ Метод repr, возвращающий колличество и стоимость гирь в коллекции"""
        return f"{self.__class__.__name__}(kettlebell_number={self.kettlebell_number!r}, kettlebell_price={self.kettlebell_price!r})"


    def single_kettlebell(self) -> float:
        """
        Функция которая определяет цену одной гири
        :return: Цена одной гири

        Примеры:
        >>> kettlebell  = KettlebellСollection(999, 18900.0)
        >>> kettlebell.single_kettlebell()
        """
        ...
    def coolest_kettlebell(self) -> int:
        """
            Функция, которая определяет самую крутую гирю
            :return: Случайный номер гири из общего числа гирь

            Примеры:
            >>> kettlebell  = KettlebellСollection(999, 18900.0)
            >>> kettlebell.coolest_kettlebell()
            """
        ...

class Kettlebell(KettlebellСollection):
    def __init__(self, kettlebell_number: int, kettlebell_price: float, kettlebell_weight: float):
        """
        Создание и подготовка к работе объекта "Коллекция гирь"
        :param kettlebell_number: Колличество гирь в коллекции
        :param kettlebell_price: Стоимость всех гирь
        :param kettlebell_weight: Масса гири

         Примеры: kettlebell  = Kettlebell(999, 18900.0,9.5)
         """
        if not isinstance(kettlebell_weight, (int, float)):
            raise TypeError("Масса гири должена быть типа int или float")
        if kettlebell_weight < 0:
            raise ValueError("Масса гири должна быть положительным числом больше нуля")
        self.kettlebell_weight = kettlebell_weight

    def __repr__(self):
        """ Метод repr, возвращающий колличество и стоимость гирь в коллекции, вес заданной гири"""
        return f"{self.__class__.__name__}(kettlebell_number={self.kettlebell_number!r}, kettlebell_price={self.kettlebell_price!r}, kettlebell_weight={self.kettlebell_weight!r} )"
    def coolest_kettlebell(self) -> int:
        """
            Функция, которая определяет самую крутую гирю
            :return: Выводит заданный вес гири, определяя текущую гирю как самую крутую

            Примеры:
            >>> kettlebell  = Kettlebell(999, 18900.0, 500)
            >>> kettlebell.coolest_kettlebell()
            """
        ...

if __name__ == "__main__":
    pass