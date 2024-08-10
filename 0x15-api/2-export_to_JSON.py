#!/usr/bin/python3
"""Implement API call to CSV"""
from sys import argv
import json
import requests


def api_to_json():
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    users = (requests.get(url + "users/" + user_id)).json()
    todos = (requests.get(url + "todos")).json()
    userName = users["username"]
    userDetails = []

    for todo in todos:
        if todo["userId"] == int(user_id):
            taskDict = {
                "task": todo["title"], "completed": todo["completed"],
                "username": userName
            }
            userDetails.append(taskDict)
    taskDict = {user_id: userDetails}

    with open(f"{user_id}.json", 'w') as file:
        json.dump(taskDict, file)


if __name__ == "__main__":
    api_to_json()
