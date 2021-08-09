import json
from src.insta_request.insta_request import InstaRequest

with open('tests/user_object.json') as f:
    user_follower_object = json.load(f)

with open('tests/user_objects.json') as f:
    multi_user_follower_object = json.load(f)

requestInstance = InstaRequest()


class TestRequest:
    def test_get_user_id(self):
        """"Should return user_id"""
        assert requestInstance.get_user_id("therock") == "232192182"


class TestParse:

    def test_parse_follower(self):
        """"Should return array with one name & username."""
        assert requestInstance.parse_followers(user_follower_object) == [
            {"test_username", "Test Tester"}]

    def test_parse_followers(self):
        """"Should return array with two names & usernames."""
        assert requestInstance.parse_followers(multi_user_follower_object) == [
            {"test_username", "Test Tester"},
            {"test_username2", "Test Testerson"}
        ]
