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

    csv_filename = f"{employee_id}.csv"

    user_data = {
        employee_id: [
            {
                "task": task["title"],
                "completed": task["completed"],
                "username": user["username"]
            }
            for task in user_todo
        ]
    }

    with open(f'{employee_id}.json', 'w', encoding='UTF=8') as f:
        json.dump(user_data, f)
