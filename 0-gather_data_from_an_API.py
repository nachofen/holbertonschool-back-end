#!/usr/bin/python3
"""Write a Python script that, using the jsonplaceholder.typicode.com API,
that returns information for a given employee ID about his/her
TODO list progress."""

import json
import requests
from sys import argv

if __name__ == "__main__":

    if len(argv) != 2:
        exit()

    employee_id = argv[1]
    user_req = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    )
    user = json.loads(user_req.text)

    user_todo_req = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    )
    user_todo = json.loads(user_todo_req.text)

    completed = 0
    not_completed = 0
    for task in user_todo:
        if task["completed"]:
            completed += 1
        else:
            not_completed += 1

    print(f"Employee {user['name']} is done with tasks"
          f"({completed}/{not_completed + completed}):")
    for task in user_todo:
        if task["completed"]:
            print(f'\t {task["title"]}')
