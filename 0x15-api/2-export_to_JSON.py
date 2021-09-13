#!/usr/bin/python3
"""comment"""

import csv
import json
import requests
import sys


if __name__ == '__main__':
    """function"""
    user = requests.get("https://jsonplaceholder.typicode.com/users")
    for r_user in user.json():
        if r_user.get("id") == int(sys.argv[1]):
            u = (r_user.get('username'))
            break
    TASK_TITLE = []
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    for r_todos in todos.json():
        if r_todos.get("userId") == int(sys.argv[1]):
            TASK_TITLE.append((r_todos.get("completed"), r_todos.get("title")))
    value = []
    for task in TASK_TITLE:
        value.append({'task': task[1], "completed": task[0], "username": u})
    data = {str(sys.argv[1]): value}
    filename = '{}.json'.format(sys.argv[1])
    with open(filename, 'w') as f:
        json.dump(data, f)
