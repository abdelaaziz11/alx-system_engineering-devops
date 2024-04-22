#!/usr/bin/python3
""" Gather data from an API """
import requests
from sys import argv


if __name__ == "__main__":
    #api url
    reqs = "https://jsonplaceholder.typicode.com/"

    #user and todos url with ID
    user = requests.get(reqs + "users/{}".format(argv[1])).json()
    todos = requests.get(reqs + "todos", params={"userId": argv[1]}).json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]

    print("Employee {} is done with tasks({}/{})".format(
        user.get("name"), len(completed), len(todos)))

    [print("\t {}".format(a)) for a in completed]
