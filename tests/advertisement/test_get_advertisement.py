import pytest
import allure
from http import HTTPStatus


from clients.advertisement.advertisement_client import AdvertisementsClient
from clients.advertisement.advertisement_schema import (
    AdvertisementListAdapter,
    ADVERTISEMENT_LIST_JSON_SCHEMA,
)
from fixtures.advertisements import AdvertisementFixture
from tools.assertions.advertisement import assert_get_advertisement_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema


@pytest.mark.regression
@pytest.mark.advertisement
class TestGetAdvertisementById:
    @allure.title("Get advertisement by id")
    @allure.description("Verify that advertisement can be retrieved by its id")
    @pytest.mark.bug("BUG-002")
    # BUG-002 (primary):
    # GET /item/{id} returns list instead of single object
    # Workaround: using list schema
    # BUG-004 (secondary, indirect impact):
    # create API returns invalid schema,
    # so request is used as expected data in assertions
    # TODO:
    # - update GET /item/{id} to expect single object instead of list (BUG-002)
    # - switch to response-based assertions instead of request (BUG-004)
    # - refactor fixture to return full CreateAdvertisementResponseSchema
    def test_get_advertisement(
        self,
        advertisement_client: AdvertisementsClient,
        function_advertisement: AdvertisementFixture,
    ):
        response = advertisement_client.get_advertisement_api(function_advertisement.id)

        assert_status_code(response.status_code, HTTPStatus.OK)

        response_data = AdvertisementListAdapter.validate_json(response.text)
        assert_get_advertisement_response(
            response_data, function_advertisement.request, function_advertisement.id
        )

        validate_json_schema(response.json(), ADVERTISEMENT_LIST_JSON_SCHEMA)
