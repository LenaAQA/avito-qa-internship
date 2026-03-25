import pytest
import allure
from http import HTTPStatus

from clients.advertisement.advertisement_client import AdvertisementsClient
from clients.advertisement.advertisement_schema import (
    CreateAdvertisementRequestSchema,
    CreateAdvertisementResponseSchema,
)
from tools.assertions.base import assert_status_code
from tools.assertions.advertisement import assert_create_advertisement_response
from tools.assertions.schema import validate_json_schema


@pytest.mark.regression
@pytest.mark.advertisement
class TestAdvertisement:
    @pytest.mark.xfail(
        reason="BUG-004: response schema mismatch (see BUGS.md)", strict=False
    )
    @allure.title("Create advertisement with valid data")
    @allure.description(
        "Verify successful creation of an advertisement with valid data"
    )
    @pytest.mark.bug("BUG-004")
    def test_create_advertisement(self, advertisement_client: AdvertisementsClient):
        request = CreateAdvertisementRequestSchema()
        response = advertisement_client.create_advertisement_api(request)
        assert_status_code(response.status_code, HTTPStatus.OK)

        response_data = CreateAdvertisementResponseSchema.model_validate_json(
            response.text
        )
        assert_create_advertisement_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())
