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
    employee_name = users["name"]
    completed_task = 0
    assigned_task = 0
    task_title = []

    for todo in todos:
        if employee_id == todo['userId']:
            assigned_task += 1
            if todo["completed"]:
                completed_task += 1
                task_title.append(todo['title'])
    output = "Employee {} is done with task({}/{}):"
    print(output.format(employee_name, completed_task, assigned_task))
    for title in task_title:
        print(f"\t {title}")


if __name__ == "__main__":
    todo_list()
