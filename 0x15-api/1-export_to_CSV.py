#!/usr/bin/python3
"""This module implement API  call and save to csv file"""
import csv
from sys import argv
import requests


def api_to_csv():
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    users = (requests.get(url + "users/" + user_id)).json()
    todos = (requests.get(url + "todos")).json()
    mainList = []
    tempList = []

    userId = users["id"]
    userName = users["username"]
    fileName = f"{user_id}.csv"

    for todo in todos:
        if int(user_id) == todo["userId"]:
            tempList.extend(
                [userId, userName, todo["completed"], todo["title"]]
            )
            mainList.append(tempList)
            tempList = []

    with open(fileName, 'w', newline="") as file:
        csvWriter = csv.writer(file, quoting=csv.QUOTE_ALL)
        csvWriter.writerows(mainList)


if __name__ == "__main__":
    api_to_csv()
