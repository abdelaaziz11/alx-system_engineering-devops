#!/usr/bin/python3
""" Gather data from an API
using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys


if __name__ == "__main__":
    reqs = "https://jsonplaceholder.typicode.com/"
    user = requests.get(reqs + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(reqs + "todos", params={"userId": sys.argv[1]}).json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{})".format(
        user.get("name"), len(completed), len(todos)))
    [print("\t{}".format(c)) for c in completed]
