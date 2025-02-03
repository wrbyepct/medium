import pytest

pytestmark = pytest.mark.django_db


# Test follow method
def test_profile_model_behavior__follow_method_correct(two_profiles):
    fan, idol = two_profiles
    assert fan.following.all().count() == 0
    assert idol.followers.all().count() == 0

    # Act
    fan.follow(idol)
    idol.refresh_from_db()

    assert fan.following.all().count() == 1
    assert fan.has_followed(idol)

    assert idol.followers.all().count() == 1
    assert idol.followers.filter(pkid=fan.pkid).exists()


# Test unfollow method
def test_profile_model_behavior__unfollow_method_correct(two_profiles):
    # Arrange
    fan, idol = two_profiles

    fan.follow(idol)
    assert fan.has_followed(idol)
    # Act
    fan.unfollow(idol)
    assert not fan.has_followed(idol)
    assert fan.following.all().count() == 0
