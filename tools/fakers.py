from faker import Faker


class Fake:
    """
    Класс для генерации случайных тестовых данных с использованием библиотеки Faker.
    """

    def __init__(self, faker: Faker):
        """
        :param faker: Экземпляр класса Faker, который будет использоваться для генерации данных.
        """
        self.faker = faker

    def advertisement_name(self) -> str:
        """
        Генерирует название объявления.

        :return: Случайное название объявления.
        """
        return f"{self.faker.word().capitalize()} {self.faker.word()}"

    def seller_id(self) -> int:
        """
        Генерирует sellerId в допустимом диапазоне.

        :return: Случайный sellerId в диапазоне 111111–999999.
        """
        return self.faker.random_int(min=111111, max=999999)

    def price(self) -> int:
        """
        Генерирует цену объявления.

        :return: Случайная цена объявления.
        """
        return self.faker.random_int(min=1, max=1_000_000)

    def likes(self) -> int:
        """
        Генерирует количество лайков.

        :return: Случайное количество лайков.
        """
        return self.faker.random_int(min=0, max=100)

    def view_count(self) -> int:
        """
        Генерирует количество просмотров.

        :return: Случайное количество просмотров.
        """
        return self.faker.random_int(min=0, max=10_000)

    def contacts(self) -> int:
        """
        Генерирует количество контактов.

        :return: Случайное количество контактов.
        """
        return self.faker.random_int(min=0, max=100)


fake = Fake(faker=Faker())
