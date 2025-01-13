import pytest

pytestmark = pytest.mark.django_db


def test_user_factory_behavior_create_normal_user_successful(normal_user):
    assert normal_user.first_name is not None
    assert normal_user.last_name is not None
    assert normal_user.email is not None
    assert normal_user.password is not None
    assert normal_user.is_active
    assert not normal_user.is_staff
    assert not normal_user.is_superuser


def test_user_factory_behavior_create_super_user_successful(super_user):
    assert super_user.first_name is not None
    assert super_user.last_name is not None
    assert super_user.email is not None
    assert super_user.password is not None
    assert super_user.is_active
    assert super_user.is_staff
    assert super_user.is_superuser
