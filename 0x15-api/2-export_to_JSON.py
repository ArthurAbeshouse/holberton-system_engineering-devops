#!/usr/bin/python3
"""Exports data to json"""
from json import dump
from requests import get
from sys import argv


empo_url = "https://jsonplaceholder.typicode.com/users/"
tasks_url = "https://jsonplaceholder.typicode.com/todos/"


def data():
    """Parses data form API"""
    if len(argv) < 2:
        return print("Invalid")
    empo_id = argv[1]
    empo = get(empo_url + empo_id).json()["username"]
    tasks = get(tasks_url).json()
    task_list = []
    dict_new = {empo_id: task_list}
    for i in tasks:
        dict_new[empo_id].append({"task": i["title"],
                                  "completed": i["completed"],
                                  "username": empo})
    with open(empo_id + ".json", "w") as file:
        dump(dict_new, file)


if __name__ == "__main__":
    data()
