#!/usr/bin/python3
"""comment"""

import requests
import sys


def function():
    """function"""
    id_u = int(sys.argv[1])
    user = requests.get('https://jsonplaceholder.typicode.com/users')
    for r_user in user.json():
        if r_user.get('id') == id_u:
            EMPLOYEE_NAME = (r_user.get('name'))
            break
    NUMBER_OF_DONE_TASKS = 0
    TOTAL = 0
    TASK_TITLE = []
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    for r_todos in todos.json():
        if r_todos.get('userId') == int(sys.argv[1]):
            TOTAL += 1
            if r_todos.get('completed') is True:
                NUMBER_OF_DONE_TASKS += 1
                TASK_TITLE.append(r_todos.get('title'))
    print('Employee {} is done with tasks({}/{}):'.format(EMPLOYEE_NAME,
                                                          NUMBER_OF_DONE_TASKS,
                                                          TOTAL))
    for task in TASK_TITLE:
        print('\t {}'.format(task))
if __name__ == '__main__':
    function()
