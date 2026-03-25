from http import HTTPStatus

import pytest
import re

from clients.advertisement.advertisement_client import (
    AdvertisementsClient,
    get_advertisements_client,
)
from clients.advertisement.advertisement_schema import CreateAdvertisementRequestSchema
from pydantic import BaseModel

from tools.assertions.base import assert_status_code


UUID_REGEX = r"\b[0-9a-fA-F\-]{36}\b"


# NOTE:
# Temporary model due to BUG-004 (create response is broken).
# Should include full response schema after fix.
class AdvertisementFixture(BaseModel):
    request: CreateAdvertisementRequestSchema
    id: str


@pytest.fixture
def advertisement_client() -> AdvertisementsClient:
    return get_advertisements_client()


# BUG-004: create API returns invalid schema (status instead of object)
# WORKAROUND: extract advertisement id from status string
# TODO: remove workaround and return full CreateAdvertisementResponseSchema after fix
@pytest.fixture
def function_advertisement(
    advertisement_client: AdvertisementsClient,
) -> AdvertisementFixture:
    request = CreateAdvertisementRequestSchema()
    response = advertisement_client.create_advertisement_api(request)

    assert_status_code(response.status_code, HTTPStatus.OK)
    data = response.json()
    status = data.get("status", "")

    match = re.search(UUID_REGEX, status)
    assert match, f"Cannot extract id from response: {data}"

    ad_id = match.group(0)

    return AdvertisementFixture(request=request, id=ad_id)
