import pytest

pytest_plugins = [
    "core.tests.user.fixtures",
    "core.tests.fixtures",
    "core.tests.articles.fixtures",
]


def pytest_collection_modifyitems(items):
    for item in items:
        if "structure" in item.name:
            item.add_marker(pytest.mark.structure)
        if "behavior" in item.name:
            item.add_marker(pytest.mark.behavior)
        if "endpoint" in item.name:
            item.add_marker(pytest.mark.endpoint)
