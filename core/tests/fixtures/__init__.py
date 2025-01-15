import pytest
from django.contrib.sessions.middleware import SessionMiddleware
from django.test import RequestFactory

"""
Q: Why Mock Request with SessionMiddleWare is Needed?

A: The functions from 'allauth' need it:

    def unstash_verified_email(self, request):
            ret = request.session.get("account_verified_email")
    >       request.session["account_verified_email"] = None
    E       TypeError: 'Mock' object does not support item assignment

    Those functions are used in CustomRegisterSerializer's .save()

Q: Then How do We mock it?
A: Mock it with django.test.RequestFactory
"""


@pytest.fixture
def mock_request():
    request = RequestFactory().get("/")
    middleware = SessionMiddleware(lambda req: None)  # noqa: ARG005
    middleware.process_request(request=request)
    request.session.save()
    return request
