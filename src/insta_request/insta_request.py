import requests
import json
import os

from dotenv import load_dotenv

load_dotenv()

with open('data/user_id.json') as f:
    user_data = json.load(f)

# user_id = user_data['user_id']
# print("user_data: ", user_data)
# print("user_id: ", user_id)

with open('data/user_following.json') as f:
    user_following_data = json.load(f)

# following = user_following_data['body']['users']

API_KEY = os.environ['API_KEY']
USER_ID = os.environ['USER_ID']

headers = {
    'x-rapidapi-key': API_KEY,
    'x-rapidapi-host': "instagram47.p.rapidapi.com"
}

# print("user_following_data: ", user_following_data)
# print("following: ", following)
# print("following LENGTH: ", len(following))


def get_user_id(username):
    get_user_id_url = "https://instagram47.p.rapidapi.com/get_user_id"
    querystring = {"username": username}
    response = requests.request(
        "GET", get_user_id_url, headers=headers, params=querystring)
    userid = response.text[0]
    print("get_user_id response.text: ", response.text)
    print("userid: ", userid)
    return response


def get_user_following(user_id):
    user_following_url = "https://instagram47.p.rapidapi.com/user_following"
    querystring = {"userid": user_id}
    user_following_response = requests.request("GET", user_following_url,
                                               headers=headers, params=querystring)
    print("user_following_response.text: ", user_following_response.text)
    return user_following_response


def get_user_followers(user_id):
    user_followers_url = "https://instagram47.p.rapidapi.com/user_followers"
    querystring = {"userid": user_id}
    response = requests.request(
        "GET", user_followers_url, headers=headers, params=querystring)
    print("response.text: ", response.text)
    return response


def parse_followers(follower_list):
    username = follower_list['body']['edges'][0]['node']['username']
    full_name = follower_list['body']['edges'][0]['node']['full_name']
    print(username)
    print(full_name)
    return [{username, full_name}]
