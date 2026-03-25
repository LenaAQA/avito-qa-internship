from enum import Enum


class APIRoutes(str, Enum):
    ADVERTISEMENT = "/api/1/item"
    SELLER_ADVERTISEMENTS = "/api/1/{seller_id}/item"
    STATISTIC_ADVERTISEMENT = "/api/1/statistic/{advertisement_id}"

    def __str__(self):
        return self.value
