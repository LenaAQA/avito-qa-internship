import pytest

from clients.statistics.statistic_client import StatisticsClient, get_statistics_client


@pytest.fixture
def statistics_client() -> StatisticsClient:
    return get_statistics_client()
