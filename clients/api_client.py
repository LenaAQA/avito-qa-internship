import allure
from typing import Any

from httpx import Client, URL, QueryParams, Response


class APIClient:
    def __init__(self, client: Client):
        """
        Базовый API клиент, принимающий объект httpx. Client.

        :param client: экземпляр httpx.Client для выполнения HTTP-запросов
        """
        self.client = client

    @allure.step("Make GET request to {url}")
    def get(self, url: URL | str, params: QueryParams | None = None) -> Response:
        """
        Выполняет GET-запрос.

        :param url: URL-адрес эндпоинта.
        :param params: GET-параметры запроса.
        :return: Объект Response с данными ответа.
        """
        return self.client.get(url, params=params)

    @allure.step("Make POST request to {url}")
    def post(self, url: URL | str, json: Any | None = None) -> Response:
        """
        Выполняет POST-запрос.

        :param url: URL-адрес эндпоинта.
        :param json: Данные в формате JSON.
        :return: Объект Response с данными ответа.
        """
        return self.client.post(url, json=json)

    @allure.step("Make DELETE request to {url}")
    def delete(self, url: URL | str) -> Response:
        """
        Выполняет DELETE-запрос (удаление данных).

        :param url: URL-адрес эндпоинта.
        :return: Объект Response с данными ответа.
        """
        return self.client.delete(url)
