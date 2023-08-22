#!/usr/bin/python3
"""Using what you did in the task #0, extend your Python script to export data in the JSON format."""

import json
import requests

if __name__ == "__main__":

    user_req = requests.get(
        'https://jsonplaceholder.typicode.com/users'
    )
    users = json.loads(user_req.text)

    all_users = {}

    for user in users:
        employee_id = str(user['id'])

        user_todo_req = requests.get(
            f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
        )
        user_todo = json.loads(user_todo_req.text)

        tasks = []
        for task in user_todo:
            tasks.append({
                "username": user['username'],
                "task": task['title'],
                "completed": task['completed']
            })

        all_users[employee_id] = tasks

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_users, json_file)
