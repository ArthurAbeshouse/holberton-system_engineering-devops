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
    dict_new = {}
    user_dict = {}
    user_name = {}
    for u in empo:
        empo_id = u.get("id")
        user_dict[empo_id] = []
        user_name[empo_id] = u.get("username")
#        tasks = get(tasks_url,"{}").foarmat(empo_id).json()
#        tasks = get(tasks_url + "?userId=" + empo_id).json()
    for i in get(tasks_url).json():
        uid = i.get("userId")
        task_list.append({"username": user_name.get(uid),
                          "task": i["title"],
                          "completed": i["completed"]})
        dict_new[uid] = task_list
    with open("todo_all_employees.json", "w") as file:
        dump(dict_new, file)


if __name__ == "__main__":
    data()
#userdict.get(uid).append(taskdict)
