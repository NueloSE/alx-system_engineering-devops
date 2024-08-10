#!/usr/bin/python3
"""
A python script that using the REST API for a given employee ID, returns
information about his/her TODO list progress.
"""
import requests
from sys import argv


def todo_list():
    """implement REST API call"""
    employee_id = int(argv[1])
    url = "https://jsonplaceholder.typicode.com/"
    users = (requests.get(url + "users/{}".format(employee_id))).json()
    todos = (requests.get(url + "todos/")).json()
    name = users["name"]
    taskDone = 0
    taskCount = 0
    taskTitle = []

    for todo in todos:
        if employee_id == todo['userId']:
            taskCount += 1
            if todo["completed"]:
                taskDone += 1
                taskTitle.append(todo['title'])
    output = (
        "Employee {} is done with tasks({}/{}):"
        .format(name, taskDone, taskCount)
    )
    print(output)
    for title in taskTitle:
        print(f"\t {title}")


if __name__ == "__main__":
    todo_list()
