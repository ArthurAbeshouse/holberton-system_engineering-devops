#!/usr/bin/python3
"""Gets todo list for employee bassed on id"""
from requests import get
from sys import argv


empo_url = "https://jsonplaceholder.typicode.com/users/"
tasks_url = "https://jsonplaceholder.typicode.com/todos/"


def data():
    """Parses data form API"""
    if len(argv) < 2:
        return print("Invalid")
    empo_id = (argv[1])
    empo = get(empo_url + empo_id).json()
    tasks = get(tasks_url).json()
    task_list = []
    num1 = 0  # Amount of tasks
    num2 = 0  # Amount of completed tasks
    for i in tasks:
        if i["userId"] == empo.get("id"):
            num1 += 1
            if i["completed"]:
                num2 += 1
                task_list.append(i["title"])
    print("Employee", empo.get("name"),
          "is done with tasks({}/{}):".format(num2, num1))

    for task in task_list:
        print("\t {}".format(task))


if __name__ == "__main__":
    data()
