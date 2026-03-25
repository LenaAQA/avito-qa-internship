from httpx import Response
import allure

from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client
from tools.routes import APIRoutes


class StatisticsClient(APIClient):
    """
    Client for working with /api/1/statistic
    """

    @allure.step("Get statistic by advertisement id {advertisement_id}")
    def get_statistic_api(self, advertisement_id: str) -> Response:
        """
        Метод получения статистики.

        :param advertisement_id: Идентификатор объявления.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        url = APIRoutes.STATISTIC_ADVERTISEMENT.value.format(
            advertisement_id=advertisement_id
        )
        return self.get(url)


def get_statistics_client() -> StatisticsClient:
    return StatisticsClient(client=get_public_http_client())
