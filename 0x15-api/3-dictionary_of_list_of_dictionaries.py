#!/usr/bin/python3
"""comment"""

import csv
import json
import requests
import sys


if __name__ == '__main__':
    """function"""
    user = requests.get("https://jsonplaceholder.typicode.com/users")
    u = user.json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos")
    todo = todo.json()

    dict_list = {}
    user_list = {}
    for users in u:
        id_u = users.get('id')
        dict_list[id_u] = []
        user_list[id_u] = users.get('username')
    for todos in todo:
        data = {}
        id_u = todos.get('userId')
        data['task'] = todos.get('title')
        data['completed'] = todos.get('completed')
        data['username'] = user_list.get(id_u)
        dict_list.get(id_u).append(data)
    with open('todo_all_employees.json', 'w') as f:
        json.dump(dict_list, f)
