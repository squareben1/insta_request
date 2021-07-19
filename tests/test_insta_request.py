import json
from src.insta_request.insta_request import InstaRequest

with open('tests/user_object.json') as f:
    user_follower_object = json.load(f)

with open('tests/user_objects.json') as f:
    multi_user_follower_object = json.load(f)


def test_parse_follower():
    """"Should return array with one name & username."""
    assert InstaRequest.parse_followers(user_follower_object) == [
        {"test_username", "Test Tester"}]


def test_parse_followers():
    """"Should return array with two names & usernames."""
    assert InstaRequest.parse_followers(multi_user_follower_object) == [
        {"test_username", "Test Tester"},
        {"test_username2", "Test Testerson"}
    ]
