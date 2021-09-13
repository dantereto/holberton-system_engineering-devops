#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""

import requests
from sys import argv

if __name__ == "__main__":
    todos_url = 'https://jsonplaceholder.typicode.com/todos?userId=' + argv[1]
    todos_response = requests.get(todos_url)
    user_url = 'https://jsonplaceholder.typicode.com/users/' + argv[1]
    user_response = requests.get(user_url)

    task_done_list = []
    task_done = 0
    lenght = len(todos_response.json())
    user_name = user_response.json().get('name')

    for user in todos_response.json():
        if user['completed'] is True:
            task_done_list.append(user['title'])
            task_done = task_done + 1

    print('Employee {} is done with tasks({}/{}):\
        '.format(user_name, task_done, lenght))
    for task in task_done_list:
        print('\t {}'.format(task))
