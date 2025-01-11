import re

import pytest
from allauth.account.models import EmailAddress
from django.core import mail
from django.urls import reverse
from faker import Faker
from rest_framework import status
from rest_framework.test import APIClient

from .constants import (
    TEST_USER_FIRST_NAME,
    TEST_USER_LAST_NAME,
    TEST_USER_PASSWORD,
)

fake = Faker()


@pytest.fixture
def user_data():
    return {
        "email": fake.email(),
        "first_name": TEST_USER_FIRST_NAME,
        "last_name": TEST_USER_LAST_NAME,
        "password1": TEST_USER_PASSWORD,
        "password2": TEST_USER_PASSWORD,
    }


@pytest.fixture
def authenticated_client(user_data):
    client = APIClient()  # only it can store crendietial token

    # Register user
    response = client.post(reverse("rest_register"), user_data)
    assert response.status_code == status.HTTP_201_CREATED

    # Get the validation key from mail body

    email_content = mail.outbox.pop(0)
    confirmation_lint = re.search(
        r"http://.*?account-confirm-email/.*?/", email_content.body
    ).group(0)
    key = confirmation_lint.split("/")[-2]

    # Veryfy email
    response = client.post(reverse("rest_verify_email"), {"key": key})
    assert response.status_code == status.HTTP_200_OK

    user = EmailAddress.objects.get(email=user_data["email"])
    assert user.verified

    # Login user
    login_data = {"email": user_data["email"], "password": user_data["password1"]}
    response = client.post(reverse("rest_login"), login_data)

    client.credentials(HTTP_AUTHORIZATION=f"Bearer {response.data['access']}")
    return client
