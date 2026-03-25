import pytest
import allure
from http import HTTPStatus

from clients.advertisement.advertisement_client import AdvertisementsClient
from clients.advertisement.advertisement_schema import (
    AdvertisementsListAdapter,
    ADVERTISEMENTS_LIST_JSON_SCHEMA,
)
from fixtures.advertisements import AdvertisementFixture
from tools.assertions.advertisement import assert_get_seller_advertisements_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema


@pytest.mark.regression
@pytest.mark.advertisement
class TestGetSellerAdvertisements:
    @allure.title("Get advertisements by seller id")
    @allure.description("Verify that seller advertisements can be retrieved")
    # BUG-004 (secondary, indirect impact):
    # create API returns invalid schema,
    # so request is used as expected data in assertions
    # TODO:
    # - switch to response-based assertions instead of request (BUG-004)
    # - refactor fixture to return full CreateAdvertisementResponseSchema
    def test_get_seller_advertisement(
        self,
        advertisement_client: AdvertisementsClient,
        function_advertisement: AdvertisementFixture,
    ):
        seller_id = function_advertisement.request.seller_id
        response = advertisement_client.get_advertisements_by_seller_api(seller_id)

        assert_status_code(response.status_code, HTTPStatus.OK)

        response_data = AdvertisementsListAdapter.validate_json(response.text)

        assert_get_seller_advertisements_response(
            response_data, function_advertisement.request, function_advertisement.id
        )

        validate_json_schema(response.json(), ADVERTISEMENTS_LIST_JSON_SCHEMA)
