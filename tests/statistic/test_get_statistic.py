import pytest
import allure
from http import HTTPStatus

from clients.statistics.statistic_client import StatisticsClient
from clients.statistics.statistics_schema import (
    StatisticsListAdapter,
    STATISTICS_LIST_JSON_SCHEMA,
)
from fixtures.advertisements import AdvertisementFixture
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from tools.assertions.statistics import assert_get_statistics_response


@pytest.mark.regression
@pytest.mark.advertisement
class TestGetStatisticById:
    @allure.title("Get statistic by advertisement id")
    @allure.description(
        "Verify that advertisement statistics can be retrieved by its id"
    )
    @pytest.mark.bug("BUG-003")
    # BUG-003 (primary):
    # GET /statistic/{id} returns list instead of single object
    # WORKAROUND:
    # - use list schema for response validation
    # - access first element [0] for assertions
    # BUG-001 (secondary, indirect impact):
    # create API returns invalid schema,
    # so request is used as expected data
    # TODO:
    # - update test to expect single StatisticsSchema object (BUG-003)
    # - switch to response-based assertions instead of request (BUG-004)
    # - refactor fixture to return full CreateAdvertisementResponseSchema
    def test_get_statistic(
        self,
        statistics_client: StatisticsClient,
        function_advertisement: AdvertisementFixture,
    ):
        response = statistics_client.get_statistic_api(function_advertisement.id)

        assert_status_code(response.status_code, HTTPStatus.OK)

        response_data = StatisticsListAdapter.validate_json(response.text)
        assert_get_statistics_response(response_data, function_advertisement.request)

        validate_json_schema(response.json(), STATISTICS_LIST_JSON_SCHEMA)
