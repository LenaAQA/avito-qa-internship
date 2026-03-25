from httpx import Response
import allure

from clients.api_client import APIClient
from clients.advertisement.advertisement_schema import (
    CreateAdvertisementRequestSchema,
    CreateAdvertisementResponseSchema,
)
from clients.public_http_builder import get_public_http_client
from tools.routes import APIRoutes


class AdvertisementsClient(APIClient):
    """
    Клиент для работы с /api/1/item
    """

    @allure.step("Create advertisement")
    def create_advertisement_api(
        self, request: CreateAdvertisementRequestSchema
    ) -> Response:
        """
        Метод создания объявления.

        :param request: Данные для создания объявления.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(
            APIRoutes.ADVERTISEMENT, json=request.model_dump(by_alias=True)
        )

    @allure.step("Get advertisement by id {advertisement_id}")
    def get_advertisement_api(self, advertisement_id: str) -> Response:
        """
        Метод получения объявления.

        :param advertisement_id: Идентификатор объявления.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"{APIRoutes.ADVERTISEMENT}/{advertisement_id}")

    @allure.step("Get advertisements by seller id {seller_id}")
    def get_advertisements_by_seller_api(self, seller_id: int) -> Response:
        """
        Метод получения всех объявлений продавца.

        :param seller_id: Идентификатор продавца.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        url = APIRoutes.SELLER_ADVERTISEMENTS.value.format(seller_id=seller_id)
        return self.get(url)

    def create_advertisement(
        self, request: CreateAdvertisementRequestSchema
    ) -> CreateAdvertisementResponseSchema:
        response = self.create_advertisement_api(request)
        return CreateAdvertisementResponseSchema.model_validate_json(response.text)


def get_advertisements_client() -> AdvertisementsClient:
    """
    Функция создаёт экземпляр AdvertisementClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию AdvertisementClient.
    """
    return AdvertisementsClient(client=get_public_http_client())
