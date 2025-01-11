import pytest
from django.contrib.auth import get_user_model
from rest_framework.serializers import ValidationError

pytestmark = pytest.mark.django_db

User = get_user_model()


def test_user_model_behavior_create_regular_user_sucessful():
    # Arrange
    user_info = {
        "email": "test@example.com",
        "first_name": "Test_First_Name",
        "last_name": "Test_First_Name",
        "password": "testpassword",
    }

    # Act
    user = User.objects.create_user(**user_info)

    # Assert
    assert user.email == user_info["email"]
    assert user.first_name == user_info["first_name"]
    assert user.last_name == user_info["last_name"]
    assert user.check_password(user_info["password"])
    assert user.is_active
    assert not user.is_staff


@pytest.mark.parametrize(
    "user_info",
    [
        {
            "email": "",  # Missing email
            "first_name": "Test_First_Name",
            "last_name": "Test_First_Name",
            "password": "testpassword",
        },
        {
            "email": "test@example.com",
            "first_name": "",  # Missing first name
            "last_name": "Test_First_Name",
            "password": "testpassword",
        },
        {
            "email": "test@example.com",
            "first_name": "Test_First_Name",
            "last_name": "",  # Missing last name
            "password": "testpassword",
        },
        {
            "email": "test@example.com",
            "first_name": "Test_First_Name",
            "last_name": "Test_First_Name",
            "password": "",  # Missing password
        },
    ],
)
def test_user_model_behavior_create_regular_user_missing_fields_should_raise_value_error(
    user_info,
):
    with pytest.raises(ValueError):  # noqa:PT011
        User.objects.create_user(**user_info)


@pytest.mark.parametrize(
    "invalid_mail",
    [
        "plainaddress",  # Missing @ and domain
        "@missinglocal.com",  # Missing local part
        "missing@domain",  # Incomplete domain
        "missing.domain@",  # Missing domain
        "two@@domain.com",  # Multiple @ symbols
        ".invalid@email.com",  # Leading dot in local part
        "invalid@email.com.",  # Trailing dot in domain
        "invalid.@email.com",  # Trailing dot in local part
        # Length Errors
        "email@" + "d" * 256 + ".com",  # Domain > 255 chars
        # Character Errors
        "invalid<>@email.com",  # Invalid special chars
        "invalid()@email.com",  # Invalid parentheses
        "invalid[]@email.com",  # Invalid brackets
        "invalid\\@email.com",  # Invalid backslash
        "invalid,@email.com",  # Invalid comma
        "çõñτªçτ@domain.com",  # Non-ASCII chars
        # Domain Errors
        "email@-domain.com",  # Domain starts with hyphen
        "email@domain-.com",  # Domain ends with hyphen
        "email@domain.c",  # Single char TLD
        "email@domain..com",  # Multiple dots in domain
        "email@.domain.com",  # Leading dot in domain
        # Space Errors
        "invalid email@email.com",  # Space in local part
        "invalid@email com",  # Space in domain
        # RFC 5321 Errors
        "email@domain.com@domain.com",  # Multiple @ in path
        "email@domain@domain.com",  # Multiple @ symbols
        "email@[IPv6:2001:db8::1]",  # IPv6 format
    ],
)
def test_user_model_behavior_invalid_email_should_fail(invalid_mail):
    user_info = {
        "email": invalid_mail,
        "first_name": "Test_First_Name",
        "last_name": "Test_First_Name",
        "password": "testpassword",
    }

    with pytest.raises(ValidationError):
        User.objects.create_user(**user_info)


def test_user_model_behavior_create_superuser_successful():
    user_info = {
        "email": "test@example.com",
        "first_name": "Test_First_Name",
        "last_name": "Test_First_Name",
        "password": "testpassword",
    }

    user = User.objects.create_superuser(**user_info)

    assert user.email == user_info["email"]
    assert user.first_name == user_info["first_name"]
    assert user.last_name == user_info["last_name"]
    assert user.check_password(user_info["password"])
    assert user.is_active
    assert user.is_staff
    assert user.is_superuser
