from pydantic import BaseModel, Field, TypeAdapter


class StatisticsSchema(BaseModel):
    """
    Описание структуры статистики объявления.
    """

    likes: int
    view_count: int = Field(alias="viewCount")
    contacts: int


# NOTE:
# API inconsistency:
# - GET /statistic/{id} returns a list instead of a single object
# - expected: single StatisticsSchema
# Keeping list schema as a temporary solution (BUG-003)
GetStatisticResponseSchema = list[StatisticsSchema]

StatisticsListAdapter = TypeAdapter(list[StatisticsSchema])
STATISTICS_LIST_JSON_SCHEMA = StatisticsListAdapter.json_schema()
