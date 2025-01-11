import re

import pytest
from django.contrib.auth import get_user_model
from django.core import mail
from django.urls import reverse
from rest_framework import status

pytestmark = pytest.mark.django_db

User = get_user_model()


def test_user_endpoint_change_password_successful(authenticated_client, user_data):
    password_info = {
        "old_password": user_data["password1"],
        "new_password1": "testpassword_new",
        "new_password2": "testpassword_new",
    }

    response = authenticated_client.post(reverse("rest_password_change"), password_info)
    assert response.status_code == status.HTTP_200_OK

    user = User.objects.get(email=user_data["email"])
    assert user.check_password(password_info["new_password1"])


def test_user_endpoint_change_password_a_new_password_not_matching_with_400_response(
    authenticated_client, user_data
):
    password_info = {
        "old_password": user_data["password1"],
        "new_password1": "testpassword_new_new",
        "new_password2": "testpassword_new",
    }
    response = authenticated_client.post(reverse("rest_password_change"), password_info)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_user_endpoint_rest_password_flow_successful(authenticated_client, user_data):
    # Request password reset
    response = authenticated_client.post(
        reverse("rest_password_reset"), {"email": user_data["email"]}
    )
    assert response.status_code == status.HTTP_200_OK

    # Get uid and token from confirmation link
    email_content = mail.outbox.pop(0)
    confirmation_link = re.search(
        "http://.*?password_rest/confirm/./.*?/", email_content.body
    ).group(0)

    split_link = confirmation_link.split("/")
    uid = split_link[-3]
    token = split_link[-2]

    # Confirm reset request
    confirm_data = {
        "new_password1": "testpassword_new_2",
        "new_password2": "testpassword_new_2",
        "uid": uid,
        "token": token,
    }
    response = authenticated_client.post(
        reverse("password_reset_confirm", args={"uid64": uid, "token": token}),
        confirm_data,
    )

    assert response.status_code == status.HTTP_200_OK

    user = User.objects.get(email=user_data["email"])
    assert user.check_password(confirm_data["new_password1"])
