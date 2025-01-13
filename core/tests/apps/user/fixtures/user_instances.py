import pytest


@pytest.fixture
def normal_user(user_factory):
    return user_factory.create()


@pytest.fixture
def super_user(user_factory):
    return user_factory.create(is_superuser=True, is_staff=True)
