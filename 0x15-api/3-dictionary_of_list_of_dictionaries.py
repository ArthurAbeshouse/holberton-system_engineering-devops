#!/usr/bin/python3
"""Exports data to json"""
from json import dump
from requests import get


empo_url = "https://jsonplaceholder.typicode.com/users/"
tasks_url = "https://jsonplaceholder.typicode.com/"


def data():
    """Parses data form API"""
    empo = get(empo_url).json()
    task_list = []
    dict_new = {}
    for u in empo:
        empo_id = str(u["id"])
        tasks = get(tasks_url + "todos?userId=" + empo_id).json()
        for i in tasks:
            task_list.append({"username": u["username"],
                              "task": i["title"],
                              "completed": i["completed"]})
        dict_new[empo_id] = task_list

    with open("todo_all_employees.json", "w") as file:
        dump(dict_new, file)


if __name__ == "__main__":
    data()
