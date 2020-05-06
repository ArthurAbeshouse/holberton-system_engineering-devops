#!/usr/bin/python3
"""Exports data to json"""
from json import dump
from requests import get
empo_url = "https://jsonplaceholder.typicode.com/users/"
tasks_url = "https://jsonplaceholder.typicode.com/todos/"


def data():
    """Parses data form API"""
    empo = get(empo_url).json()
    task_list = []
#    dict_new = {}
    user_dict = {}
    user_name = {}
    for u in empo:
        empo_id = u.get("id")
        user_dict[empo_id] = []
        user_name[empo_id] = u.get("username")
    for i in get(tasks_url).json():
        uid = i.get("userId")
        task_list.append({"username": user_name.get(uid),
                          "task": i.get("title"),
                          "completed": i.get("completed")})
#        print("uid:", uid)
        user_dict.get(uid).append(task_list)
    with open("todo_all_employees.json", "w") as jsonfile:
        dump(user_dict, jsonfile)


if __name__ == "__main__":
    data()
