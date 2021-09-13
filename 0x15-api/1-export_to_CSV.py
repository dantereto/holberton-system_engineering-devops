#!/usr/bin/python3
"""comment"""

import csv
import requests
import sys


def function():
    """function"""
    user = requests.get("https://jsonplaceholder.typicode.com/users")
    for r_user in user.json():
        if r_user.get("id") == int(sys.argv[1]):
            u = (r_user.get('username'))
            break
    TASK_TITLE = []
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    file = sys.argv[1] + '.csv'
    with open(file, mode='w') as f:
        write = csv.writer(f, delimiter=',', quotechar='"',
                           quoting=csv.QUOTE_ALL, lineterminator='\n')
        for r_todos in todos.json():
            if r_todos.get("userId") == int(sys.argv[1]):
                write.writerow([int(sys.argv[1]), u,
                                str(r_todos.get('completed')),
                                r_todos.get('title')])
if __name__ == "__main__":
    function()
