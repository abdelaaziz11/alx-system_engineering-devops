#!/usr/bin/python3
""" Gather data from an API
using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
from sys import argv
import requests


if __name__ == "__main__":
    reqs = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(reqs + "users/{}".format(argv[1])).json()
    todos = requests.get(reqs + "todos", params={"userId": argv[1]}).json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{})"
            .format(user.get("name"), len(completed), len(todos)))
    for a in completed:
        print("\t{}".format(a))
