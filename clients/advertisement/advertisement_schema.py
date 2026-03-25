from pydantic import BaseModel, Field, ConfigDict, TypeAdapter

from tools.fakers import fake

from clients.statistics.statistics_schema import StatisticsSchema


class AdvertisementSchema(BaseModel):
    """
    Описание структуры объявления.
    """

    model_config = ConfigDict(populate_by_name=True)
    id: str
    seller_id: int = Field(alias="sellerId")
    name: str
    price: int
    statistics: StatisticsSchema
    created_at: str = Field(alias="createdAt")


# NOTE:
# API inconsistency (BUG-001):
# - POST /item requires `statistics` field in request
# - expected: statistics should be server-generated and not provided by client
# Temporary workaround:
# - auto-generate statistics via default_factory
# - remove field after API is fixed
class CreateAdvertisementRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание объявления.
    """

    model_config = ConfigDict(populate_by_name=True)

    seller_id: int = Field(alias="sellerID", default_factory=fake.seller_id)
    name: str = Field(default_factory=fake.advertisement_name)
    price: int = Field(default_factory=fake.price)

    statistics: StatisticsSchema = Field(
        default_factory=lambda: StatisticsSchema(
            likes=fake.likes(),
            viewCount=fake.view_count(),
            contacts=fake.contacts(),
        )
    )


class CreateAdvertisementResponseSchema(AdvertisementSchema):
    """
    Описание структуры ответа создания объявления.
    """

    pass


# NOTE:
# API inconsistency:
# - GET /item/{id} returns a list instead of a single object
# - expected: single AdvertisementSchema
# Keeping list schema as a temporary solution (BUG-002)
GetAdvertisementResponseSchema = list[AdvertisementSchema]
AdvertisementListAdapter = TypeAdapter(list[AdvertisementSchema])
ADVERTISEMENT_LIST_JSON_SCHEMA = AdvertisementListAdapter.json_schema()

GetAdvertisementsResponseSchema = list[AdvertisementSchema]
AdvertisementsListAdapter = TypeAdapter(list[AdvertisementSchema])
ADVERTISEMENTS_LIST_JSON_SCHEMA = AdvertisementsListAdapter.json_schema()
