import requests
import json
import os

from dotenv import load_dotenv

load_dotenv()

with open('data/user_id.json') as f:
    user_data = json.load(f)

with open('data/user_following.json') as f:
    user_following_data = json.load(f)

API_KEY = os.environ['API_KEY']
USER_ID = os.environ['USER_ID']

headers = {
    'x-rapidapi-key': API_KEY,
    'x-rapidapi-host': "instagram47.p.rapidapi.com"
}


class InstaRequest():
    def __init__(self) -> None:
        pass

    def get_user_id(self, username):
        get_user_id_url = "https://instagram47.p.rapidapi.com/get_user_id"
        querystring = {"username": username}
        response = requests.request(
            "GET", get_user_id_url, headers=headers, params=querystring)

        json_response = json.loads(response.text)
        self.userid = json_response['user_id']
        print("get_user_id response.text: ", response.text)
        print("json load response.text: ", json.loads(response.text))
        print("userid: ", self.userid)
        return response

    def get_user_following(self, user_id):
        user_following_url = "https://instagram47.p.rapidapi.com/user_following"
        querystring = {"userid": user_id}
        user_following_response = requests.request("GET", user_following_url,
                                                   headers=headers, params=querystring)
        print("user_following_response.text: ", user_following_response.text)
        return user_following_response

    def get_user_followers(self, user_id):
        user_followers_url = "https://instagram47.p.rapidapi.com/user_followers"
        querystring = {"userid": user_id}
        response = requests.request(
            "GET", user_followers_url, headers=headers, params=querystring)
        print("response.text: ", response.text)
        return response

    def parse_followers(self, follower_list):
        """Return list of names & usernames."""
        array = []
        for user in follower_list['body']['edges']:
            username = user['node']['username']
            full_name = user['node']['full_name']
            array.append({username, full_name})
            print(username, full_name)
        print("pare_followers array: ", array)
        print("array length: ", len(array))
        return array

    # def execute()


# InstaRequest.get_user_id(username='NAME')
