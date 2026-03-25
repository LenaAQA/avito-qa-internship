import allure

from clients.advertisement.advertisement_schema import (
    CreateAdvertisementRequestSchema,
    CreateAdvertisementResponseSchema,
    AdvertisementSchema,
    GetAdvertisementsResponseSchema,
)
from tools.assertions.base import assert_equal, assert_length, assert_is_not_none
from tools.assertions.statistics import assert_statistics
from tools.logger import get_logger

logger = get_logger("ADVERTISEMENT_ASSERTIONS")


@allure.step("Check create advertisement response")
def assert_create_advertisement_response(
    request: CreateAdvertisementRequestSchema,
    response: CreateAdvertisementResponseSchema,
):
    """
    Проверяет, что ответ на создание объявления соответствует данным из запроса.
    :param request: Исходный запрос на создание объявления.
    :param response: Ответ API с данными объявления.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check create advertisement response")

    assert_equal(response.seller_id, request.seller_id, "seller_id")
    assert_equal(response.name, request.name, "name")
    assert_equal(response.price, request.price, "price")

    assert_statistics(response.statistics, request.statistics)

    assert_is_not_none(response.created_at, "created_at")
    assert_is_not_none(response.id, "id")


@allure.step("Check advertisement against request")
def assert_advertisement_from_request(
    actual: AdvertisementSchema,
    request: CreateAdvertisementRequestSchema,
    expected_id: str,
):
    logger.info("Check advertisement against request")

    assert_equal(actual.id, expected_id, "id")
    assert_equal(actual.seller_id, request.seller_id, "seller_id")
    assert_equal(actual.name, request.name, "name")
    assert_equal(actual.price, request.price, "price")

    assert_statistics(actual.statistics, request.statistics)

    assert_is_not_none(actual.created_at, "created_at")


# NOTE:
# Uses request instead of response due to BUG-004.
# Should be refactored to use assert_advertisement(actual, expected)
@allure.step("Check get advertisement response")
def assert_get_advertisement_response(
    get_advertisement_response: list[AdvertisementSchema],
    create_advertisement_request: CreateAdvertisementRequestSchema,
    expected_id: str,
):
    """
    Проверяет, что ответ на получение объявления соответствует данным запроса id ответа соответствует созданному.

    :param get_advertisement_response: Ответ API при запросе данных объявления.
    :param create_advertisement_request: Данные запроса на создание объявления.
    :param expected_id: Ожидаемый id объявления.
    :raises AssertionError: Если данные объявления не совпадают.
    """
    logger.info("Check get advertisement response")

    assert_length(
        get_advertisement_response, [create_advertisement_request], "advertisements"
    )
    assert_advertisement_from_request(
        get_advertisement_response[0], create_advertisement_request, expected_id
    )


# NOTE:
# Uses request instead of response due to BUG-004.
# Should be refactored to use assert_advertisement(actual, expected)
@allure.step("Check get advertisements response")
def assert_get_seller_advertisements_response(
    get_advertisements_response: GetAdvertisementsResponseSchema,
    expected_request: CreateAdvertisementRequestSchema,
    expected_id: str,
):
    """
    Проверяет, что ответ на получение списка объявлений соответствует ответам на их создание.

    :param get_advertisements_response: Ответ API при запросе списка объявлений.
    :param expected_request: Данные запроса на создание объявления.
    :param expected_id: Ожидаемый id объявления.
    :raises AssertionError: Если данные объявлений не совпадают.
    """
    logger.info("Check get advertisements response")
    expected = [expected_request]
    assert_length(get_advertisements_response, expected, "advertisements")
    for index, request in enumerate(expected):
        assert_advertisement_from_request(
            get_advertisements_response[index], request, expected_id
        )
