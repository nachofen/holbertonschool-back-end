#!/usr/bin/python3
"""Write a Python script that, using the jsonplaceholder.typicode.com API,
that returns information for a given employee ID about his/her
TODO list progress."""

import csv
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

    with open(csv_filename, "w", newline="", encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
    # csv.writer is the function provided by the csv module that creates
    # a CSV writer object.
    # csv_file is the file object that you've opened using the open() func

        for task in user_todo:
            csv_writer.writerow([
                user['id'],
                user['username'],
                "True" if task["completed"] else "False",
                task["title"]
            ])
