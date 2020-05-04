#!/usr/bin/python3
"""Exports data to json"""
from requests import get
from sys import argv
from json import dump


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
    _dict = {}
    dict_new = {str(empo_id): task_list}
    for i in tasks:
        #        if i["userId"] == empo_id:
        _dict["task"] = i["title"]
        _dict["completed"] = i["completed"]
        _dict["username"] = empo
        task_list.append(_dict)
    with open(empo_id + ".json", "w") as file:
        dump(dict_new, file)


if __name__ == "__main__":
    data()
