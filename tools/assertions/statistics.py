import allure

from clients.advertisement.advertisement_schema import CreateAdvertisementRequestSchema
from clients.statistics.statistics_schema import (
    StatisticsSchema,
    GetStatisticResponseSchema,
)
from tools.assertions.base import assert_equal, assert_length
from tools.logger import get_logger


logger = get_logger("STATISTICS_ASSERTIONS")


@allure.step("Check statistics")
def assert_statistics(actual: StatisticsSchema, expected: StatisticsSchema):
    logger.info("Check statistics")

    assert_equal(actual.likes, expected.likes, "likes")
    assert_equal(actual.view_count, expected.view_count, "view_count")
    assert_equal(actual.contacts, expected.contacts, "contacts")


# NOTE:
# - API returns list instead of single object (BUG-003)
# - request is used as expected data due to create API bug (BUG-004)
# Should be refactored after API fixes:
# - use single StatisticsSchema instead of list
# - switch to response-based assertions
@allure.step("Check get statistics response")
def assert_get_statistics_response(
    get_statistics_response: GetStatisticResponseSchema,
    expected_request: CreateAdvertisementRequestSchema,
):
    """
    Проверяет, что ответ на получение статистики соответствует данным запроса.

    :param get_statistics_response: Ответ API (список статистики)
    :param expected_request: Данные запроса на создание объявления
    """
    logger.info("Check get statistic response")

    assert_length(get_statistics_response, [expected_request.statistics], "statistics")

    assert_statistics(get_statistics_response[0], expected_request.statistics)
